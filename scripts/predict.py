import joblib
import pandas as pd

class predecirFuamdor:

    def __init__(self):
        self.modelo = joblib.load("models/modelo_fumador.joblib")
        self.features = self.modelo.feature_names_in_

    def predecir(self, datos_usuario):
        df = pd.DataFrame([datos_usuario])
        df = df[self.features]

        prob = self.modelo.predict_proba(df)[0][1]
        pred = self.modelo.predict(df)[0]

        resultado = "Fumador" if pred == 1 else "No fumador"
        print(f"Resultado: {resultado} (Probabilidad: {prob:.2%})")

        return resultado, prob