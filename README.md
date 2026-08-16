# 지오테스 홈페이지

㈜지오테스솔루션 / 지오테스 컨택센터 솔루션 사이트.

정적 HTML + CSS만 씁니다. 빌드 도구도, 프레임워크도, 의존성 설치도 없습니다.
페이지는 Python 스크립트로 생성합니다.

---

## 폴더

```
dist/                    배포되는 것 전부
  index.html             홈
  assets/nova.css        랜딩형 스타일 (홈·솔루션·업종)
  assets/nova-post.css   문서형 스타일 (정보글·지역 페이지)
  solution/              솔루션 상세 8 + 허브 (자동 생성)
_tools/
  gen_solution.py        솔루션 페이지 생성기
_notes/                  기획 문서 (배포 대상 아님)
```

## 페이지 다시 만들기

```bash
python _tools/gen_solution.py
```

내용을 고칠 때는 `_tools/gen_solution.py` 안의 `PAGES` 목록만 수정하면 됩니다.
HTML을 직접 손대지 마세요. 다시 생성하면 덮어써집니다.

## 로컬에서 보기

```bash
python -m http.server 8791 --directory dist
```

http://localhost:8791

---

## 배포

`dist/` 폴더를 그대로 올리면 됩니다.

**Cloudflare Pages** — 빌드 명령 없음, 출력 디렉터리 `dist`
**GitHub Pages** — 저장소 설정에서 Pages 소스를 지정
  ※ `username.github.io/저장소이름/` 형태로 배포하면 `/assets/...` 같은
     절대 경로가 깨집니다. 커스텀 도메인을 붙이거나 Cloudflare Pages를 쓰세요.

---

## 디자인

퍼플/그린 Nova. 색·간격·컴포넌트 규칙은 `_notes/디자인시스템.md`에 있습니다.

- 브랜드 `#6d4aff` / 포인트 `#35e0a1` `#ffd53e`
- 본문 Pretendard, 숫자·영문 Poppins
- UI에 이모지를 쓰지 않습니다. 아이콘은 인라인 SVG
- 새 콜아웃·인용박스를 만들지 않습니다. 있는 서식만 씁니다

## 아직 확정되지 않은 것

요금, 무상 지원 범위, AI 기능 판매 범위, 보유 인증, 고객사 표기 방식이
확정 전입니다. 해당 자리는 구조만 잡아두었고 `_notes/사장님_확인요청.md`에
질문을 정리해 두었습니다.
