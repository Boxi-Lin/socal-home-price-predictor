from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)


@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['city']
    property_type = request.form['property_type']
    bed = int(request.form['bed'])
    bath = int(request.form['bath'])
    year_built = int(request.form['year_built'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, property_type, total_sqft, bath, bed, year_built, util.__model, util.__data_columns)
    })
    return response

if __name__ == "__main__":
    util.load_saved_artifacts()
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run()