import requests


def brands_info():
    url = "https://catalog.wb.ru/catalog/men_shoes/catalog?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&kind=1&lang=ru&locale=ru&pricemarginCoeff=1.0&reg=0&regions=68,64,83,4,38,80,33,70,82,86,75,30,69,22,66,31,40,1,48,71&spp=0&subject=104;105;128;130;232;396;1382;1586"
    response = requests.get(url).json()
    data = response["data"]
    products = data["products"]
    lst = []
    for i in products:
        brands = dict()
        brands["brand"] = i["brand"]
        brands["brand_id"] = i["brandId"]
        lst.append(brands)

    brand_set = []
    for item in lst:
        br = item["brand"]
        brand_set.append(br)
        br_id = item["brand_id"]
        brand_set.append(br_id)

    new_brand_set = []
    for i in brand_set:
        if i not in new_brand_set:
            new_brand_set.append(i)

    conclusion_list = []
    for i in range(len(new_brand_set)):
        brand_info = dict()
        if type(new_brand_set[i]) is str:
            brand_info["brand"] = new_brand_set[i]
        else:
            brand_info["brand_id"] = new_brand_set[i]

        conclusion_list.append(brand_info)

    return conclusion_list
