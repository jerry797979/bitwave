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
writeFileSync(join(OUT, "regions.json"), JSON.stringify({ provinces }, null, 0), "utf8");

console.log(`시도 ${provinces.length} / 시군구 ${nCity} / 읍면동 ${nDong}`);
console.log(`→ dist/_data/regions.json`);
