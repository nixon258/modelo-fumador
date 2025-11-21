import pandas as pd

class preporsesardor:

    def __init__(self, df):
        print("Iniciando preprocesamiento")

        df = self.copiardf(df)
        df = self.eliminarColumnas(df)
        df = self.convercionEnDummys(df)
        df = self.EliminarColumDumis(df)
        self.X, self.Y = self.separarX_Y(df)

        print("Preprocesamiento listo")


    def copiardf (self, data):
        print("se realizo copia de seguridad")
        df=data.copy()
        return df
    def eliminarColumnas (self, df):
        print("se realizo eliminar columnas no relevantes para el modelo o con poca relacion")
        df=df.drop(columns=['ID','eyesight(left)', 'eyesight(right)', 'hearing(left)', 'hearing(right)', 'oral', 'dental caries', 'tartar','Cholesterol','LDL','Urine protein','systolic','HDL'])
        return df
    def convercionEnDummys (self, df):
        dfdumy=df.copy()
        gender=pd.get_dummies(dfdumy['gender'])
        gender['Male'] = gender['M'].astype(int)
        gender['Female'] = gender['F'].astype(int)
        print("gender cambiado a dummys")

        dfdumy = pd.concat([dfdumy, gender], axis=1)
        print ("se concateno tabla gender con dfdummy")
        return dfdumy
    def EliminarColumDumis (self, df):
        df = df.drop(['gender','F','M'], axis=1)
        print("se realizo eliminar columnas gender que se convirtia a dummys")
        return df

    def separarX_Y (self, df):
        y=df['smoking']
        x=df.drop('smoking', axis=1)
        print("se realizo separado en 'X' y 'Y'para el modelo ")
        return x,y






