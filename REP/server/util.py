import json
import pickle
import numpy as np
import sklearn

__locations = None
__data_columns = None
__model = None

# property types: "condo/co-op", "mobile/manufactured home", "multi-family (2-4 unit)",
# "multi-family (5+ unit)", "single family residential", "townhouse"]}

def get_estimated_price(city, property_type, sqft, bath, beds, year_built, model, X_columns):
    import numpy as np
    # Convert input strings to lowercase to match the exported feature names
    city = city.strip().lower()
    property_type = property_type.strip().lower()

    # Create a zero vector for the input features
    x = np.zeros(len(X_columns))

    # Assign numeric features using the lowercase keys
    if 'square feet' in X_columns:
        x[X_columns.index('square feet')] = sqft
    if 'baths' in X_columns:
        x[X_columns.index('baths')] = bath
    if 'beds' in X_columns:
        x[X_columns.index('beds')] = beds
    if 'year built' in X_columns:
        x[X_columns.index('year built')] = year_built

    # One-hot encode the city
    if city in X_columns:
        x[X_columns.index(city)] = 1
    else:
        print(f"Warning: City '{city}' not found in training data.")

    # One-hot encode the property type
    if property_type in X_columns:
        x[X_columns.index(property_type)] = 1
    else:
        print(f"Warning: Property type '{property_type}' not found in training data.")

    # Get the predicted log price from the model
    predicted_log_price = __model.predict([x])[0]
    # Convert the log price back to actual price
    predicted_price = np.expm1(predicted_log_price)

    return round(predicted_price, 2)


def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:-6]

    global __model
    with open("./artifacts/la_county_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
        print("loading saved artifacts...done")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('alhambra', 'single family residential', 1500, 6, 4, 1970, __model, __data_columns))

if hasattr(__model, "coef_"):
    print("Model Coefficients:")
    print(__model.coef_)
    print("Model Intercept:")
    print(__model.intercept_)

# If the model is a pipeline, for example with a step named 'lr'
elif hasattr(__model, "named_steps"):
    print("Model Coefficients (Pipeline):")
    print(__model.named_steps["lr"].coef_)
    print("Model Intercept (Pipeline):")
    print(__model.named_steps["lr"].intercept_)
else:
    print("The model does not have coefficient attributes.")
