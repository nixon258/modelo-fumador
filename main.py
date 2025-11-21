from scripts.loader import Loader
from scripts.preprosesing import preporsesardor
from scripts.trainModel import trainModel
from scripts.predict import predecirFuamdor
import pandas as pd


def main():
    print("========== cargando data frame ==========")
    loader = Loader("data/smoking.csv")
    df= loader.loadDB()

    print("========== alistando los datos ==========")
    prep = preporsesardor(df)

    X = prep.X
    Y = prep.Y

    print("========== ENTRENANDO MODELO ==========")
    trainModel(X, Y)

    print("========== PREDICCIÓN DE PRUEBA ==========")
    datos_usuario = {
        'age': 40,
    'height(cm)': 175,
    'weight(kg)': 75,
    'waist(cm)': 85.0,
    'systolic': 122,
    'relaxation': 82,
    'fasting blood sugar': 97,
    'Cholesterol': 190,
    'triglyceride': 130,
    'HDL': 55,
    'LDL': 112,
    'hemoglobin': 14.7,
    'Urine protein': 1,
    'serum creatinine': 1.1,
    'AST': 24,
    'ALT': 25,
    'Gtp': 27,
    'Male': 1,
    'Female': 0
    }

    predictor = predecirFuamdor()
    resultado, prob = predictor.predecir(datos_usuario)

    print("\n========== RESULTADO FINAL ==========")
    print(f"Clasificación: {resultado}")
    print(f"Probabilidad: {prob:.2%}")


if __name__ == "__main__":
    main()
