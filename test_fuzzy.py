from soft_computing.fuzzy_logic import predict_damage_risk


risk, category = predict_damage_risk(

    age=8,

    condition=5,

    rain=8,

    traffic_level=8,

    drainage_level=9,

    vehicle_frequency=8

)


print("ROAD DAMAGE PROGRESSION PREDICTION")

print("-----------------------------------")

print("Predicted Risk Score:", risk)

print("Risk Category:", category)