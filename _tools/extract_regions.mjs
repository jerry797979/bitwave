// 전국콜비즈 지역 데이터를 지오테스용 JSON으로 변환
//   node _tools/extract_regions.mjs
// → dist/_data/regions.json
//
// 콜비즈에서 가져오는 것은 행정구역 목록뿐입니다. 키워드·본문은 가져오지 않습니다.
// (두 사이트가 같은 키워드를 노리면 서로 순위를 깎아먹기 때문)

import { PROVINCES } from "file:///C:/Users/marke/Desktop/callbiz/_local/engine.mjs";
import { DONGS } from "file:///C:/Users/marke/Desktop/callbiz/_local/dongs.mjs";
import { writeFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const OUT = join(ROOT, "dist", "_data");

const provinces = PROVINCES.map(([slug, ko, cities]) => ({
  slug,
  ko,
  cities: cities.map(([cslug, cko]) => ({
    slug: cslug,
    ko: cko,
    dongs: (DONGS[`${slug}/${cslug}`] || []).map(([dslug, dko]) => ({ slug: dslug, ko: dko })),
  })),
}));

let nCity = 0, nDong = 0;
for (const p of provinces) {
  nCity += p.cities.length;
  for (const c of p.cities) nDong += c.dongs.length;
}

mkdirSync(OUT, { recursive: true });
mkdirSync(join(OUT, "regions"), { recursive: true });

// 통짜 파일 하나를 매 요청마다 읽으면 느립니다(150KB).
// 시도별로 쪼개서 필요한 것만 읽게 합니다.
for (const p of provinces) {
  writeFileSync(join(OUT, "regions", `${p.slug}.json`), JSON.stringify(p), "utf8");
}

// 목록용 얇은 색인 — 시도와 시군구 이름만 (읍면동 제외)
const index = provinces.map(({ slug, ko, cities }) => ({
  slug, ko,
  cities: cities.map(({ slug, ko }) => ({ slug, ko })),
}));
writeFileSync(join(OUT, "regions-index.json"), JSON.stringify({ provinces: index }), "utf8");

// 이전 방식 호환용 통짜 파일도 남겨 둡니다
writeFileSync(join(OUT, "regions.json"), JSON.stringify({ provinces }), "utf8");

console.log(`시도 ${provinces.length} / 시군구 ${nCity} / 읍면동 ${nDong}`);
console.log(`→ dist/_data/regions/{시도}.json  (${provinces.length}개)`);
console.log(`→ dist/_data/regions-index.json`);
console.log(`→ dist/_data/regions.json`);
