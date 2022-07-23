import fake_useragent
import requests
from parsers.wildberries.brands_info import brands_info


def get_links(url) -> list:
    """
    return a list of links in one single page
    """
    user_agent = fake_useragent.UserAgent().random

    header = {
    "user-agent": user_agent
    }

    response = requests.get(url, headers=header).json()

    data = response["data"]
    products = data["products"]

    id_list = []

    for prod in products:
        try:
            if prod["promoTextCat"] == "CRAZY SALE":
                res = prod["id"]
                id_list.append(res)
        except KeyError:
            continue

    list_of_links = []
    for itr in range(len(id_list)):
        try:
            current_id = id_list.pop(itr)
            result = f"https://www.wildberries.ru/catalog/{current_id}/detail.aspx?targetUrl=GP"
            list_of_links.append(result)
        except IndexError:
            pass
    return list_of_links


def pages(brand_input) -> list:
    """
    returns a list of pages(lists of links per page)
    """
    try:
        result_brand = brands_info()[brand_input]
    except Exception:
        print("Такого нет!")

    list_of_pages = []

    try:
        for i in range(1, 10):
            page = get_links(f"https://catalog.wb.ru/catalog/men_shoes/catalog?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&fbrand={result_brand}&kind=1&lang=ru&locale=ru&page={i}&pricemarginCoeff=1.0&reg=0&regions=68,64,83,4,38,80,33,70,82,86,75,30,69,22,66,31,40,1,48,71&sort=popular&spp=0&subject=104;105;128;130;232;396;1382;1586")
            if len(page) != 0:
                list_of_pages.append(page)
            continue
    except UnboundLocalError:
            pass

    return list_of_pages


