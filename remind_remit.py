"""
송금 비교기 분기 점검 리마인더 (1/4/7/10월 1일)
상업 가격은 JS렌더링+수시변동이라 크롤링 감시 부적합 → 분기별 수동 점검 알림 방식.
점검 절차: XE/Wise/Remitly/WU에서 C$1,000 CAD→INR 견적 확인 → CONFIG 수치와 비교 → 변경 시 클로드와 갱신.
"""
import os
import requests

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def send_telegram(msg):
    r = requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
        json={"chat_id": TELEGRAM_CHAT_ID, "text": msg},
        timeout=30,
    )
    print("텔레그램:", r.status_code)

if __name__ == "__main__":
    send_telegram(
        "[송금비교 분기점검] ca-india-remit 수수료 점검 시기.\n"
        "절차: XE/Wise/Remitly/WU에서 C$1,000 CAD→INR 견적 확인 → 사이트 수치와 비교 → 차이 크면 클로드와 CONFIG 갱신.\n"
        "사이트: ca-india-remit.pages.dev"
    )
