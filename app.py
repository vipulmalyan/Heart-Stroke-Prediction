import streamlit as st
import pandas as pd
import pickle
import joblib

st.set_page_config(layout="wide")

# Load the scaler object
scaler_path = 'scaler.pkl'
with open(scaler_path, 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Load the trained models
dt_path = 'dt.sav'

dt_model = joblib.load(dt_path)


st.title('Heart Stroke Prediction App')

st.sidebar.header('User Input Features')

# Collect user input features
gender = st.sidebar.radio('Gender', ('Male', 'Female'))
age = st.sidebar.slider('Age', 0, 100, 25)
hypertension = st.sidebar.checkbox('Hypertension')
heart_disease = st.sidebar.checkbox('Heart Disease')
ever_married = st.sidebar.radio('Ever Married', ('Yes', 'No'))
work_type = st.sidebar.selectbox('Work Type', ('Private', 'Self-employed', 'Govt_job', 'Children', 'Never_worked'))
residence_type = st.sidebar.radio('Residence Type', ('Urban', 'Rural'))
avg_glucose_level = st.sidebar.number_input('Average Glucose Level', min_value=0.0, max_value=300.0, value=100.0)
bmi = st.sidebar.number_input('BMI', min_value=0.0, max_value=100.0, value=25.0)
smoking_status = st.sidebar.selectbox('Smoking Status', ('formerly smoked', 'never smoked', 'smokes', 'Unknown'))

# Encode categorical variables
gender = 1 if gender == 'Male' else 0
ever_married = 1 if ever_married == 'Yes' else 0
work_type = ['Private', 'Self-employed', 'Govt_job', 'Children', 'Never_worked'].index(work_type)
residence_type = 1 if residence_type == 'Urban' else 0
smoking_status = ['formerly smoked', 'never smoked', 'smokes', 'Unknown'].index(smoking_status)

# Create a DataFrame with user input
user_input = pd.DataFrame({'gender': gender, 'age': age, 'hypertension': hypertension, 'heart_disease': heart_disease,
                           'ever_married': ever_married, 'work_type': work_type, 'Residence_type': residence_type,
                           'avg_glucose_level': avg_glucose_level, 'bmi': bmi, 'smoking_status': smoking_status},
                          index=[0])

# Standardize user input features
user_input_std = scaler.transform(user_input)

if st.button('Predict'):
    dt_prediction = dt_model.predict(user_input_std)

    st.subheader('Prediction Results:')
    st.write('You have been diagnosed with Heart Stroke Risk.' if dt_prediction[0] == 1 else 'You have been diganosed with no Heart Stroke Risk. Congratulations!')



hide_st_style = '''
<style> footer {visibility: hidden;} 
</style>
'''
st.markdown(hide_st_style, unsafe_allow_html=True)


footer_html = """
<style>
.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    color: white; /* Text color */
    padding: 10px;
    text-align: center; /* Center the text */
    font-size: 18px; /* Adjust the font size */
}
</style>
<div class="footer">Made by Vipul Malyan</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://raw.githubusercontent.com/vipulmalyan/Heart-Stroke-Prediction/main/image-from-rawpixel-id-10235756-jpeg.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
