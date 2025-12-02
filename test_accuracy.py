"""
Test script to validate model accuracy with known real-world cars
"""

import requests
import json

API_URL = "http://localhost:8000/predict"

# Real-world cars with known 0-100 km/h times
# Sources: manufacturer specs, Car and Driver, Motor Trend
test_cars = [
    {
        "name": "2020 Porsche 911 Turbo S",
        "specs": {
            "year": 2020,
            "horsepower": 640,
            "engine_size": 3.8,
            "torque": 590,
            "weight": 3640,
            "drivetrain_rwd": 1,
            "transmission_dct": 1
        },
        "actual_time": 2.7  # seconds 0-100 km/h
    },
    {
        "name": "2019 Ferrari 488 Pista",
        "specs": {
            "year": 2019,
            "horsepower": 710,
            "engine_size": 3.9,
            "torque": 568,
            "weight": 3053,
            "drivetrain_rwd": 1,
            "transmission_dct": 1
        },
        "actual_time": 2.85
    },
    {
        "name": "2021 Tesla Model S Plaid",
        "specs": {
            "year": 2021,
            "horsepower": 1020,
            "engine_size": 0,  # Electric
            "torque": 1050,
            "weight": 4766,
            "drivetrain_rwd": 0,  # AWD
            "transmission_dct": 0
        },
        "actual_time": 2.1
    },
    {
        "name": "2020 McLaren 720S",
        "specs": {
            "year": 2020,
            "horsepower": 710,
            "engine_size": 4.0,
            "torque": 568,
            "weight": 3128,
            "drivetrain_rwd": 1,
            "transmission_dct": 1
        },
        "actual_time": 2.9
    },
    {
        "name": "2019 Lamborghini Huracan Performante",
        "specs": {
            "year": 2019,
            "horsepower": 640,
            "engine_size": 5.2,
            "torque": 443,
            "weight": 3047,
            "drivetrain_rwd": 0,  # AWD
            "transmission_dct": 1
        },
        "actual_time": 2.9
    },
    {
        "name": "2020 Chevrolet Corvette C8",
        "specs": {
            "year": 2020,
            "horsepower": 495,
            "engine_size": 6.2,
            "torque": 470,
            "weight": 3366,
            "drivetrain_rwd": 1,
            "transmission_dct": 1
        },
        "actual_time": 2.9
    },
    {
        "name": "2019 Nissan GT-R",
        "specs": {
            "year": 2019,
            "horsepower": 565,
            "engine_size": 3.8,
            "torque": 467,
            "weight": 3933,
            "drivetrain_rwd": 0,  # AWD
            "transmission_dct": 1
        },
        "actual_time": 2.9
    },
    {
        "name": "2020 Audi R8 V10 Plus",
        "specs": {
            "year": 2020,
            "horsepower": 602,
            "engine_size": 5.2,
            "torque": 413,
            "weight": 3516,
            "drivetrain_rwd": 0,  # AWD
            "transmission_dct": 1
        },
        "actual_time": 3.2
    }
]

def test_model_accuracy():
    """Test the model with known cars and calculate error metrics"""
    
    print("=" * 80)
    print("MODEL ACCURACY TEST - Real World Cars")
    print("=" * 80)
    print()
    
    errors = []
    results = []
    
    for car in test_cars:
        try:
            # Make prediction
            response = requests.post(API_URL, json=car["specs"])
            
            if response.status_code == 200:
                prediction_data = response.json()
                predicted = prediction_data["prediction"]
                actual = car["actual_time"]
                error = predicted - actual
                abs_error = abs(error)
                percent_error = (abs_error / actual) * 100
                
                errors.append(abs_error)
                
                result = {
                    "name": car["name"],
                    "actual": actual,
                    "predicted": predicted,
                    "error": error,
                    "abs_error": abs_error,
                    "percent_error": percent_error
                }
                results.append(result)
                
                # Print result
                status = "✓" if abs_error < 0.5 else "⚠️" if abs_error < 1.0 else "❌"
                print(f"{status} {car['name']}")
                print(f"   Actual: {actual:.2f}s | Predicted: {predicted:.2f}s | Error: {error:+.2f}s ({percent_error:.1f}%)")
                print()
            else:
                print(f"❌ {car['name']} - API Error: {response.status_code}")
                print()
                
        except Exception as e:
            print(f"❌ {car['name']} - Error: {e}")
            print()
    
    # Calculate overall metrics
    if errors:
        print("=" * 80)
        print("OVERALL METRICS")
        print("=" * 80)
        
        mae = sum(errors) / len(errors)
        rmse = (sum(e**2 for e in errors) / len(errors)) ** 0.5
        max_error = max(errors)
        min_error = min(errors)
        
        print(f"Mean Absolute Error (MAE):  {mae:.3f} seconds")
        print(f"Root Mean Squared Error:    {rmse:.3f} seconds")
        print(f"Max Error:                  {max_error:.3f} seconds")
        print(f"Min Error:                  {min_error:.3f} seconds")
        print()
        
        # Accuracy buckets
        within_half_sec = sum(1 for e in errors if e < 0.5)
        within_one_sec = sum(1 for e in errors if e < 1.0)
        
        print(f"Predictions within ±0.5s:   {within_half_sec}/{len(errors)} ({within_half_sec/len(errors)*100:.1f}%)")
        print(f"Predictions within ±1.0s:   {within_one_sec}/{len(errors)} ({within_one_sec/len(errors)*100:.1f}%)")
        print()
        
        # Compare to training metrics
        print("=" * 80)
        print("COMPARISON TO TRAINING METRICS")
        print("=" * 80)
        print("Training MAE: ~0.29-0.31 seconds (on test set)")
        print(f"Real-world MAE: {mae:.3f} seconds")
        
        if mae < 0.5:
            print("✅ Model performing well on real-world data!")
        elif mae < 1.0:
            print("⚠️ Model decent but could be improved")
        else:
            print("❌ Model needs improvement for real-world predictions")
        print()
        
        # Show best and worst predictions
        sorted_results = sorted(results, key=lambda x: x['abs_error'])
        
        print("=" * 80)
        print("BEST PREDICTION")
        print("=" * 80)
        best = sorted_results[0]
        print(f"{best['name']}")
        print(f"Actual: {best['actual']:.2f}s | Predicted: {best['predicted']:.2f}s | Error: {best['error']:+.2f}s")
        print()
        
        print("=" * 80)
        print("WORST PREDICTION")
        print("=" * 80)
        worst = sorted_results[-1]
        print(f"{worst['name']}")
        print(f"Actual: {worst['actual']:.2f}s | Predicted: {worst['predicted']:.2f}s | Error: {worst['error']:+.2f}s")
        print()
    
    else:
        print("❌ No successful predictions to analyze")

if __name__ == "__main__":
    print()
    print("Make sure your API is running on http://localhost:8000")
    print("Press Enter to start testing...")
    input()
    
    test_model_accuracy()