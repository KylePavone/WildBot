import requests
from bs4 import BeautifulSoup
import fake_useragent


def lm_parse(brand):
    fake_agent = fake_useragent.UserAgent().random
    header = {
        "user-agent": fake_agent
    }

    url = f"https://www.lamoda.ru/c/2981/shoes-krossovk-kedy-muzhskie/?brands={brand}&page=1"

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


    return list_of_links

#print(lm_parse("1061"))
