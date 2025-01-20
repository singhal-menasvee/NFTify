from flask import Flask, request, jsonify
import numpy as np
import joblib  # To load your trained ML model

app = Flask(__name__)

# Load your trained machine learning model (replace 'nft_model.pkl' with your model)
model = joblib.load('nft_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the frontend (NFT metadata)
    data = request.json
    
    # Prepare the data for prediction (you need to modify this based on your NFT model)
    features = np.array([data['artist_reputation'], data['rarity_score'], data['previous_sales']])
    
    # Predict the value of the NFT
    prediction = model.predict([features])
    
    # Return the predicted value as JSON
    return jsonify({'predicted_value': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
