# -*- coding: utf-8 -*-
"""
비트웨이브 나머지 페이지 생성기 (솔루션 외)
  python _tools/gen_pages.py

  활용사례 허브 + 7  /  업종별 허브 + 11  /  요금 · 구축사례 · 회사소개 · 상담문의

머리말·꼬리말·상대경로 처리는 gen_solution.py 것을 그대로 가져다 씀.
내용 수정은 아래 데이터 목록만 고치면 됨.
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_solution import (head, header, FOOTER, write, e, SITE, TEL, TEL_RAW)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DIST = os.path.join(ROOT, "dist")

# ---------------------------------------------------------------- 활용사례

USE_CASES = [
 dict(slug="support", nav="고객 응대",
  h1="반복 문의를<br>첫 통화에서 끝냅니다",
  sub="같은 질문에 같은 답을 하루에 수십 번 하고 있다면, 그 시간은 다른 곳에 써야 합니다.",
  aq="고객 응대를 자동화하면 서비스가 나빠지지 않나요?",
  a="나빠지는 쪽은 <b>대기</b>입니다. 답이 정해진 문의까지 사람이 받으면 정작 설명이 필요한 고객이 기다립니다. "
    "<span class='hl'>정해진 답이 있는 문의는 즉시 처리하고, 판단이 필요한 통화는 사람에게 넘기는</span> 구조가 양쪽 다 낫습니다.",
  points=[("첫 통화 종결","묻고 답하고 끝냅니다. 다시 걸 일이 줄어듭니다."),
          ("대기 이탈 감소","기다리다 끊는 고객이 사라집니다."),
          ("야간·휴일 유지","시간대와 상관없이 같은 안내가 나갑니다.")],
  flows=[("발화로 의도 파악","무엇 때문에 걸었는지 첫 마디에서 잡습니다."),
         ("자료 기반 응답","등록된 안내와 정책에서 근거를 찾아 답합니다."),
         ("처리·접수","단순 변경과 접수는 통화 안에서 끝냅니다."),
         ("상담원 인계","넘길 때 대화 요약을 함께 전달합니다.")],
  faq=[("어떤 문의부터 넣나요?","가장 자주 오면서 답이 고정된 것부터 넣습니다."),
       ("답을 못 하면요?","상담원에게 넘어갑니다. 고객이 설명을 반복하지 않게 요약이 같이 갑니다."),
       ("안내 내용을 바꾸려면요?","등록된 자료를 수정하면 그다음 통화부터 반영됩니다.")]),

 dict(slug="booking", nav="예약·접수",
  h1="예약 변경 전화를<br>사람이 받지 않아도 됩니다",
  sub="예약 확인, 변경, 취소는 통화 내용이 거의 정해져 있습니다.",
  aq="예약 전화는 어떤 점이 자동화하기 좋은가요?",
  a="예약 통화는 <span class='hl'>물어볼 것과 확인할 것이 정해져 있습니다</span>. 누구인지 확인하고, 언제로 옮길지 듣고, 가능한 시간을 알려주면 끝납니다. "
    "여기에 방문 전 확인 전화까지 붙이면 빈자리가 줄어듭니다.",
  points=[("빈자리 감소","오기로 한 사람이 안 오는 일이 줄어듭니다."),
          ("접수 누락 방지","업무 외 시간 예약도 받아 둡니다."),
          ("변경 처리 자동화","일정 조정을 통화 안에서 끝냅니다.")],
  flows=[("본인 확인","이름과 연락처로 예약 건을 찾습니다."),
         ("가능 시간 안내","비어 있는 시간을 알려주고 고릅니다."),
         ("확정 안내 발송","정해진 일정을 문자로 보냅니다."),
         ("방문 전 확인","하루 이틀 전에 다시 걸어 확인합니다.")],
  faq=[("기존 예약 시스템과 연결되나요?","연동 방식은 쓰시는 시스템을 보고 정합니다."),
       ("취소도 받을 수 있나요?","취소와 변경 모두 통화 안에서 처리합니다."),
       ("확정 문자는 자동인가요?","통화가 끝나면 바로 나갑니다.")]),

 dict(slug="routing", nav="대표번호 안내",
  h1="번호를 누르지 않고도<br>맞는 곳으로 갑니다",
  sub="1번 누르고 다시 2번 누르는 안내를 끝까지 듣는 고객은 많지 않습니다.",
  aq="기존 ARS와 무엇이 다른가요?",
  a="기존 ARS는 <b>메뉴를 순서대로 눌러야</b> 원하는 곳에 도착합니다. 단계가 깊어질수록 중간에 끊는 사람이 늘어납니다. "
    "<span class='hl'>말한 내용으로 바로 분기하면</span> 메뉴 트리를 지나갈 필요가 없습니다.",
  points=[("대기 없는 첫 응답","울리자마자 받습니다."),
          ("정확한 이관","부서·지점·긴급도를 판단해 넘깁니다."),
          ("단순 문의 종결","위치와 영업시간은 그 자리에서 끝냅니다.")],
  flows=[("첫 마디로 분류","무엇 때문에 걸었는지 듣고 나눕니다."),
         ("지점·부서 분기","조건과 일정에 따라 갈라집니다."),
         ("자료 기반 안내","반복 문의는 연결 없이 답합니다."),
         ("요약과 함께 이관","넘길 때 지금까지의 내용을 붙입니다.")],
  faq=[("쓰던 대표번호를 그대로 쓰나요?","번호를 바꾸지 않고 적용합니다."),
       ("기존 ARS와 같이 쓸 수 있나요?","일부 구간만 바꾸는 방식도 가능합니다."),
       ("긴급 전화는 어떻게 하나요?","조건을 정해 바로 담당자로 넘깁니다.")]),

 dict(slug="outbound", nav="아웃바운드 영업",
  h1="사람이 못 거는 양까지<br>걸어 봅니다",
  sub="명단은 있는데 걸 사람이 없어서 못 돌리는 경우가 많습니다.",
  aq="자동 발신이 영업에 실제로 도움이 되나요?",
  a="도움이 되는 지점은 <span class='hl'>거르는 단계</span>입니다. 수백 통을 돌려 관심 있는 곳만 남기면, 영업 담당자는 그 명단부터 시작합니다. "
    "관심 없는 통화에 쓰던 시간이 빠집니다.",
  points=[("도달량 확보","같은 톤으로 정해진 양을 채웁니다."),
          ("관심 고객 선별","반응이 있는 곳만 남깁니다."),
          ("기록 자동화","통화 결과가 CRM에 바로 쌓입니다.")],
  flows=[("명단 업로드","보유한 목록을 올립니다."),
         ("대량 발신","예약 발송과 자동 재발신을 씁니다."),
         ("관심 확인","조건을 물어 자격을 나눕니다."),
         ("담당자 연결","가능성 있는 건만 사람에게 넘깁니다.")],
  faq=[("발신 시간 규정은 지켜지나요?","발신 가능 시간대와 수신 거부 처리를 설정에 넣습니다."),
       ("스크립트는 누가 만드나요?","기존에 쓰시던 내용을 바탕으로 함께 정리합니다."),
       ("결과를 어디서 보나요?","통화별 결과와 녹취를 관리자 화면에서 봅니다.")]),

 dict(slug="reminder", nav="리마인드·해피콜",
  h1="잊지 않게,<br>빠뜨리지 않게",
  sub="방문 전 확인과 사후 만족도 조사는 미루면 안 하게 됩니다.",
  aq="리마인드 전화를 꼭 사람이 해야 하나요?",
  a="확인 전화는 <span class='hl'>내용이 거의 같고 양이 많습니다</span>. 사람이 하면 바쁠 때 가장 먼저 밀립니다. "
    "자동으로 돌리면 밀리지 않고, 응답 결과만 정리해서 봅니다.",
  points=[("노쇼 감소","오기 전에 한 번 더 확인합니다."),
          ("사후 관리 유지","바빠도 빠뜨리지 않습니다."),
          ("응답 자동 정리","결과가 이력에 바로 남습니다.")],
  flows=[("대상 추출","날짜와 조건으로 명단을 뽑습니다."),
         ("자동 발신","정해진 시간에 겁니다."),
         ("응답 수집","확인·변경·취소를 통화에서 받습니다."),
         ("결과 반영","일정과 이력에 반영합니다.")],
  faq=[("몇 번까지 다시 거나요?","재발신 횟수와 간격을 정해둡니다."),
       ("문자로도 보낼 수 있나요?","통화와 문자를 함께 씁니다."),
       ("불만이 나오면요?","상담원에게 바로 넘깁니다.")]),

 dict(slug="overdue", nav="미납 안내",
  h1="정해진 기준 안에서<br>차분하게 안내합니다",
  sub="미납 안내는 무엇을 말하고 무엇을 말하지 않을지가 중요합니다.",
  aq="미납 안내를 자동으로 해도 되나요?",
  a="규정을 지키는 것이 전제입니다. <span class='hl'>발신 가능 시간, 금지 표현, 수신 거부 처리</span>를 설정에 넣어두면 통화마다 같은 기준이 적용됩니다. "
    "사람마다 말이 달라지는 문제가 줄어듭니다.",
  points=[("일관된 안내","누가 받아도 같은 내용이 전달됩니다."),
          ("약속 기록","납부 예정일과 금액을 남깁니다."),
          ("규정 준수","시간과 표현을 기준 안에서 관리합니다.")],
  flows=[("본인 확인","정해진 절차로 확인합니다."),
         ("금액·기한 안내","미납 내용과 납부 방법을 전달합니다."),
         ("납부 약속 접수","예정일과 방식을 받습니다."),
         ("이의 제기 이관","항의나 분쟁은 사람에게 넘깁니다.")],
  faq=[("이미 납부한 분에게 또 걸지 않나요?","납부 확인 결과를 반영해 대상에서 뺍니다."),
       ("녹취는 남나요?","전 통화를 남기고 조건으로 찾습니다."),
       ("수신 거부는요?","거부 의사를 받으면 다음 발신에서 제외합니다.")]),

 dict(slug="survey", nav="설문조사",
  h1="문자로는 답하지 않는 분들께<br>전화로 묻습니다",
  sub="응답률이 낮으면 결과를 믿기 어렵습니다.",
  aq="전화 설문이 문자 설문보다 나은가요?",
  a="대상에 따라 다릅니다. <span class='hl'>문자에 응답하지 않는 층</span>, 특히 연령대가 높은 표본은 통화 응답률이 훨씬 높습니다. "
    "점수와 자유응답을 함께 받아 바로 정리된 형태로 쌓습니다.",
  points=[("응답률 확보","닿기 어려운 표본까지 접근합니다."),
          ("건당 비용 절감","동시에 여러 건을 돌립니다."),
          ("즉시 집계","응답이 들어오는 대로 쌓입니다.")],
  flows=[("문항 구성","질문 순서와 조건 분기를 정합니다."),
         ("자동 발신","대상 명단으로 동시에 겁니다."),
         ("응답 수집","점수와 자유응답을 함께 받습니다."),
         ("결과 정리","항목별로 집계해 내려받습니다.")],
  faq=[("자유응답도 되나요?","말한 내용을 글로 정리해 남깁니다."),
       ("개인정보 동의는요?","안내와 동의 절차를 문항에 넣습니다."),
       ("결과를 외부로 보낼 수 있나요?","파일로 내려받거나 시스템으로 넘깁니다.")]),
]

# ---------------------------------------------------------------- 업종별

INDUSTRIES = [
 ("hospital","병원·의원","예약 전화가 진료를 방해하지 않게",
  "접수 직원이 전화를 받느라 앞에 선 환자를 기다리게 하는 상황이 반복됩니다.",
  ["예약·변경 자동 접수","진료시간·위치 안내 자동화","방문 전 확인 전화"]),
 ("public","공공·기관","민원 전화가 몰려도 대기가 없게",
  "특정 기간에 민원이 폭증하고, 담당자 개인번호가 노출되는 문제가 함께 옵니다.",
  ["민원 유형 자동 분류","담당 부서 자동 연결","개인번호 비노출 통화"]),
 ("finance","금융·보험","녹취와 본인확인을 규정대로",
  "통화 내용을 남겨야 하고, 누가 언제 무엇을 안내했는지 확인할 수 있어야 합니다.",
  ["전 통화 녹취·조건 검색","본인확인 절차 표준화","보관 위치·기간 선택"]),
 ("education","교육·학원","상담 전화를 놓치지 않게",
  "상담 문의는 저녁과 주말에 몰리는데, 그 시간에 받을 사람이 없습니다.",
  ["업무 외 시간 상담 접수","안심번호로 교사 번호 보호","등록 상담 이력 관리"]),
 ("shop","쇼핑몰","전화·채팅 문의를 한 화면에서",
  "주문, 배송, 교환 문의가 전화와 메신저로 동시에 들어옵니다.",
  ["채널 통합 상담","주문 조회 자동 응답","반복 문의 자동 처리"]),
 ("manufacturing","제조업","거래처 통화를 회사 자산으로",
  "담당자 개인 휴대폰에만 이력이 남아, 자리를 비우면 아무도 답을 못 합니다.",
  ["거래처별 통화 이력","담당자 부재 시 인수인계","견적·발주 문의 기록"]),
 ("distribution","유통·물류","배송 문의를 자동으로 걸러",
  "같은 배송 조회 문의가 하루 종일 반복됩니다.",
  ["배송 조회 자동 안내","클레임 접수 분류","대량 안내 발송"]),
 ("law","법무·세무","놓친 전화가 곧 놓친 사건",
  "상담 중에는 전화를 받을 수 없고, 부재중 전화는 다시 걸어오지 않습니다.",
  ["부재중 콜백 접수","상담 예약 자동 안내","통화 내용 기록"]),
 ("counseling","심리상담","상담사 번호를 보호하면서",
  "개인 번호로 연락이 이어지면 상담사가 소진됩니다.",
  ["안심번호 통화","상담 시간 외 자동 안내","이력 접근 권한 관리"]),
 ("sales","분양·영업","걸어야 할 곳이 많을 때",
  "명단은 큰데 상담 인력은 한정돼 있습니다.",
  ["대량 발신·재발신","관심 고객 선별","상담원별 실적 통계"]),
 ("rental","렌탈·구독","정기 안내를 빠뜨리지 않게",
  "만기, 점검, 수납 안내가 매달 반복됩니다.",
  ["정기 안내 자동 발신","납부 안내 표준화","해지 방어 상담 연결"]),
]

# ---------------------------------------------------------------- 템플릿 조각

def hero(eyebrow, h1, sub, crumb):
    return f'''
<div class="hero-top">
  <div class="wrap">
    <p style="font-size:13px;color:var(--slate-400);text-align:center">{crumb}</p>
    <div class="hero-center">
      <span class="eyebrow">{eyebrow}</span>
      <h1 style="margin-top:16px">{h1}</h1>
      <p class="sub">{sub}</p>
      <div class="actions">
        <a href="/#lead" class="btn btn-brand">무료 상담 신청</a>
        <a href="tel:{TEL_RAW}" class="btn btn-outline">{TEL}</a>
      </div>
    </div>
  </div>
</div>'''


def answer_box(q, a):
    return f'''
<section style="padding:56px 0 0">
  <div class="wrap"><div class="answer"><span class="lab">{e(q)}</span><p>{a}</p></div></div>
</section>'''


def sec(eyebrow, title, inner, bg=False, narrow=False):
    style = ' style="background:var(--slate-50)"' if bg else ""
    w = "wrap-narrow" if narrow else "wrap"
    return f'''
<section{style}>
  <div class="{w}">
    <div class="sec-head"><span class="eyebrow">{eyebrow}</span><h2 class="h">{title}</h2></div>
    {inner}
  </div>
</section>'''


def faq_block(items):
    ds = "".join(f'<details><summary>{e(q)}</summary><div class="a">{e(a)}</div></details>'
                 for q, a in items)
    return sec("FAQ", "자주 묻는 것",
               f'<div class="faq" style="max-width:720px;margin:0 auto">{ds}</div>', narrow=True)


# ---------------------------------------------------------------- 렌더

def render_usecase(u, others):
    pts = "".join(f'<div class="card"><h3>{e(t)}</h3><p class="cd">{e(d)}</p></div>' for t, d in u["points"])
    fls = "".join(f'<div class="step"><span class="sn wn c{i}">{i+1}</span><div><h4>{e(t)}</h4><p>{e(d)}</p></div></div>'
                  for i, (t, d) in enumerate(u["flows"]))
    rel = "".join(f'<a href="/use-cases/{o["slug"]}/" class="ind"><h4>{o["nav"]}</h4></a>' for o in others)
    return (head(f'{u["nav"]} AI 자동화 | 비트웨이브', u["sub"], f'{SITE}/use-cases/{u["slug"]}/', u["faq"])
      + header()
      + hero("Use case", u["h1"], u["sub"],
             '<a href="/">홈</a> · <a href="/use-cases/">활용사례</a> · ' + e(u["nav"]))
      + answer_box(u["aq"], u["a"])
      + sec("Outcomes", "무엇이 달라지나요", f'<div class="cards3">{pts}</div>')
      + sec("Workflow", "통화는 이렇게 흘러갑니다", f'<div class="steps">{fls}</div>', bg=True)
      + faq_block(u["faq"])
      + sec("More", "다른 활용사례", f'<div class="ind-grid">{rel}</div>', bg=True)
      + FOOTER)


def render_industry(ind, others):
    slug, nav, h1, sub, feats = ind
    cards = "".join(f'<div class="card"><h3>{e(f)}</h3></div>' for f in feats)
    rel = "".join(f'<a href="/industries/{o[0]}/" class="ind"><h4>{o[1]}</h4></a>' for o in others)
    faq = [("도입까지 얼마나 걸리나요?", "규모와 구성에 따라 다릅니다. 현황을 본 뒤 일정을 알려드립니다."),
           ("쓰던 번호를 그대로 쓸 수 있나요?", "번호 이전으로 유지할 수 있습니다."),
           ("작은 규모도 되나요?", "몇 석 규모부터 구성합니다.")]
    return (head(f'{nav} 콜센터·고객관리 구축 | 비트웨이브', sub, f'{SITE}/industries/{slug}/', faq)
      + header()
      + hero("Industry", h1, sub, '<a href="/">홈</a> · <a href="/industries/">업종별</a> · ' + e(nav))
      + answer_box(f"{nav}은 무엇이 다른가요?",
          f"업종마다 전화로 오는 내용이 다릅니다. {e(nav)}에서 자주 나오는 것은 아래 세 가지입니다. "
          f"비트웨이브는 <span class='hl'>이 업종에서 반복해서 나온 요구를 기본 구성으로</span> 잡아두고 시작합니다.")
      + sec("Setup", "이 업종의 기본 구성", f'<div class="cards3">{cards}</div>')
      + faq_block(faq)
      + sec("More", "다른 업종", f'<div class="ind-grid">{rel}</div>', bg=True)
      + FOOTER)


def hub(eyebrow, h1, sub, cards, canonical, title, desc):
    return (head(title, desc, canonical) + header()
      + hero(eyebrow, h1, sub, '<a href="/">홈</a> · ' + e(h1.replace("<br>", " ")))
      + f'<section style="padding:56px 0 76px"><div class="wrap"><div class="cards2">{cards}</div></div></section>'
      + FOOTER)


# ---------------------------------------------------------------- 단독 페이지

def page_pricing():
    body = '''
<div class="table-scroll">
  <table class="t">
    <thead><tr><th>항목</th><th>내용</th><th>과금</th></tr></thead>
    <tbody>
      <tr><th>시스템 구축</th><td class="typ">IP 교환기 · 상담 프로그램 · 설치 · 교육</td><td class="price">1회</td></tr>
      <tr><th>회선 이용료</th><td class="typ">인터넷전화 회선, 대표번호, 통화료</td><td class="price">월</td></tr>
      <tr><th>유지보수</th><td class="typ">장애 대응, 기능 수정, 정기 점검</td><td class="price">별도 계약</td></tr>
      <tr><th>부가서비스</th><td class="typ">문자, 팩스, 영상상담 등 선택 항목</td><td class="price">선택</td></tr>
    </tbody>
  </table>
</div>
<p class="note">※ 금액은 상담 후 견적으로 안내해 드립니다. 쓰지 않는 기능은 빼고 산정합니다.</p>'''
    faq = [("금액이 왜 공개되어 있지 않나요?", "상담 인원, 회선 수, 필요한 기능에 따라 차이가 커서 일률적인 표로는 오히려 잘못된 기대를 만듭니다."),
           ("상담 프로그램은 따로 사야 하나요?", "CRM·녹취·통계는 시스템 구축에 함께 들어갑니다. 프로그램만 따로 구매하는 항목이 없습니다."),
           ("나중에 기능을 추가하면 다시 구축해야 하나요?", "같은 시스템 안에서 기능을 켜는 방식이라 재구축은 없습니다.")]
    return (head("요금 구조 | 콜센터 구축 비용 | 비트웨이브",
                 "콜센터 구축 비용이 어떤 항목으로 구성되는지 정리했습니다. 시스템 구축, 회선 이용료, 유지보수, 부가서비스.",
                 f"{SITE}/pricing/", faq)
      + header()
      + hero("Pricing", "비용은 이렇게<br>구성됩니다",
             "규모와 구성에 따라 달라지지만, 항목 자체는 단순합니다.", '<a href="/">홈</a> · 요금')
      + sec("Structure", "네 가지 항목", body, narrow=True)
      + faq_block(faq) + FOOTER)


def page_cases():
    body = '''
<div class="table-scroll">
  <table class="t">
    <thead><tr><th>업종</th><th>규모</th><th>도입 구성</th><th>해결한 문제</th></tr></thead>
    <tbody>
      <tr><th>제조</th><td>상담 <span class="gb">20</span>석</td><td class="typ">IP교환기 · CRM · 녹취</td><td class="typ">거래처 통화 이력이 담당자 개인 휴대폰에만 남던 문제</td></tr>
      <tr><th>공공</th><td>상담 <span class="gb">35</span>석</td><td class="typ">IPCC · IVR · 전수녹취</td><td class="typ">민원 폭주 시간대 대기 이탈과 담당자 개인번호 노출</td></tr>
      <tr><th>쇼핑몰</th><td>상담 <span class="gb">12</span>석</td><td class="typ">CRM · 채팅상담 · 문자</td><td class="typ">전화·카카오·문자 문의가 서로 다른 창에 흩어지던 문제</td></tr>
      <tr><th>금융</th><td>상담 <span class="gb">60</span>석</td><td class="typ">IPCC · 스킬 호분배 · 통계</td><td class="typ">상담원별 편차와 녹취 보관 규정 대응</td></tr>
    </tbody>
  </table>
</div>
<p class="note">※ 고객사 요청에 따라 사명은 표기하지 않습니다. 위 내용은 실제 사례로 교체 예정입니다.</p>'''
    return (head("구축 사례 | 50개 기업의 컨택센터 | 비트웨이브",
                 "2006년부터 50개 기업의 컨택센터를 구축했습니다. 업종과 규모, 도입 구성으로 정리했습니다.",
                 f"{SITE}/cases/")
      + header()
      + hero("Cases", "50개 기업이<br>이렇게 쓰고 있습니다",
             "고객사 요청에 따라 사명은 표기하지 않습니다.<br>대신 업종과 규모, 무엇을 해결했는지를 적었습니다.",
             '<a href="/">홈</a> · 구축사례')
      + sec("Records", "업종별 구축 내역", body) + FOOTER)


def page_about():
    body = '''
<div class="table-scroll">
  <table class="t">
    <thead><tr><th>구분</th><th>내용</th></tr></thead>
    <tbody>
      <tr><th>개발법인</th><td class="typ">㈜지오테스솔루션 (2008년 9월 10일)</td></tr>
      <tr><th>판매법인</th><td class="typ">㈜비트웨이브 (2015년 1월 1일)</td></tr>
      <tr><th>사업 시작</th><td class="typ">2006년</td></tr>
      <tr><th>대표이사</th><td class="typ">신명남</td></tr>
      <tr><th>사업자등록번호</th><td class="typ">144-81-03835</td></tr>
      <tr><th>주소</th><td class="typ">경기 고양시 덕양구 삼막3길 5 고양삼송듀클래스 904호</td></tr>
    </tbody>
  </table>
</div>'''
    biz = '''<div class="cards3">
      <div class="card"><h3>인터넷전화(VoIP)</h3><p class="cd">기업 대상 인터넷전화 서비스와 VPN.</p></div>
      <div class="card"><h3>IP-PBX · IP-IVR</h3><p class="cd">대형 서버형과 중소형 임베디드 교환기 개발.</p></div>
      <div class="card"><h3>통합 IPCC</h3><p class="cd">콜센터 솔루션 구축과 호스팅·임대 서비스.</p></div>
      <div class="card"><h3>콜센터 애플리케이션</h3><p class="cd">CRM, 녹취, 통계 등 상담 프로그램 개발.</p></div>
      <div class="card"><h3>Centrex Switch</h3><p class="cd">통신사업자용 VoIP 및 SIP Proxy 시스템.</p></div>
      <div class="card"><h3>온라인 마케팅</h3><p class="cd">마케팅 프로그램 개발과 대행.</p></div>
    </div>'''
    return (head("회사소개 | ㈜지오테스솔루션 · 비트웨이브",
                 "2006년부터 인터넷전화와 컨택센터 솔루션을 직접 개발해 온 ㈜지오테스솔루션의 회사 정보입니다.",
                 f"{SITE}/about/")
      + header()
      + hero("About", "2006년부터<br>이 일만 했습니다",
             "회선을 공급하면서 교환기와 상담 프로그램까지 직접 만드는 곳은 많지 않습니다.",
             '<a href="/">홈</a> · 회사소개')
      + sec("Business", "하는 일", biz)
      + sec("Company", "회사 정보", body, bg=True, narrow=True) + FOOTER)


def page_contact():
    form = '''
<div class="lead-wrap">
  <form class="lead" onsubmit="return false">
    <h3>무료 상담 신청</h3>
    <p class="ls">평일 09:00 – 18:00 · ''' + TEL + '''</p>
    <label for="c-company">회사명</label><input type="text" id="c-company" required>
    <label for="c-name">담당자</label><input type="text" id="c-name" required>
    <label for="c-tel">연락처</label><input type="tel" id="c-tel" required>
    <label for="c-size">상담 인원</label>
    <select id="c-size"><option>5석 이하</option><option>6 – 20석</option><option>21 – 50석</option><option>51석 이상</option><option>아직 모르겠습니다</option></select>
    <label for="c-memo">문의 내용</label><textarea id="c-memo"></textarea>
    <div class="agree"><input type="checkbox" id="c-agree" required>
      <label for="c-agree" style="margin:0;font-weight:500">상담을 위한 개인정보 수집·이용에 동의합니다</label></div>
    <button type="submit" class="btn btn-brand">상담 신청하기</button>
  </form>
</div>
<p class="note" style="text-align:center">※ 폼 전송 기능은 서버 연결 후 동작합니다.</p>'''
    info = '''<div class="cards3">
      <div class="card"><h3>고객센터</h3><p class="cd">''' + TEL + '''<br>평일 09:00 – 18:00</p></div>
      <div class="card"><h3>영업 문의</h3><p class="cd">070-7615-0119<br>02-6974-0888</p></div>
      <div class="card"><h3>기술 지원</h3><p class="cd">070-7615-0927<br>help@ziotes.com</p></div>
    </div>'''
    return (head("상담 문의 | 비트웨이브",
                 "콜센터 구축 상담은 무료입니다. 현황을 보고 필요한 구성만 담아 제안해 드립니다.",
                 f"{SITE}/contact/")
      + header()
      + hero("Contact", "무엇이 불편하신지만<br>알려주세요",
             "현황을 먼저 보고 필요한 구성만 담아 제안해 드립니다. 상담은 무료입니다.",
             '<a href="/">홈</a> · 상담문의')
      + sec("Channels", "연락처", info)
      + sec("Form", "상담 신청", form, bg=True, narrow=True) + FOOTER)


# ---------------------------------------------------------------- 실행

def main():
    print("나머지 페이지 생성")

    uc_cards = "".join(
      f'<a href="/use-cases/{u["slug"]}/" class="card" style="display:block">'
      f'<span class="svc-tag">Use case</span><h3>{u["nav"]}</h3>'
      f'<p class="cd">{e(u["sub"])}</p></a>' for u in USE_CASES)
    write(os.path.join(DIST, "use-cases", "index.html"),
          hub("Use cases", "어떤 전화 업무를<br>맡기시겠습니까",
              "걸려오는 전화부터 걸어야 하는 전화까지.", uc_cards,
              f"{SITE}/use-cases/", "활용사례 | 전화 업무 자동화 | 비트웨이브",
              "고객 응대, 예약·접수, 대표번호 안내, 아웃바운드 영업, 리마인드, 미납 안내, 설문조사."), 1)
    for u in USE_CASES:
        others = [o for o in USE_CASES if o["slug"] != u["slug"]][:4]
        write(os.path.join(DIST, "use-cases", u["slug"], "index.html"), render_usecase(u, others), 2)

    ind_cards = "".join(
      f'<a href="/industries/{i[0]}/" class="card" style="display:block">'
      f'<span class="svc-tag">Industry</span><h3>{i[1]}</h3>'
      f'<p class="cd">{e(i[3])}</p></a>' for i in INDUSTRIES)
    write(os.path.join(DIST, "industries", "index.html"),
          hub("Industries", "업종마다<br>필요한 것이 다릅니다",
              "50개 기업을 구축하며 쌓인 업종별 기본 구성이 있습니다.", ind_cards,
              f"{SITE}/industries/", "업종별 콜센터 구축 | 비트웨이브",
              "병원, 공공, 금융, 교육, 쇼핑몰, 제조, 유통, 법무, 심리상담, 분양, 렌탈."), 1)
    for i in INDUSTRIES:
        others = [o for o in INDUSTRIES if o[0] != i[0]][:4]
        write(os.path.join(DIST, "industries", i[0], "index.html"), render_industry(i, others), 2)

    write(os.path.join(DIST, "pricing", "index.html"), page_pricing(), 1)
    write(os.path.join(DIST, "cases", "index.html"), page_cases(), 1)
    write(os.path.join(DIST, "about", "index.html"), page_about(), 1)
    write(os.path.join(DIST, "contact", "index.html"), page_contact(), 1)

    total = 2 + len(USE_CASES) + len(INDUSTRIES) + 4
    print(f"\n총 {total}개 생성 완료")


if __name__ == "__main__":
    main()
