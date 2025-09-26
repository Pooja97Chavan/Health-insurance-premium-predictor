import streamlit as st
import pickle 
st.set_page_config(page_title="Premium Predictor", layout="centered")
st.markdown("""
    <div style="
        background-color:#f9f9f9; 
        padding:20px; 
        border-radius:10px; 
        border:1px solid #ddd; 
        margin-bottom:20px;
    ">
        <h4 style="color:#333; text-align:center;">📝 Enter Your Details</h4>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    age = st.number_input('Age', min_value=0, step=1)
    children = st.number_input('Children', min_value=0, step=1)

with col2:
    bmi = st.number_input('BMI:')
    gender = st.radio("Gender", ['Male', 'Female'])

smoker = st.selectbox("Do you smoke?", ["Yes", "No"])
model = pickle.load(open('model.pkl','rb'))

if st.button('🔮 Predict Premium'):
    gender = 0 if gender=='Male' else 1
    smoker = 0 if smoker=='No' else 1
    X_test = [[age,gender,bmi,children,smoker]]
    yp = str(round(model.predict(X_test)[0],2))
    st.markdown(f"""
        <div style="
            text-align:center; 
            margin-top:20px; 
            padding:20px; 
            background-color:#f0f8ff; 
            border-radius:10px; 
            border:2px solid #4682B4;
        ">
            <p style='font-size:32px; color:#003366; font-weight:bold;'>
                💡 Your Predicted Premium is: {yp}
            </p>
        </div>
    """, unsafe_allow_html=True)