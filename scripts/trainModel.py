import json
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from scripts.preprosesing import preporsesardor
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from utils.paths import ruta_absoluta


class trainModel:
    def __init__(self,x,y):
        X_train, X_test, y_train, y_test = self.preparardt(x,y)
        modelo = self.entrnarmodel(X_train, y_train)
        metrics = self.evaluar(modelo, X_test, y_test)
        self.exportar(modelo, metrics)

    def preparardt(self,x,y):
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.35, random_state=17)
        return X_train, X_test, y_train, y_test

    def entrnarmodel(self,X_train, y_train):
        modelo = LogisticRegression()
        modelo.fit(X_train, y_train)
        return modelo

    def evaluar(self,modelo,X_test,y_test):
        # Evaluar exactitud
        y_pred = modelo.predict(X_test)
        y_proba = modelo.predict_proba(X_test)[:, 1]

        metrics = {
            "accuracy": round(accuracy_score(y_test, y_pred), 3),
            "precision": round(precision_score(y_test, y_pred), 3),
            "recall": round(recall_score(y_test, y_pred), 3),
            "f1": round(f1_score(y_test, y_pred), 3),
            "roc_auc": round(roc_auc_score(y_test, y_proba), 3)
        }
        return metrics

    def exportar(self,modelo,metrics):
        joblib.dump(modelo, ruta_absoluta("models/modelo_fumador.joblib"))
        print("Modelo guardado en 'models/modelo_fumador.joblib'")


        with open("metrics/metrics.json", "w") as f:
            json.dump(metrics, f, indent=2)
        print("Métricas guardadas en 'metrics/metrics.json'")


