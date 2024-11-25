import requests

url = "https://safebite-api.onrender.com/predict"
data = {
    "food_product": "bread",
    "main_ingredient": "wheat",
    "sweetener": "",
    "fat_oil": "butter",
    "seasoning": "",
    "allergens": "",
    "price": 50,
    "customer_rating": 4.5
}
response = requests.post(url, json=data)
print(response.json())
