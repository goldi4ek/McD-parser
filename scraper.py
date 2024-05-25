import requests
from bs4 import BeautifulSoup
import json


URL = "https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html"


def fetch_menu():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")

    menu_items = []
    for item in soup.find_all("li", class_="cmp-category__item"):

        product_id = item["data-product-id"]

        product_url = f"https://www.mcdonalds.com/dnaapp/itemDetails?country=UA&language=uk&showLiveData=true&item={product_id}"

        response = requests.get(product_url)

        data = response.json()

        error = data.get("error")
        if error:
            description = error.get("description", None)
            menu_items.append({"product_id": product_id, "description": description})
            continue

        name = data["item"].get("item_name", None)
        description = data["item"].get("description", None)

        nutrients = data["item"]["nutrient_facts"]["nutrient"]
        nutrient_dict = {
            nutrient["nutrient_name_id"]: nutrient["value"] for nutrient in nutrients
        }
        calories = nutrient_dict.get("energy_kcal", None)
        fats = nutrient_dict.get("fat", None)
        carbs = nutrient_dict.get("carbohydrate", None)
        proteins = nutrient_dict.get("protein", None)
        unsaturated_fats = nutrient_dict.get("НЖК", None)
        sugar = nutrient_dict.get("Цукор", None)
        salt = nutrient_dict.get("salt", None)
        portion = nutrient_dict.get("primary_serving_size", None)

        menu_items.append(
            {
                "product_id": product_id,
                "name": name,
                "description": description,
                "calories": calories,
                "fats": fats,
                "carbs": carbs,
                "proteins": proteins,
                "unsaturated_fats": unsaturated_fats,
                "sugar": sugar,
                "salt": salt,
                "portion": portion,
            }
        )

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(menu_items, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    fetch_menu()
