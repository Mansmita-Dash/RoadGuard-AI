from flask import Flask, render_template, request
from soft_computing.fuzzy_logic import predict_damage_risk

app = Flask(__name__, static_folder='Static')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/assessment')
def assessment():
    return render_template('assessment.html')


@app.route('/predict', methods=['POST'])
def predict():

    # Get data from the assessment form
    road_age = float(request.form.get('road_age'))
    road_condition = request.form.get('road_condition')
    rainfall = request.form.get('rainfall')
    traffic = request.form.get('traffic')
    drainage = request.form.get('drainage')
    heavy_vehicles = request.form.get('heavy_vehicles')

    # Convert categorical inputs into numerical values
    condition_values = {
        'Good': 0,
        'Moderate': 5,
        'Poor': 8,
        'Severe': 10
    }

    rainfall_values = {
        'Low': 0,
        'Moderate': 5,
        'High': 8,
        'Very High': 10
    }

    traffic_values = {
        'Low': 0,
        'Medium': 5,
        'High': 8,
        'Very High': 10
    }

    drainage_values = {
        'Good': 0,
        'Average': 5,
        'Poor': 10
    }

    vehicle_values = {
        'Low': 0,
        'Medium': 5,
        'High': 10
    }

    # Run the Fuzzy Logic model
    risk_score, risk_category = predict_damage_risk(
        age=road_age,
        condition=condition_values[road_condition],
        rain=rainfall_values[rainfall],
        traffic_level=traffic_values[traffic],
        drainage_level=drainage_values[drainage],
        vehicle_frequency=vehicle_values[heavy_vehicles]
    )

    # Generate maintenance recommendation
    if risk_category == "Low":
        recommendation = "Continue regular road monitoring and routine maintenance."

    elif risk_category == "Medium":
        recommendation = "Schedule preventive maintenance and inspect drainage conditions."

    else:
        recommendation = "Prioritize road inspection and consider urgent repair work."

    return render_template(
        'result.html',
        road_age=road_age,
        road_condition=road_condition,
        rainfall=rainfall,
        traffic=traffic,
        drainage=drainage,
        heavy_vehicles=heavy_vehicles,
        risk_score=risk_score,
        risk_category=risk_category,
        recommendation=recommendation
    )


if __name__ == '__main__':
    app.run(debug=True)