from fastapi import FastAPI
import joblib
import os

app = FastAPI(title="API MLOps Ventas")

# Comprobación segura del archivo del modelo
MODEL_PATH = "models/modelo.pkl"

if os.path.exists(MODEL_PATH):
    modelo = joblib.load(MODEL_PATH)
else:
    modelo = None
    print(f"Advertencia: No se encontró el archivo en '{MODEL_PATH}'. Carga un modelo antes de hacer predicciones.")

@app.get("/")
def inicio():
    return {
        "estado": "activo",
        "modelo_cargado": modelo is not None
    }
