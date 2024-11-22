# Food Allergen Prediction

## Overview
Food Allergen Prediction is a web application built with **Streamlit** and **Machine Learning**. It predicts whether a food product contains allergens based on the ingredients, seasoning, price, and customer ratings etc. This application aims to help users identify whether a food product may contain allergens by processing the given data.

## Features
- Predicts if a food product contains allergens based on its ingredients and other details.
- Takes input such as food product name, main ingredient, seasoning, allergens, price, and customer rating.
- Displays the result with a warning if allergens are detected.
- Easy-to-use interface for both food producers and consumers to check for allergens in food products.

## Technologies Used
- **Streamlit**: For building the interactive web app.
- **Python**: Core programming language for model logic and data processing.
- **Machine Learning**: Model to predict allergens based on input data.
- **Pandas**: For data manipulation and preprocessing.
- **Scikit-learn**: For machine learning model training.

## Installation

### Prerequisites
- Python 3.7 or higher.
- pip (Python package installer).

### Steps to Install

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/food-allergen-prediction.git
    ```

2. Navigate to the project directory:
    ```bash
    cd food-allergen-prediction
    ```

3. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - For Windows:
        ```bash
        venv\Scripts\activate
        ```
    - For macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application
Once the installation is complete, you can start the Streamlit app with the following command:

```bash
streamlit run app/main.py
# for api
python app/api.py