# -*- coding: utf-8 -*-
"""
관리자 화면 예시(mock) 조각 모음

이미지가 아니라 HTML입니다. 기능이 바뀌면 여기 문구만 고치면 전 페이지에 반영됩니다.
캡처를 쓰지 않는 이유는 세 가지입니다.
  - 화면이 바뀔 때마다 이미지를 다시 찍어야 합니다
  - 이미지 안의 글자는 검색엔진과 AI가 읽지 못합니다
  - 실제 고객 데이터가 찍힐 위험이 없습니다

스타일은 nova.css의 '화면 예시(mock)' 블록에 있습니다.
"""

CHECK = ('<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>')
PHONE = ('<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2'
         'A19.79 19.79 0 0 1 2.08 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11'
         'L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>')
PLAY = ('<svg width="11" height="11" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>')


def frame(title, right, body, note=None):
    n = f'<p class="mock-note">{note}</p>' if note else ""
    return f'''<div class="mock">
  <div class="mock-bar"><span class="dots"><i></i><i></i><i></i></span><b>{title}</b><span class="right">{right}</span></div>
  <div class="mock-body">{body}</div>
</div>{n}'''


# ---------------------------------------------------------------- 상담 화면

def consult():
    body = f'''
    <div class="mock-incoming">
      <span class="ic">{PHONE}</span>
      <div><b>010-2847-**** · 김○○ 님</b><small>세 번째 통화 · 마지막 상담 2026-08-02</small></div>
      <span class="mk talk" style="margin-left:auto">통화 중 00:42</span>
    </div>
    <div class="mock-split">
      <div class="mock-card">
        <h5>고객 정보</h5>
        <div class="mock-row"><span>등급</span><span>정기</span></div>
        <div class="mock-row"><span>가입일</span><span>2023-04-11</span></div>
        <div class="mock-row"><span>담당</span><span>2팀 이○○</span></div>
        <div class="mock-row"><span>누적 상담</span><span>3건</span></div>
        <div class="mock-row"><span>미처리</span><span>1건</span></div>
      </div>
      <div class="mock-card">
        <h5>상담 이력</h5>
        <div class="mock-log">
          <div><b>배송 지연 문의</b><p>도착 예정일 안내, 쿠폰 발송 처리</p><time>2026-08-02 · 박○○</time></div>
          <div><b>주소 변경 요청</b><p>배송지 수정 완료</p><time>2026-06-18 · 이○○</time></div>
          <div><b>가입 문의</b><p>요금제 안내</p><time>2023-04-11 · 김○○</time></div>
        </div>
      </div>
    </div>'''
    return frame("상담 화면", "전화가 울리는 순간", body,
                 "화면 예시입니다. 표시 항목은 업무에 맞게 추가하거나 뺄 수 있습니다.")


# ---------------------------------------------------------------- 녹취 검색

def recording():
    rows = [
        ("08-16 14:22", "수신", "010-2847-****", "이○○", "04:12", "done", "완료"),
        ("08-16 13:58", "발신", "02-512-****", "박○○", "01:35", "done", "완료"),
        ("08-16 13:40", "수신", "010-9931-****", "—", "00:00", "miss", "부재중"),
        ("08-16 11:07", "수신", "031-771-****", "김○○", "07:48", "done", "완료"),
    ]
    trs = "".join(
        f'<tr><td>{d}</td><td>{k}</td><td>{n}</td><td>{a}</td><td class="num">{t}</td>'
        f'<td><span class="mk {c}">{s}</span></td>'
        f'<td><span class="play">{PLAY}</span></td></tr>'
        for d, k, n, a, t, c, s in rows)
    body = f'''
    <div class="mock-filter">
      <span class="on">최근 7일</span><span>상담원 전체</span><span>수신·발신</span>
      <span>통화 상태</span><span>고객번호 검색</span>
    </div>
    <table>
      <thead><tr><th>일시</th><th>구분</th><th>고객번호</th><th>상담원</th><th>통화시간</th><th>상태</th><th>듣기</th></tr></thead>
      <tbody>{trs}</tbody>
    </table>'''
    return frame("통화 녹취", "기간·상담원·번호로 검색", body,
                 "화면 예시입니다. 부재중 통화도 목록에 남아 놓친 전화를 확인할 수 있습니다.")


# ---------------------------------------------------------------- 전광판

def dashboard():
    seats = [("이○○", "talk", "통화중"), ("박○○", "talk", "통화중"), ("김○○", "wait", "대기"),
             ("정○○", "wait", "대기"), ("최○○", "rest", "휴식"), ("한○○", "talk", "통화중"),
             ("오○○", "wait", "대기"), ("서○○", "talk", "통화중")]
    tiles = "".join(f'<div class="mock-seat"><b>{n}</b><span class="mk {c}">{s}</span></div>'
                    for n, c, s in seats)
    body = f'''
    <div class="mock-sum">
      <div><small>대기 중인 전화</small><b style="color:#a32020">2</b></div>
      <div><small>통화 중</small><b style="color:var(--mint-ink)">4</b></div>
      <div><small>대기 상담원</small><b>3</b></div>
      <div><small>오늘 받은 전화</small><b>218</b></div>
      <div><small>놓친 전화</small><b style="color:#a32020">6</b></div>
    </div>
    <div class="mock-seats">{tiles}</div>'''
    return frame("실시간 현황판", "지금 이 순간", body,
                 "화면 예시입니다. 대기 전화가 쌓이는 순간이 바로 보입니다.")


# ---------------------------------------------------------------- 통계

def stats():
    bars = [("월", 46, ""), ("화", 62, ""), ("수", 58, ""), ("목", 71, ""),
            ("금", 88, ""), ("토", 34, "alt"), ("일", 18, "alt")]
    b = "".join(f'<div><i class="{c}" style="height:{h}%"></i><small>{d}</small></div>'
                for d, h, c in bars)
    body = f'''
    <div class="mock-sum">
      <div><small>이번 주 통화</small><b>1,284</b></div>
      <div><small>평균 응답</small><b>8초</b></div>
      <div><small>첫 통화 종결</small><b>71%</b></div>
      <div><small>놓친 전화</small><b>3.2%</b></div>
    </div>
    <div class="mock-bars">{b}</div>'''
    return frame("통계", "요일별 통화량", body,
                 "화면 예시입니다. 수치는 예시이며 실제 값은 운영 데이터로 채워집니다.")


# ---------------------------------------------------------------- AI 통화요약

def ai_summary():
    body = '''
    <div class="mock-card" style="margin-bottom:12px">
      <div class="mock-row"><span>통화</span><span>2026-08-16 14:22 · 4분 12초</span></div>
      <div class="mock-row"><span>고객</span><span>010-2847-**** 김○○</span></div>
      <div class="mock-row"><span>상담원</span><span>2팀 이○○</span></div>
    </div>
    <h5 style="font-size:12px;font-weight:800;color:var(--slate-500);margin-bottom:8px">요약</h5>
    <div class="mock-quote">
      주문한 상품의 배송이 예정일보다 늦어진 건으로 문의.
      현재 배송 단계와 도착 예정일을 안내하고, 지연에 대한 쿠폰 발송을 약속함.
      고객은 안내 내용에 동의했으며 추가 요청 사항 없음.
    </div>
    <div class="mock-tags">
      <span>배송 지연</span><span>도착일 안내</span><span>쿠폰 발송</span><span>처리 완료</span>
    </div>'''
    return frame("AI 통화요약", "통화가 끝나면 자동으로", body,
                 "화면 예시입니다. 요약과 분류는 통화가 끝나는 즉시 생성됩니다.")


# ---------------------------------------------------------------- ARS 시나리오

def ivr_tree():
    body = '''
    <div class="mock-filter"><span class="on">평일 09:00–18:00</span><span>점심시간</span><span>야간·주말</span><span>공휴일</span></div>
    <table>
      <thead><tr><th>단계</th><th>안내 내용</th><th>누르면</th></tr></thead>
      <tbody>
        <tr><td class="num">시작</td><td>안녕하세요, ○○입니다. 무엇을 도와드릴까요?</td><td>—</td></tr>
        <tr><td class="num">1</td><td>주문·배송 문의</td><td>조회 후 자동 안내</td></tr>
        <tr><td class="num">2</td><td>교환·반품 접수</td><td>접수 후 담당 배정</td></tr>
        <tr><td class="num">3</td><td>영업시간·오시는 길</td><td>안내 후 종료</td></tr>
        <tr><td class="num">0</td><td>상담원 연결</td><td>대기열 배정</td></tr>
      </tbody>
    </table>'''
    return frame("ARS 시나리오", "시간대별로 다르게", body,
                 "화면 예시입니다. 안내 문구는 관리자 화면에서 직접 수정하면 음성으로 만들어 적용됩니다.")


ALL = {
    "consult": ("상담 화면", "전화가 울리는 순간 고객이 먼저 뜹니다", consult),
    "recording": ("통화 녹취", "필요한 통화를 조건으로 찾습니다", recording),
    "dashboard": ("실시간 현황판", "지금 몇 통이 대기 중인지 보입니다", dashboard),
    "stats": ("통계", "무엇을 줄일지 정하려면 먼저 봐야 합니다", stats),
    "ai_summary": ("AI 통화요약", "통화를 다시 듣지 않아도 됩니다", ai_summary),
    "ivr_tree": ("ARS 시나리오", "시간대에 따라 다른 안내가 나갑니다", ivr_tree),
}
