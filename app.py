## Importing required libraries
import streamlit as st
import pickle

## Title of the page
st.title("Student Score Predictor")

## Loading the models
regressor = pickle.load(open('Models/ridge.pkl','rb'))
scaler = pickle.load(open('Models/scaler.pkl','rb'))

## Taking the inputs on the home page
hours_studied = st.number_input(label="Enter the Hours Studied:" ,min_value=0,step=1,max_value=24)
previous_score = st.number_input(label="Enter the previous test score:",min_value=0,step=1,max_value=100)
activity = st.text_input(label="Are you involved in extra curricular activities:").lower().strip()
if activity == "yes":
    activities = 1
else:
    activities = 0
sample_paper = st.number_input(label="Enter the number of ques papers solved:",min_value=0,step=1,max_value=15)
sleep_hours = st.number_input(label="Enter the number of sleep hours:",min_value=0,step=1,max_value=24)

## Prediction of the Score
predicted_score = regressor.predict(scaler.transform([[hours_studied,previous_score,activities,sample_paper,sleep_hours]]))

## Display score when the button is pressed
st.button("Predict Score",on_click=lambda: st.write('Your predicted score is : ',predicted_score[0]),type='secondary',icon=":material/online_prediction:")
