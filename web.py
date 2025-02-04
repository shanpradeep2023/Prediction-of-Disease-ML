import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Desease Outbreaks',layout='wide',page_icon='⚕️')

# diabetes_model = pickle.load(open(r"C:\Users\shanp\Documents\PRADEEP\Learning\ML\training\diabetes_model.sav",'rb'))
# heart_model = pickle.load(open(r"C:\Users\shanp\Documents\PRADEEP\Learning\ML\training\heart_model.sav",'rb'))
# parkinsons_model = pickle.load(open(r"C:\Users\shanp\Documents\PRADEEP\Learning\ML\training\parkinsons_model.sav",'rb'))

diabetes_model = pickle.load(open(r"training\diabetes_model.sav",'rb'))
heart_model = pickle.load(open(r"training\heart_model.sav",'rb'))
parkinsons_model = pickle.load(open(r"training\parkinsons_model.sav",'rb'))

with st.sidebar:
    selected = option_menu('Prediction od disease outbreak systems',['Diabetes Prediction','Heart desease Prediction','Parkinsons Prediction'],menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
    with col2:
        Glucose=st.text_input('Glucose level')
    with col3:
        BloodPressure=st.text_input('Blood Pressure value')
    with col1:
        SkinThickness=st.text_input('Skin Thickness value')
    with col2:
        Insulin=st.text_input('Insulin level')
    with col3:
        BMI=st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function')
    with col2:
        Age=st.text_input('Age')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
    # Check if all inputs are entered
        if '' in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]:
            diab_diagnosis = 'Enter values'
        else:
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            user_input = [float(x) for x in user_input]
            diab_prediction = diabetes_model.predict([user_input])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'Person is Diabetic'
            else:
                diab_diagnosis = 'Person is not Diabetic'
        st.success(diab_diagnosis)



elif selected == 'Heart desease Prediction':
    st.title('Heart desease Prediction using ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        age = st.text_input('Age of the patient')
    with col2:
        sex = st.selectbox('Sex of the patient', ['Male', 'Female'])
    with col3:
        cp = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'])
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl')
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['Yes', 'No'])
    with col1:
        restecg = st.selectbox('Resting Electrocardiogram Results', ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'])
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])
    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise Relative to Rest')
    with col2:
        slope = st.selectbox('Slope of the peak exercise ST segment', ['Upsloping', 'Flat', 'Downsloping'])
    with col3:
        ca = st.selectbox('Number of major vessels colored by fluoroscopy', ['0', '1', '2', '3', '4'])
    with col1:
        thalassemia = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])

    # Mapping categorical inputs to numbers based on dataset
    sex_map = {'Male': 1, 'Female': 0}
    cp_map = {'Typical Angina': 1, 'Atypical Angina': 2, 'Non-Anginal Pain': 3, 'Asymptomatic': 4}
    fbs_map = {'Yes': 1, 'No': 0}
    restecg_map = {'Normal': 0, 'ST-T Wave Abnormality': 1, 'Left Ventricular Hypertrophy': 2}
    exang_map = {'Yes': 1, 'No': 0}
    slope_map = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
    thalassemia_map = {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2}

    heart_diagnosis = ''

    # Button to predict
    if st.button('Heart Disease Test Result'):
        # Check if all numerical fields are entered
        if '' in [age, trestbps, chol, thalach, oldpeak]:
            heart_diagnosis = 'Enter all values'
        else:
            try:
                # Convert inputs to correct format
                user_input = [
                    float(age),
                    sex_map[sex],
                    cp_map[cp],
                    float(trestbps),
                    float(chol),
                    fbs_map[fbs],
                    restecg_map[restecg],
                    float(thalach),
                    exang_map[exang],
                    float(oldpeak),
                    slope_map[slope],
                    int(ca),
                    thalassemia_map[thalassemia]
                ]

                # Predict using the model
                heart_prediction = heart_model.predict([user_input])

                if heart_prediction[0] == 1:
                    heart_diagnosis = 'Person has Heart Disease'
                else:
                    heart_diagnosis = 'Person does not have Heart Disease'
            except:
                heart_diagnosis = "Error in input values"

        st.success(heart_diagnosis)


elif selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction using ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        name = st.text_input("Name")  # Name is not used for prediction
    with col2:
        MDVP_Fo_Hz = st.text_input("MDVP: Fundamental Frequency (Fo) in Hz")
    with col3:
        MDVP_Fhi_Hz = st.text_input("MDVP: Highest Fundamental Frequency (Fhi) in Hz")
    with col1:
        MDVP_Flo_Hz = st.text_input("MDVP: Lowest Fundamental Frequency (Flo) in Hz")
    with col2:
        MDVP_Jitter = st.text_input("MDVP: Jitter (%)")
    with col3:
        MDVP_Jitter_Abs = st.text_input("MDVP: Absolute Jitter")
    with col1:
        MDVP_RAP = st.text_input("MDVP: Relative Amplitude Perturbation (RAP)")
    with col2:
        MDVP_PPQ = st.text_input("MDVP: Point Period Perturbation Quotient (PPQ)")
    with col3:
        Jitter_DDP = st.text_input("Jitter: DDP (Difference of Difference Periods)")
    with col1:
        MDVP_Shimmer = st.text_input("MDVP: Shimmer (%)")
    with col2:
        MDVP_Shimmer_dB = st.text_input("MDVP: Shimmer (dB)")
    with col3:
        Shimmer_APQ3 = st.text_input("Shimmer: Amplitude Perturbation Quotient (APQ3)")
    with col1:
        Shimmer_APQ5 = st.text_input("Shimmer: Amplitude Perturbation Quotient (APQ5)")
    with col2:
        MDVP_APQ = st.text_input("MDVP: Amplitude Perturbation Quotient")
    with col3:
        Shimmer_DDA = st.text_input("Shimmer: DDA (Difference of Difference Amplitudes)")
    with col1:
        NHR = st.text_input("Noise-to-Harmonics Ratio (NHR)")
    with col2:
        HNR = st.text_input("Harmonics-to-Noise Ratio (HNR)")
    with col3:
        RPDE = st.text_input("Recurrence Period Density Entropy (RPDE)")
    with col1:
        DFA = st.text_input("Detrended Fluctuation Analysis (DFA)")
    with col2:
        spread1 = st.text_input("Spread 1 (non-linear measures)")
    with col3:
        spread2 = st.text_input("Spread 2 (non-linear measures)")
    with col1:
        D2 = st.text_input("Correlation Dimension (D2)")
    with col2:
        PPE = st.text_input("Pitch Period Entropy (PPE)")

    # Mapping the 'status' field (convert categorical to numeric)
    status_map = {'0 (Healthy)': 0, '1 (Parkinson’s)': 1}
    with col3:
        status = st.selectbox("Status (Parkinson’s Disease)", ["0 (Healthy)", "1 (Parkinson’s)"])

    parkinsons_diagnosis = ''

    # Button to predict
    if st.button("Parkinson's Disease Test Result"):
        # Check if all numerical fields are entered
        input_fields = [
            MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP,
            MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5,
            MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE
        ]
        
        if '' in input_fields:
            parkinsons_diagnosis = "Enter all values"
        else:
            try:
                # Convert inputs to float
                user_input = [
                    float(MDVP_Fo_Hz), float(MDVP_Fhi_Hz), float(MDVP_Flo_Hz), float(MDVP_Jitter),
                    float(MDVP_Jitter_Abs), float(MDVP_RAP), float(MDVP_PPQ), float(Jitter_DDP),
                    float(MDVP_Shimmer), float(MDVP_Shimmer_dB), float(Shimmer_APQ3), float(Shimmer_APQ5),
                    float(MDVP_APQ), float(Shimmer_DDA), float(NHR), float(HNR), float(RPDE),
                    float(DFA), float(spread1), float(spread2), float(D2), float(PPE)
                ]

                # Predict using the model
                parkinsons_prediction = parkinsons_model.predict([user_input])

                if parkinsons_prediction[0] == 1:
                    parkinsons_diagnosis = "Person has Parkinson's Disease"
                else:
                    parkinsons_diagnosis = "Person does not have Parkinson's Disease"
            except:
                parkinsons_diagnosis = "Error in input values"

        st.success(parkinsons_diagnosis)
    
                            
                                              
    
