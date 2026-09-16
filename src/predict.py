import joblib
import pandas as pd

modelo = joblib.load("models/modelo.pkl")

dia = pd.DataFrame({"dia": [12]})

prediccion = modelo.predict(dia)

print(prediccion)
