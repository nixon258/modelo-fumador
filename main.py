from scripts.loader import Loader
from scripts.preprosesing import preporsesardor
from scripts.trainModel import trainModel
from scripts.predict import predecirFuamdor
import pandas as pd


def main():
    print("========== CARGANDO BASE DE DATOS ==========")
    loader = Loader("data/smoking.csv")
    df= loader.loadDB()

    print("========== PREPROCESANDO DATOS ==========")
    prep = preporsesardor(df)

    X = prep.X
    Y = prep.Y

    print("========== ENTRENANDO MODELO ==========")
    trainer = trainModel(X, Y)

    print("========== PREDICCIÓN DE PRUEBA ==========")
    # Ejemplo de datos de prueba
    datos_usuario = {
        "age": 40,
        "height(cm)": 175,
        "weight(kg)": 70,
        "waist(cm)": 90,
        "Male": 1,
        "Female": 0
    }

    predictor = predecirFuamdor()
    resultado, prob = predictor.predecir(datos_usuario)

    print("\n========== RESULTADO FINAL ==========")
    print(f"Clasificación: {resultado}")
    print(f"Probabilidad: {prob:.2%}")


if __name__ == "__main__":
    main()
