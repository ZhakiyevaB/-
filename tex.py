import requests
from bs4 import BeautifulSoup
import json
url = "https://www.technodom.kz/cms/sale?utm_source=yandex&utm_medium=cpc&utm_campaign=yandex_search_td_dm_technodom_upc_1123&yclid=14491457557665153023"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(response.text, "lxml")

phones = soup.find_all("div", class_="ProductCardV_card__pIoz2 ProductItem_product__HR8Z9")

apple_phones = []

for phone in phones[:20]:
    memory_info = phone.find_all("div", class_="Chips__Body")

    if "256Гб" in memory_info:
        name = phone.find_all("div", class_="Typography ProductCardV_title__rFAYr ProductCardV_loading__TkTOe Typography__M")
        price = phone.find_all("div", class_="Typography ProductCardPrices_price__5dlTx Typography__Subtitle")

        apple_phones.append({"name": name, "memory": memory_info, "price": price})

with open("apple.json", "w", encoding="utf-8") as json_file:
    json.dump(apple_phones, json_file, ensure_ascii=False, indent=2)

print()

