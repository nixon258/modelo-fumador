import streamlit as st
from modules.predecirFumador import predecirFumador

def main():

    st.title("🚬 Predicción de Fumador")
    st.write("Ingrese los datos clínicos para evaluar la probabilidad de ser fumador.")

    st.subheader("Datos personales")
    age = st.number_input("Edad", min_value=10, max_value=100, value=40)
    height = st.number_input("Altura (cm)", 100, 220, 175)
    weight = st.number_input("Peso (kg)", 30, 200, 75)
    waist = st.number_input("Cintura (cm)", 40, 180, 85)

    st.subheader("Presión arterial")
    systolic = st.number_input("Sistólica", 80, 200, 122)
    relaxation = st.number_input("Diastólica", 50, 150, 82)

    st.subheader("Análisis de sangre")
    fasting_bs = st.number_input("Glucosa en ayunas (mg/dL)", 50, 300, 97)
    cholesterol = st.number_input("Colesterol", 80, 400, 190)
    triglyceride = st.number_input("Triglicéridos", 30, 500, 130)
    hdl = st.number_input("HDL", 10, 120, 55)
    ldl = st.number_input("LDL", 30, 300, 112)
    hemoglobin = st.number_input("Hemoglobina", 5.0, 20.0, 14.7)
    urine_protein = st.number_input("Proteína en orina", 0, 5, 1)

    serum_creatinine = st.number_input("Creatinina en suero", 0.1, 5.0, 1.1)
    ast = st.number_input("AST", 5, 100, 24)
    alt = st.number_input("ALT", 5, 100, 25)
    gtp = st.number_input("GTP", 5, 200, 27)

    genero = st.radio("Género", ["Male", "Female"])
    male = 1 if genero == "Male" else 0
    female = 1 if genero == "Female" else 0

    # Diccionario EXACTO para el modelo
    datos = {
        "age": age,
        "height(cm)": height,
        "weight(kg)": weight,
        "waist(cm)": waist,
        "systolic": systolic,
        "relaxation": relaxation,
        "fasting blood sugar": fasting_bs,
        "Cholesterol": cholesterol,
        "triglyceride": triglyceride,
        "HDL": hdl,
        "LDL": ldl,
        "hemoglobin": hemoglobin,
        "Urine protein": urine_protein,
        "serum creatinine": serum_creatinine,
        "AST": ast,
        "ALT": alt,
        "Gtp": gtp,
        "Male": male,
        "Female": female
    }

    if st.button("Predecir"):
        predictor = predecirFumador()
        resultado, prob = predictor.predecir(datos)

        st.success(f"Resultado: **{resultado}**")
        st.info(f"Probabilidad: **{prob:.2%}**")

if __name__ == "__main__":
    main()
