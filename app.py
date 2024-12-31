from flask import Flask, request, jsonify
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the saved model
model = joblib.load('fraud_detection.pkl')

@app.route('/')
def home():
    return "Fraud Detection API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get and validate data
        data = request.get_json(force=True)
        if 'features' not in data:
            return jsonify({'error': 'Missing key: "features"'}), 400
        if len(data['features']) != 22:  # Assuming the model expects 22 features
            return jsonify({'error': f'Expected 22 features, got {len(data["features"])}'}), 400

        # Convert data into numpy array
        features = np.array(data['features']).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)

        # Return prediction result as JSON
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
