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

    t = int(str(results.text)[-4:])

    if current <= t:
        text = str(results.text + " Released " + url)
        tele.send_msg(text=text)
        print(t)
        current = t + 1
        print(current)
        print("Done")

    elif current > t:
        print("Not changed")
        print(current)
        print(t)


    else:
        print("Error")

while True:
    main()