# -*- coding: utf-8 -*-
"""
전문용어 검수 —  python _tools/check_terms.py

전문용어는 검색 유입 때문에 반드시 남깁니다. 사람들이 그 말로 검색하기 때문입니다.
다만 처음 나올 때 옆에 쉬운 말을 붙여야 읽는 사람이 이해합니다.

이 스크립트는 페이지마다 각 용어가 '처음 나오는 자리'를 찾아,
그 근처에 풀이가 붙어 있는지 확인합니다.
"""
import os, re, sys
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
DIST = os.path.join(ROOT, "dist")

# 용어 → 이 낱말들 중 하나가 근처에 있으면 "풀이가 붙었다"고 본다
TERMS = {
    "IPCC":      ["콜센터 시스템", "하나로 묶", "통합", "인터넷 전화", "인터넷전화", "나눠주고", "교환기"],
    "IP-PBX":    ["교환기", "나눠주는"],
    "CTI":       ["전화와", "상담 화면", "상담화면", "연결하는", "심장", "분배", "화면에 띄"],
    "ACD":       ["분배", "배분", "나눕니다", "나눠주는"],
    "IVR":       ["자동안내", "자동 안내", "갈라", "자동응답", "자동 응답", "사람 없이 안내", "안내하고"],
    "ARS":       ["자동응답", "자동 응답", "안내", "화면에서 고", "음성"],
    "VoIP":      ["인터넷전화", "인터넷 전화"],
    "STT":       ["글로", "텍스트", "음성인식", "음성 인식"],
    "AICC":      ["AI 콜센터", "AI 컨택센터", "음성인식과 AI", "AI를 붙인", "사람 없이 처리"],
    "SIP":       ["인터넷전화", "규격", "표준"],
    "CRM":       ["고객관리", "고객 관리", "상담 화면", "상담화면", "고객이 먼저 뜹", "고객 정보"],
    "PBX":       ["교환기"],
    "TTS":       ["음성으로", "글로 입력"],
    "SLA":       ["장애 대응", "응답 기준", "약속"],
    "호분배":     ["분배", "배분", "나눕니다", "ACD"],
    "전광판":     ["현황", "상태", "대기", "통화중", "한 화면"],
    "오토콜":     ["자동 발신", "자동발신", "자동으로 전화", "자동으로 거는"],
    "스크린 팝업": ["고객 정보", "고객정보", "뜹니다", "띄웁니다", "뜨는 것", "먼저 뜹"],
    "옴니채널":   ["채널", "통합"],
}

WINDOW = 90   # 용어 앞뒤로 이만큼 안에 풀이가 있으면 통과


def text_of(html):
    """본문만 남긴다. 메뉴·푸터에 있는 용어는 풀이를 붙일 자리가 아니다."""
    s = html
    for pat in (r"<script[\s\S]*?</script>", r"<style[\s\S]*?</style>",
                r"<header[\s\S]*?</header>", r"<footer[\s\S]*?</footer>",
                r'<nav[\s\S]*?</nav>',
                r'<div class="drawer"[\s\S]*?<!-- 히어로 -->',
                r'<div class="drawer"[\s\S]*?</div>\s*</div>\s*</div>',
                r'<div class="fab">[\s\S]*?</div>'):
        s = re.sub(pat, " ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = s.replace("&nbsp;", " ").replace("&amp;", "&")
    return re.sub(r"\s+", " ", s)


def main():
    pages = []
    for dp, _, fns in os.walk(DIST):
        for fn in fns:
            if fn.endswith(".html") and "glossary" not in dp:  # 용어집은 풀이 그 자체
                pages.append(os.path.join(dp, fn))
    pages.sort()

    missing = defaultdict(list)   # 용어 → [페이지…]
    used = defaultdict(int)

    for p in pages:
        rel = os.path.relpath(p, DIST).replace(os.sep, "/")
        txt = text_of(open(p, encoding="utf-8").read())
        for term, hints in TERMS.items():
            i = txt.find(term)
            if i < 0:
                continue
            used[term] += 1
            near = txt[max(0, i - WINDOW): i + WINDOW + len(term)]
            if not any(h in near for h in hints):
                missing[term].append(rel)

    print(f"검사한 페이지 {len(pages)}개\n")
    print(f"{'용어':<14}{'쓰인 페이지':>10}{'풀이 없음':>10}")
    print("-" * 36)
    total = 0
    for term in TERMS:
        if not used[term]:
            continue
        m = len(missing[term])
        total += m
        mark = "  ←" if m else ""
        print(f"{term:<14}{used[term]:>10}{m:>10}{mark}")

    print("-" * 36)
    print(f"풀이가 빠진 자리 총 {total}곳\n")

    for term, pgs in missing.items():
        if not pgs:
            continue
        print(f"[{term}] {len(pgs)}곳")
        for x in pgs[:6]:
            print(f"    {x}")
        if len(pgs) > 6:
            print(f"    … 외 {len(pgs) - 6}개")
        print()

    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
