P_rain = 0.2 
P_no_rain = 0.8 
P_cloudy_given_rain = 0.9 
P_cloudy_given_no_rain = 0.3 
P_cloudy = (P_cloudy_given_rain * P_rain) + (P_cloudy_given_no_rain * P_no_rain) 
P_rain_given_cloudy = (P_cloudy_given_rain * P_rain) / P_cloudy 
print("P(Cloudy) =", P_cloudy) 
print("P(Rain | Cloudy) =", P_rain_given_cloudy) 
if P_rain_given_cloudy > 0.5: 
    print("Prediction: It will likely Rain") 
else: 
    print("Prediction: Rain is less likely")  