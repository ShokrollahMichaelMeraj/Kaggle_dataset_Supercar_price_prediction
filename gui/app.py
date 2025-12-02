from flask import Flask, request, jsonify
import numpy as np
import joblib
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScalar

model = load_model('../models/nn_zero_to_sixty.keras')
scalar = joblib.load('../models/nn_scaler.pkl')
featureInfo = joblib.load('../models/feature_info.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        carFeatures = np.array([[
            data['year'],
            data['horsepower'],
            data['engine_size'],
            data['torque'],
            data['weight'],
            data['powerWeight'],
            data['torqueWeight'],
            data['drivetrainRwd'],
            data['transmissionDct']
        ]])
        carFeaturesScaled = scalar.transform(carFeatures)
        prediction = model.predict(carFeaturesScaled)
        return jsonify({'acceleration': prediction[0][0]})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
if __name__ == '__main__':
    app.run(debug=True)