import requests

Token_telebot = "5892940185:AAGv1E2CovFqIlY0-yE2N8w03X6yeExLJa4"
chat_id = "5983861224"
# Bot_username = "@OnePiece009Bot"


def send_msg(text):
    url_req = f"https://api.telegram.org/bot{Token_telebot}/sendMessage?chat_id={chat_id}&text={text}"
    results = requests.get(url_req)
    print(results.json())




