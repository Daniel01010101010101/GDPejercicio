import streamlit as st
import requests

# Configurar la página con título e icono
st.set_page_config(page_title="Consulta de API para Modelo de Adultos", page_icon="🤖", layout="wide")

# Aplicar estilos personalizados con fondo azul
st.markdown(
    """
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #ADD8E6;
        }
        .title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            color: #4A90E2;
        }
        .subtitle {
            font-size: 24px;
            text-align: center;
            color: #333;
        }
        .stMarkdown img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 200px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Mostrar una imagen de un robot bailando
st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnVlbXpwY2cxazgzc29qc3kxaGplbWx3c3k4ZG9pcHFwa21xdW41cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pIMlKqgdZgvo4/giphy.gif", use_container_width=False)

# Título de la aplicación
st.markdown("<p class='title'>Consulta de API para Modelo de Adultos</p>", unsafe_allow_html=True)

# Subtítulo
st.markdown("<p class='subtitle'>Optimizada con mejoras visuales</p>", unsafe_allow_html=True)

# Función para realizar la solicitud POST a la API
def realizar_solicitud_post(url, data):
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, response.text
    except Exception as e:
        return False, str(e)

# Formulario para introducir los datos requeridos por la API
with st.form("api_form"):
    age = st.number_input("Edad", min_value=1, value=21)
    workclass = st.selectbox("Clase de trabajo", ["Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov", "Local-gov", "State-gov", "Without-pay", "Never-worked"])
    fnlwgt = st.number_input("fnlwgt", value=346478)
    education = st.selectbox("Educación", ["Bachelors", "Some-college", "11th", "HS-grad", "Prof-school", "Assoc-acdm", "Assoc-voc", "9th", "7th-8th", "12th", "Masters", "1st-4th", "10th", "Doctorate", "5th-6th", "Preschool"])
    education_num = st.number_input("Número de educación", min_value=1, max_value=16, value=10)
    marital_status = st.selectbox("Estado civil", ["Married-civ-spouse", "Divorced", "Never-married", "Separated", "Widowed", "Married-spouse-absent", "Married-AF-spouse"])
    occupation = st.selectbox("Ocupación", ["Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial", "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct", "Adm-clerical", "Farming-fishing", "Transport-moving", "Priv-house-serv", "Protective-serv", "Armed-Forces"])
    relationship = st.selectbox("Relación", ["Wife", "Own-child", "Husband", "Not-in-family", "Other-relative", "Unmarried"])
    race = st.selectbox("Raza", ["White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "Black"])
    sex = st.selectbox("Sexo", ["Male", "Female"])
    capital_gain = st.number_input("Ganancia de capital", value=4000)
    capital_loss = st.number_input("Pérdida de capital", value=0)
    hours_per_week = st.number_input("Horas por semana", min_value=1, max_value=168, value=45)
    native_country = st.text_input("País de origen", value="United-States")

    submitted = st.form_submit_button("Enviar")

    if submitted:
        datos_json = {
            'age': age,
            'workclass': workclass,
            'fnlwgt': fnlwgt,
            'education': education,
            'education-num': education_num,
            'marital-status': marital_status,
            'occupation': occupation,
            'relationship': relationship,
            'race': race,
            'sex': sex,
            'capital-gain': capital_gain,
            'capital-loss': capital_loss,
            'hours-per-week': hours_per_week,
            'native-country': native_country
        }

        url = 'https://gdpejercicio-production.up.railway.app/adults_model/'

        exito, respuesta = realizar_solicitud_post(url, datos_json)

        if exito:
            st.success(f'Solicitud exitosa. Respuesta: {respuesta}')
        else:
            st.error(f'Error en la solicitud: {respuesta}')
