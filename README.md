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

## 지역 페이지 5만 장 (PHP)

`dist/_router.php` 파일 하나가 **53,238개 지역 페이지**를 만들어 냅니다.
HTML을 미리 뽑아 두지 않기 때문에 문구를 한 줄 고치면 5만 장에 바로 반영됩니다.

```
/local/                                   전국 허브             1
/local/{시도}/                             시도 허브            17
/local/{시도}/{시군구}/                     시군구 허브         229
/local/{시도}/{시군구}/{업종}/               시군구 × 업종     7,557
/local/{시도}/{시군구}/{읍면동}/             읍면동 허브       3,495
/local/{시도}/{시군구}/{읍면동}/{서비스}/     읍면동 × 서비스  41,940
/local/sitemap.xml                        사이트맵 목록
/local/sitemap-{시도}.xml                  시도별 사이트맵
```

**필요 환경** — PHP 7.4 이상, Apache mod_rewrite (`dist/.htaccess` 참고)
nginx면 `location /local/ { try_files $uri /_router.php; }` 한 줄이면 됩니다.

**로컬에서 확인**

```bash
php -S 127.0.0.1:8792 -t dist dist/_router.php
```

http://127.0.0.1:8792/local/seoul/gangnam/hospital/

**데이터**

| 파일 | 내용 |
|---|---|
| `_data/regions-index.json` | 시도·시군구 목록 (9KB, 매 요청 로드) |
| `_data/regions/{시도}.json` | 읍면동 포함 상세 (필요할 때만 로드) |
| `_data/topics.json` | 업종 33 · 서비스 12 |

지역 데이터는 `node _tools/extract_regions.mjs`, 주제는 `python _tools/gen_topics.py`로 다시 만듭니다.

> ⚠️ **GitHub Pages에서는 `/local/` 페이지가 뜨지 않습니다.** PHP를 실행하지 못하기 때문입니다.
> 미리보기에서는 정적 페이지 42장만 보입니다. 지역 페이지는 PHP가 되는 서버에 올려야 동작합니다.

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
