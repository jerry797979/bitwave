<?php
/**
 * 상담폼 설정 — 이 파일을 _config.php 로 복사한 뒤 값을 채우세요.
 *
 *   copy _config.example.php _config.php     (Windows)
 *   cp   _config.example.php _config.php     (Linux)
 *
 * _config.php 는 저장소에 올라가지 않습니다(.gitignore).
 * 토큰이 공개 저장소에 올라가면 아무나 알림을 보낼 수 있게 되기 때문입니다.
 */

return [

    // ── 텔레그램 알림 (선택) ────────────────────────────────
    // 비워 두면 알림을 보내지 않고 저장만 합니다.
    // 봇 만들기: 텔레그램에서 @BotFather → /newbot
    // chat_id 확인: 봇에게 아무 말이나 보낸 뒤
    //   https://api.telegram.org/bot<토큰>/getUpdates 접속 → result[0].message.chat.id
    'telegram_token'   => '',
    'telegram_chat_id' => '',

    // ── 이메일 알림 (선택) ─────────────────────────────────
    // 서버에 메일 발송이 설정돼 있어야 동작합니다. 안 되면 비워 두세요.
    'mail_to'   => '',              // 예: 'help@ziotes.com'
    'mail_from' => 'no-reply@ziotes.com',

    // ── 관리자 목록 보기 ───────────────────────────────────
    // /_leads.php?key=여기값  으로 접속하면 최근 신청을 볼 수 있습니다.
    // 반드시 길고 추측하기 어려운 값으로 바꾸세요. 비워 두면 목록 기능이 꺼집니다.
    'admin_key' => '',

    // ── 저장 위치 ─────────────────────────────────────────
    // 웹에서 직접 열리면 안 되는 폴더입니다. .htaccess 로 막아 두었습니다.
    'store_dir' => __DIR__ . '/_leads',

    // ── 스팸 차단 ─────────────────────────────────────────
    'min_seconds'  => 3,    // 폼을 연 지 이 시간(초) 안에 보내면 봇으로 봅니다
    'per_ip_limit' => 5,    // 같은 IP에서 한 시간에 받을 최대 건수
];
