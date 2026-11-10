import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# ----------------------------------
# 1. Define Input Variables
# ----------------------------------

road_age = ctrl.Antecedent(np.arange(0, 31, 1), 'road_age')

road_condition = ctrl.Antecedent(np.arange(0, 11, 1), 'road_condition')

rainfall = ctrl.Antecedent(np.arange(0, 11, 1), 'rainfall')

traffic = ctrl.Antecedent(np.arange(0, 11, 1), 'traffic')

drainage = ctrl.Antecedent(np.arange(0, 11, 1), 'drainage')

heavy_vehicles = ctrl.Antecedent(np.arange(0, 11, 1), 'heavy_vehicles')


# ----------------------------------
# 2. Define Output Variable
# ----------------------------------

damage_risk = ctrl.Consequent(
    np.arange(0, 101, 1),
    'damage_risk'
)


# ----------------------------------
# 3. Membership Functions
# ----------------------------------

# Road Age

road_age['new'] = fuzz.trimf(
    road_age.universe, [0, 0, 8]
)

road_age['moderate'] = fuzz.trimf(
    road_age.universe, [4, 12, 20]
)

road_age['old'] = fuzz.trimf(
    road_age.universe, [15, 30, 30]
)


# Existing Road Condition

road_condition['good'] = fuzz.trimf(
    road_condition.universe, [0, 0, 3]
)

road_condition['moderate'] = fuzz.trimf(
    road_condition.universe, [2, 5, 8]
)

road_condition['poor'] = fuzz.trimf(
    road_condition.universe, [7, 10, 10]
)


# Rainfall

rainfall['low'] = fuzz.trimf(
    rainfall.universe, [0, 0, 4]
)

rainfall['moderate'] = fuzz.trimf(
    rainfall.universe, [2, 5, 8]
)

rainfall['high'] = fuzz.trimf(
    rainfall.universe, [6, 10, 10]
)


# Traffic Density

traffic['low'] = fuzz.trimf(
    traffic.universe, [0, 0, 4]
)

traffic['medium'] = fuzz.trimf(
    traffic.universe, [2, 5, 8]
)

traffic['high'] = fuzz.trimf(
    traffic.universe, [6, 10, 10]
)


# Drainage Severity

drainage['good'] = fuzz.trimf(
    drainage.universe, [0, 0, 4]
)

drainage['average'] = fuzz.trimf(
    drainage.universe, [2, 5, 8]
)

drainage['poor'] = fuzz.trimf(
    drainage.universe, [6, 10, 10]
)


# Heavy Vehicle Frequency

heavy_vehicles['low'] = fuzz.trimf(
    heavy_vehicles.universe, [0, 0, 4]
)

heavy_vehicles['medium'] = fuzz.trimf(
    heavy_vehicles.universe, [2, 5, 8]
)

heavy_vehicles['high'] = fuzz.trimf(
    heavy_vehicles.universe, [6, 10, 10]
)


# Output Membership Functions

damage_risk['low'] = fuzz.trimf(
    damage_risk.universe, [0, 0, 40]
)

damage_risk['medium'] = fuzz.trimf(
    damage_risk.universe, [25, 50, 75]
)

damage_risk['high'] = fuzz.trimf(
    damage_risk.universe, [60, 100, 100]
)


# ----------------------------------
# 4. Define Fuzzy Rules
# ----------------------------------

rule1 = ctrl.Rule(
    road_condition['poor'] |
    (rainfall['high'] & drainage['poor']),
    damage_risk['high']
)

rule2 = ctrl.Rule(
    road_age['old'] &
    traffic['high'] &
    heavy_vehicles['high'],
    damage_risk['high']
)

rule3 = ctrl.Rule(
    road_condition['moderate'] &
    rainfall['moderate'] &
    traffic['medium'],
    damage_risk['medium']
)

rule4 = ctrl.Rule(
    drainage['average'] &
    rainfall['high'],
    damage_risk['high']
)

rule5 = ctrl.Rule(
    road_condition['good'] &
    road_age['new'] &
    rainfall['low'] &
    traffic['low'] &
    drainage['good'] &
    heavy_vehicles['low'],
    damage_risk['low']
)

rule6 = ctrl.Rule(
    traffic['high'] &
    road_condition['moderate'],
    damage_risk['high']
)

rule7 = ctrl.Rule(
    drainage['poor'] &
    heavy_vehicles['high'],
    damage_risk['high']
)

rule8 = ctrl.Rule(
    road_age['moderate'] &
    road_condition['moderate'],
    damage_risk['medium']
)

rule9 = ctrl.Rule(
    rainfall['low'] &
    drainage['good'] &
    road_condition['good'],
    damage_risk['low']
)


# ----------------------------------
# 5. Create Fuzzy Control System
# ----------------------------------

road_control = ctrl.ControlSystem([
    rule1, rule2, rule3,
    rule4, rule5, rule6,
    rule7, rule8, rule9
])


# ----------------------------------
# 6. Prediction Function
# ----------------------------------

def predict_damage_risk(
    age,
    condition,
    rain,
    traffic_level,
    drainage_level,
    vehicle_frequency
):

    simulation = ctrl.ControlSystemSimulation(road_control)

    simulation.input['road_age'] = age

    simulation.input['road_condition'] = condition

    simulation.input['rainfall'] = rain

    simulation.input['traffic'] = traffic_level

    simulation.input['drainage'] = drainage_level

    simulation.input['heavy_vehicles'] = vehicle_frequency

    simulation.compute()

    risk = simulation.output['damage_risk']

    if risk < 35:
        category = "Low"

    elif risk < 65:
        category = "Medium"

    else:
        category = "High"

    return round(risk, 2), category