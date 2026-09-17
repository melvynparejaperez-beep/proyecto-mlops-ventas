from fastapi import FastAPI
import joblib

app = FastAPI()

modelo = joblib.load("models/modelo.pkl")

@app.get("/predict")
def predict(dia:int):

resultado = modelo.predict([[dia]])

return {
"dia":dia,
"prediccion":float(resultado[0])
}
