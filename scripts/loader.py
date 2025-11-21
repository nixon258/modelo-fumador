import pandas as pd

class Loader:
    def __init__(self, ruta):
        self.ruta = ruta

    def loadDB(self):
        print("========== CARGANDO BASE DE DATOS ==========")
        data = pd.read_csv(self.ruta)
        print("========== BASE DE DATOS CARGADA ==========")
        return data