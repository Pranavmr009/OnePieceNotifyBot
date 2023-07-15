import requests

Token_telebot = "Token"
chat_id = "ID"
# Bot_username = "@OnePiece009Bot"


def send_msg(text):
    url_req = f"https://api.telegram.org/bot{Token_telebot}/sendMessage?chat_id={chat_id}&text={text}"
    results = requests.get(url_req)
    print(results.json())




