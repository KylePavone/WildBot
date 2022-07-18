import requests
from time import sleep


brands = {
    "adidas": 21,
    "Reebok": 777
}

def get_links(url):
    response = requests.get(url).json()
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


#print(len(get_links(f"https://catalog.wb.ru/catalog/men_shoes/catalog?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&fbrand={brands['Reebok']}&kind=1&lang=ru&locale=ru&page=1&pricemarginCoeff=1.0&reg=0&regions=68,64,83,4,38,80,33,70,82,86,75,30,69,22,66,31,40,1,48,71&sort=popular&spp=0&subject=104;105;128;130;232;396;1382;1586")))

def list_of_pages():
    lst = []
    for i in range(10):
        try:
            page = get_links(f"https://catalog.wb.ru/catalog/men_shoes/catalog?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&fbrand={brands['adidas']}&kind=1&lang=ru&locale=ru&page={i}&pricemarginCoeff=1.0&reg=0&regions=68,64,83,4,38,80,33,70,82,86,75,30,69,22,66,31,40,1,48,71&sort=popular&spp=0&subject=104;105;128;130;232;396;1382;1586")
            if len(page) > 0:
                lst.append(page)
        except Exception:
            pass
    for i in range(10):
        try:
            yield lst[i]
        except IndexError:
            pass


def pages_count(n):
    gen = list_of_pages()
    for i in range(n):
        try:
            print(next(gen))
            sleep(1)
        except StopIteration:
            print("Больше страниц нет!")
            break

pages = int(input("Введите количество страниц: "))

if __name__ == "__main__":
    pages_count(pages)
