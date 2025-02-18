# MCD Parser

This project uses FastAPI for creating APIs and Requests, BeautifulSoup for web scraping.

## Getting Started

First, clone the repository to your local machine:

git clone <https://github.com/goldi4ek/McD-parser>

### Prerequisites

Install the project dependencies:

```sh
pipenv install
```

Activate the pipenv shell:

```sh
pipenv shell
```

#### Running the Scraper

Run the scraper script to gather the data:

```sh
python scraper.py
```

#### Running the FastAPI server

start the FastAPI server:

```sh
uvicorn main:app --reload
```

Now, you can navigate to http://localhost:8000 in your web browser to interact with the API.

### API Endpoints

#### get: /all_products/

Example:

```sh
http://127.0.0.1:8000/all_products/
```

```json
{
    "product_id": "200360",
    "name": "Біг Чікен Чіз",
    "description": "Апетитний шматок ніжного розплавленого сиру в поєднанні із соковитою курочкою… А ще салат, смажена цибулька, медово-гірчичний соус — і все це в запашній булочці, присипаній білим і чорним кунжутом.",
    "calories": "803",
    "fats": "41.0",
    "carbs": "78.6",
    "proteins": "29.4",
    "unsaturated_fats": "10.0",
    "sugar": "11.7",
    "salt": "3.5",
    "portion": "300"
  },
  {
    "product_id": "200385",
    "name": "Біг Біф Чіз",
    "description": "Шматок ніжного розплавленого сиру і біфштекс із натуральної яловичини… Салат, смажена цибулька, нова булочка з чорним і білим кунжутом під особливим сирно-цибулевим соусом.",
    "calories": "824",
    "fats": "47.7",
    "carbs": "64.3",
    "proteins": "33.8",
    "unsaturated_fats": "18.0",
    "sugar": "9.4",
    "salt": "3.1",
    "portion": "300"
  }...
```

#### get: get: /products/{product_name}

Example:

```sh
http://127.0.0.1:8000/products/Біг%20Біф%20Чіз/
```

```json
{
  "product_id": "200385",
  "name": "Біг Біф Чіз",
  "description": "Шматок ніжного розплавленого сиру і біфштекс із натуральної яловичини… Салат, смажена цибулька, нова булочка з чорним і білим кунжутом під особливим сирно-цибулевим соусом.",
  "calories": "824",
  "fats": "47.7",
  "carbs": "64.3",
  "proteins": "33.8",
  "unsaturated_fats": "18.0",
  "sugar": "9.4",
  "salt": "3.1",
  "portion": "300"
}
```

#### get: //products/{product_name}/{product_field}

Example:

```sh
http://127.0.0.1:8000/products/Біг%20Біф%20Чіз/unsaturated_fats
```

```json
{
  "unsaturated_fats": "18.0"
}`
```
