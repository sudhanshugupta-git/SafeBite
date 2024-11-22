from flask import Flask, request, jsonify
from preprocess import preprocess_inputs
from predict import load_model_and_encoder, make_prediction

# Initialize the Flask app
app = Flask(__name__)

# Load model and encoder (for serving the predictions)
model, encoder = load_model_and_encoder()

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Food Allergen Prediction API!"})

@app.route('/predict', methods=['POST'])
def predict_allergen():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Replace empty strings with "None"
        for key in ['sweetener', 'fat_oil', 'seasoning', 'allergens']:
            if key in data and not data[key].strip():
                data[key] = "None"

        # Extract fields from the JSON
        food_product = data['food_product']
        main_ingredient = data['main_ingredient']
        sweetener = data.get('sweetener', '')
        fat_oil = data.get('fat_oil', '')
        seasoning = data.get('seasoning', '')
        allergens = data.get('allergens', '')
        price = data['price']
        customer_rating = data['customer_rating']

        # Preprocess the input data
        input_data = preprocess_inputs(
            food_product,
            main_ingredient,
            sweetener,
            fat_oil,
            seasoning,
            allergens,
            price,
            customer_rating
        )

        # Make the prediction
        result = make_prediction(model, encoder, input_data)

        # Return the prediction in the response
        if result == 1:
            return jsonify({"prediction": "allergen detected", "product": food_product}), 200
        else:
            return jsonify({"prediction": "no allergen detected", "product": food_product}), 200

    except Exception as e:
        return jsonify({"error": f"Error making prediction: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the app
    app.run(debug=True)



'''
Invoke-WebRequest -Uri http://127.0.0.1:5000/predict `
    -Method POST `
    -Headers @{"Content-Type" = "application/json"} `
    -Body '{
        "food_product": "Gluten-Free Chocolate Cake",
        "main_ingredient": "Almond Flour",
        "sweetener": "Coconut sugar",
        "fat_oil": "Coconut oil",
        "seasoning": "Vanilla extract, Cocoa",
        "allergens": "Almond",
        "price": 10.50,
        "customer_rating": 4.5
    }'



    
    Invoke-WebRequest -Uri http://127.0.0.1:5000/predict `
    -Method POST `
    -Headers @{"Content-Type" = "application/json"} `
    -Body '{
         "food_product": "Lentil Soup",
         "main_ingredient": "Lentil",
         "sweetener": "None",
         "fat_oil": "Olive oil",
         "seasoning": "Herbs de Provence",
         "allergens": "None",
         "price": 4.50,
         "customer_rating": 4.0
    }'


'''