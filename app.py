import streamlit as st
from scripts.predict import predecirFuamdor

def main():
    st.title("🚬 Predicción de Fumador")
    st.write("Ingrese los datos clínicos para evaluar la probabilidad de ser fumador.")

    st.subheader("Datos personales")
    age = st.number_input("Edad", min_value=10, max_value=100, value=40,
                          help="La edad influye porque a mayor edad puede aumentar el riesgo de enfermedades asociadas al fumar.")
    height = st.number_input("Altura (cm)", 100, 220, 175,
                             help="La altura permite calcular IMC y evaluar riesgo cardiovascular.")
    weight = st.number_input("Peso (kg)", 30, 200, 75,
                             help="El peso permite calcular IMC y correlacionarse con riesgos de salud de fumadores.")
    waist = st.number_input("Cintura (cm)", 40, 180, 85,
                            help="La circunferencia abdominal indica riesgo metabólico y cardiovascular, agravado por fumar.")

    st.subheader("Presión arterial")
    systolic = st.number_input("Sistólica", 80, 200, 122,
                               help="La presión sistólica elevada incrementa el riesgo cardiovascular, más aún en fumadores.")
    relaxation = st.number_input("Diastólica", 50, 150, 82,
                                 help="La presión diastólica alta también aumenta riesgo de complicaciones cardíacas.")

    st.subheader("Análisis de sangre")
    fasting_bs = st.number_input("Glucosa en ayunas (mg/dL)", 50, 300, 97,
                                 help="La glucosa alta indica riesgo metabólico y diabetes, que se potencia con fumar.")
    cholesterol = st.number_input("Colesterol", 80, 400, 190,
                                  help="El colesterol alto aumenta riesgo de arteriosclerosis; fumar lo agrava.")
    triglyceride = st.number_input("Triglicéridos", 30, 500, 130,
                                   help="Triglicéridos altos incrementan riesgo cardiovascular y daño arterial en fumadores.")
    hdl = st.number_input("HDL", 10, 120, 55,
                          help="El HDL 'bueno' protege; fumar reduce su efecto positivo.")
    ldl = st.number_input("LDL", 30, 300, 112,
                          help="El LDL 'malo' aumenta riesgo cardíaco; fumar potencia su efecto negativo.")
    hemoglobin = st.number_input("Hemoglobina", 5.0, 20.0, 14.7,
                                 help="La hemoglobina transporta oxígeno; fumar reduce eficiencia respiratoria.")
    urine_protein = st.number_input("Proteína en orina", 0, 5, 1,
                                    help="Indica daño renal; fumar aumenta riesgo de enfermedad renal crónica.")

    serum_creatinine = st.number_input("Creatinina en suero", 0.1, 5.0, 1.1,
                                       help="Evalúa función renal; fumar puede dañarla.")
    ast = st.number_input("AST", 5, 100, 24,
                          help="Enzima hepática; niveles altos indican daño hepático que fumar puede agravar.")
    alt = st.number_input("ALT", 5, 100, 25,
                          help="Otra enzima hepática relacionada con la salud del hígado.")
    gtp = st.number_input("GTP", 5, 200, 27,
                          help="Indicador de función hepática, afectada por fumar.")

    genero = st.radio("Género", ["Male", "Female"],
                      help="El género puede influir en patrones de fumar y susceptibilidad a enfermedades.")
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
