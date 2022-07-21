import requests
from bs4 import BeautifulSoup
from time import sleep
import fake_useragent


def lamoda_parse():
    fake_agent = fake_useragent.UserAgent().random
    header = {
        "user-agent": fake_agent
    }

    url = "https://www.lamoda.ru/c/2981/shoes-krossovk-kedy-muzhskie/?brands=1061&page=1"

    response = requests.get(url, headers=header).text

    soup = BeautifulSoup(response, "lxml")
    elem = soup.find_all("div", class_="x-product-card__card")

    list_of_elems = []

    for el in elem:
        res = el.find("a").get("href")
        list_of_elems.append(res)

    list_of_links = []

    for link in list_of_elems:
        result_link = f"https://www.lamoda.ru/{link}"
        list_of_links.append(result_link)

    number = int(input("Введите количество пар для отображения: "))

    for i in range(number):
        print(list_of_links[i])
        sleep(0.7)

    return "Done"

print(lamoda_parse())
