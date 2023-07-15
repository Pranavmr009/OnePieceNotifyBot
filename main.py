import requests
from bs4 import BeautifulSoup
import tele

current = int(1086)
def main():

    global current
    changed = str(current)
    url = "https://tcbscans.com/mangas/5/one-piece"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    results = soup.find("div", class_="text-lg font-bold")

    print(results.text)
    if changed in results.text.lower():
        print("Not changed")

    elif changed not in results.text:
        text = str(results.text + " Released " + url)
        tele.send_msg(text=text)
        current += 1
        print(current)
        main()

    else:
        print("Error")

while True:
    main()