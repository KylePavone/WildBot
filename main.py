import requests


brands = {
    "adidas": 21,
    "Reebok": 777
}

url = f"https://catalog.wb.ru/catalog/men_shoes/catalog?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&fbrand={brands['Reebok']}&kind=1&lang=ru&locale=ru&page=4&pricemarginCoeff=1.0&reg=0&regions=68,64,83,4,38,80,33,70,82,86,75,30,69,22,66,31,40,1,48,71&sort=popular&spp=0&subject=104;105;128;130;232;396;1382;1586"


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

for i in range(len(id_list)):
    try:
        current_id = id_list.pop(i)
        print(f"https://www.wildberries.ru/catalog/{current_id}/detail.aspx?targetUrl=GP")
    except IndexError:
        pass
