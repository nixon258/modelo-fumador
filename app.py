import streamlit as st
from scripts.predict import predecirFuamdor

def main():
    st.title("🚬 Predicción de Fumador")
    st.write("Ingrese los datos clínicos para evaluar la probabilidad de ser fumador.")

    st.subheader("Datos personales")
    age = st.number_input(
        "Edad", min_value=10, max_value=100, value=40,
        help="Edad: A mayor edad, mayor riesgo acumulado de enfermedades relacionadas con fumar.\nRangos: 10-30: Bajo riesgo, 31-60: Medio riesgo, 61+: Alto riesgo"
    )
    height = st.number_input(
        "Altura (cm)", 100, 220, 175,
        help="Altura: Se utiliza para calcular IMC y riesgo cardiovascular.\nRangos típicos: Hombre 160-185, Mujer 150-175"
    )
    weight = st.number_input(
        "Peso (kg)", 30, 200, 75,
        help="Peso: Permite calcular IMC.\nRangos IMC: <18.5 Bajo peso, 18.5-24.9 Normal, 25-29.9 Sobrepeso, 30+ Obesidad"
    )
    waist = st.number_input(
        "Cintura (cm)", 40, 180, 85,
        help="Cintura: Indica riesgo metabólico.\nRangos riesgo: Hombre <94 normal, 94-102 moderado, >102 alto. Mujer <80 normal, 80-88 moderado, >88 alto."
    )

    st.subheader("Presión arterial")
    systolic = st.number_input(
        "Sistólica", 80, 200, 122,
        help="Presión sistólica: elevada incrementa riesgo cardiovascular.\nRangos: <120 Normal, 120-129 Elevada, 130-139 Hipertensión grado 1, 140+ Hipertensión grado 2"
    )
    relaxation = st.number_input(
        "Diastólica", 50, 150, 82,
        help="Presión diastólica: elevada aumenta riesgo cardíaco.\nRangos: <80 Normal, 80-89 Elevada, 90+ Hipertensión"
    )

    st.subheader("Análisis de sangre")
    fasting_bs = st.number_input(
        "Glucosa en ayunas (mg/dL)", 50, 300, 97,
        help="Glucosa en ayunas: niveles altos indican riesgo de diabetes.\nRangos: <100 Normal, 100-125 Prediabetes, 126+ Diabetes"
    )
    cholesterol = st.number_input(
        "Colesterol total", 80, 400, 190,
        help="Colesterol total: niveles altos incrementan riesgo cardiovascular.\nRangos: <200 Normal, 200-239 Límite, 240+ Alto"
    )
    triglyceride = st.number_input(
        "Triglicéridos", 30, 500, 130,
        help="Triglicéridos: altos aumentan riesgo de arteriosclerosis.\nRangos: <150 Normal, 150-199 Límite, 200-499 Alto, 500+ Muy alto"
    )
    hdl = st.number_input(
        "HDL", 10, 120, 55,
        help="HDL (bueno): protege corazón. Valores bajos aumentan riesgo.\nRangos: Hombre <40 bajo, Mujer <50 bajo, 40-60/50-60 normal, >60 óptimo"
    )
    ldl = st.number_input(
        "LDL", 30, 300, 112,
        help="LDL (malo): altos niveles aumentan riesgo cardíaco.\nRangos: <100 óptimo, 100-129 Casi óptimo, 130-159 Límite, 160-189 Alto, 190+ Muy alto"
    )
    hemoglobin = st.number_input(
        "Hemoglobina", 5.0, 20.0, 14.7,
        help="Hemoglobina: transporta oxígeno; fumar puede reducir eficacia.\nRangos: Hombre 13.8-17.2, Mujer 12.1-15.1 g/dL"
    )
    urine_protein = st.number_input(
        "Proteína en orina", 0, 5, 1,
        help="Proteína en orina: indica posible daño renal. Fumar aumenta riesgo.\nRangos: 0 Normal, 1-2 Leve, 3+ Alto"
    )

    serum_creatinine = st.number_input(
        "Creatinina en suero", 0.1, 5.0, 1.1,
        help="Creatinina: evalúa función renal.\nRangos: Hombre 0.74-1.35, Mujer 0.59-1.04 mg/dL"
    )
    ast = st.number_input(
        "AST", 5, 100, 24,
        help="AST: enzima hepática, niveles altos indican daño. Fumar agrava hígado.\nRangos: 10-40 U/L"
    )
    alt = st.number_input(
        "ALT", 5, 100, 25,
        help="ALT: enzima hepática.\nRangos: 7-56 U/L"
    )
    gtp = st.number_input(
        "GTP", 5, 200, 27,
        help="GTP: función hepática.\nRangos: Hombre 8-61, Mujer 5-36 U/L"
    )

    genero = st.radio(
        "Género", ["Male", "Female"],
        help="El género puede influir en patrones de fumar y susceptibilidad a enfermedades."
    )
    male = 1 if genero == "Male" else 0
    female = 1 if genero == "Female" else 0

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
        predictor = predecirFuamdor()
        resultado, prob = predictor.predecir(datos)
        st.success(f"Resultado: **{resultado}**")
        st.info(f"Probabilidad: **{prob:.2%}**")

if __name__ == "__main__":
    main()
