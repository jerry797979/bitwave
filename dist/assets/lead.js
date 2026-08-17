/* 상담 신청 폼 처리
 *
 * class="lead" 인 폼을 찾아 자동으로 붙습니다. 폼마다 코드를 넣을 필요가 없습니다.
 * 보내는 곳은 이 파일 위치를 기준으로 계산하므로, 하위 폴더에 올려도 동작합니다.
 */
(function () {
  "use strict";

  // 이 스크립트가 /assets/lead.js 이므로 두 단계 위가 사이트 루트
  var me = document.currentScript || (function () {
    var s = document.getElementsByTagName("script");
    return s[s.length - 1];
  })();
  var BASE = me.src.replace(/assets\/lead\.js.*$/, "");
  var ENDPOINT = BASE + "_lead.php";

  function hidden(form, name, value) {
    var el = form.querySelector('input[name="' + name + '"]');
    if (!el) {
      el = document.createElement("input");
      el.type = "hidden";
      el.name = name;
      form.appendChild(el);
    }
    el.value = value;
  }

  function setup(form) {
    // 봇 걸러내기 — 사람 눈에는 안 보이고, 자동 입력 도구는 채웁니다
    if (!form.querySelector('input[name="website"]')) {
      var trap = document.createElement("input");
      trap.type = "text";
      trap.name = "website";
      trap.tabIndex = -1;
      trap.autocomplete = "off";
      trap.setAttribute("aria-hidden", "true");
      trap.style.cssText =
        "position:absolute;left:-9999px;width:1px;height:1px;opacity:0;pointer-events:none";
      form.appendChild(trap);
    }
    hidden(form, "t", String(Math.floor(Date.now() / 1000)));
    hidden(form, "page", location.pathname + location.search);

    var msg = form.querySelector(".msg");
    if (!msg) {
      msg = document.createElement("p");
      msg.className = "msg";
      form.appendChild(msg);
    }

    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      if (form.dataset.sending === "1") return;

      var btn = form.querySelector('button[type="submit"], .btn');
      var label = btn ? btn.textContent : "";

      var data = {};
      Array.prototype.forEach.call(form.elements, function (el) {
        if (!el.name) return;
        if (el.type === "checkbox") data[el.name] = el.checked ? "1" : "";
        else data[el.name] = el.value;
      });
      // 동의 체크박스는 name이 없을 수 있으므로 따로 확인
      var agreeBox = form.querySelector('input[type="checkbox"]');
      if (agreeBox) data.agree = agreeBox.checked ? "1" : "";

      if (!data.name || !data.tel) {
        show(msg, "err", "담당자와 연락처를 적어 주세요.");
        return;
      }
      if (!data.agree) {
        show(msg, "err", "개인정보 수집·이용에 동의해 주세요.");
        return;
      }

      form.dataset.sending = "1";
      if (btn) { btn.disabled = true; btn.textContent = "보내는 중…"; }
      show(msg, "", "");

      fetch(ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
      })
        .then(function (r) { return r.json().catch(function () { return { ok: false, message: "잠시 후 다시 시도해 주세요." }; }); })
        .then(function (res) {
          if (res.ok) {
            form.reset();
            hidden(form, "t", String(Math.floor(Date.now() / 1000)));
            show(msg, "ok", res.message || "접수되었습니다. 확인 후 연락드리겠습니다.");
          } else {
            show(msg, "err", res.message || "접수하지 못했습니다. 전화로 연락 주시면 바로 도와드리겠습니다.");
          }
        })
        .catch(function () {
          show(msg, "err", "접수하지 못했습니다. 1555-5528로 연락 주시면 바로 도와드리겠습니다.");
        })
        .then(function () {
          form.dataset.sending = "";
          if (btn) { btn.disabled = false; btn.textContent = label; }
        });
    });
  }

  function show(el, kind, text) {
    el.className = "msg" + (kind ? " " + kind : "");
    el.textContent = text;
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  function init() {
    Array.prototype.forEach.call(document.querySelectorAll("form.lead"), setup);
  }
})();
