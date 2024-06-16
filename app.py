import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pickle
from flask import Flask, request, jsonify
import logging

# Baca data
data = pd.read_csv('SALES.txt', sep='\s+', header=None, names=['Sales', 'Advertising'])

# Pisahkan fitur dan target
X = data[['Sales']]
y = data['Advertising']

# Bagi data menjadi training dan testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Buat model regresi linier
model = LinearRegression()
model.fit(X_train, y_train)

# Prediksi pada data test
y_pred = model.predict(X_test)

# Evaluasi model
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

# Cetak evaluasi model
print(f'RMSE: {rmse}')
print(f'R2 Score: {r2}')

# Simpan model
with open('regression.pkl', 'wb') as f:
    pickle.dump(model, f)

# Prediksi untuk sales 50, 100, dan 150
sales_values = np.array([[50], [100], [150]])
predicted_costs = model.predict(sales_values)

for sales, cost in zip([50, 100, 150], predicted_costs):
    print(f'Predicted advertising cost for {sales} sales: ${cost} million')

# Aplikasi Flask
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Endpoint untuk menampilkan data
@app.route('/data', methods=['GET'])
def display_data():
    return data.to_html()

# Endpoint untuk menampilkan RMSE dan R2 Score
@app.route('/metrics', methods=['GET'])
def display_metrics():
    metrics = {
        'RMSE': rmse,
        'R2 Score': r2
    }
    return jsonify(metrics)

# Create endpoint /predict-advertising
@app.route('/predict-advertising', methods=['POST', 'GET'])
def predict():
    app.logger.debug("Received request for /predict-advertising")

    # Get argument parameter from endpoint
    data = request.args
    app.logger.debug(f"Request arguments: {data}")

    with open("regression.pkl", 'rb') as file:
        pk_model = pickle.load(file)
    app.logger.debug("Model loaded successfully")

    # Predict with regression model
    sales = np.array([[float(data['sales'])]])
    prediction = pk_model.predict(sales)
    output = prediction[0]

    # Print prediction message
    app.logger.debug(f"Predicted advertising cost for {data['sales']} sales: ${output} million")

    # Return structured prediction result
    response = {
        "Predicted Advertising Cost": output,
        "Sales Input": float(data['sales'])
    }

    return jsonify(response)

# Run endpoint server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
