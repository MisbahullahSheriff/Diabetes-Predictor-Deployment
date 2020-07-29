import streamlit as st
import numpy as np
import pickle

clf = pickle.load(open("diabetes_model.pkl", "rb"))


def predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, Bmi, DiabetesPedigreeFunction, Age):
    p = int(Pregnancies)
    g = float(Glucose)
    bp = float(BloodPressure)
    stk = float(SkinThickness)
    ins = float(Insulin)
    bmi = float(Bmi)
    dpf = float(DiabetesPedigreeFunction)
    age = int(Age)

    data = np.array([[p, g, bp, stk, ins, bmi, dpf, age]])

    prediction = clf.predict(data)[0]

    return prediction


def main():

    st.title("Diabetes Prediction ML Web App")
    st.subheader("@author: Mohammed Misbahullah Sheriff")

    head_html = """
    <div style="background-color:#3498DB; padding:10px">
    <h2 style="color:white; text-align:center;">DIABETES PREDICTOR</h2>
    </div>
    """
    st.markdown(head_html, unsafe_allow_html=True)

    p = st.text_input("No. of Pregnancies", "0")
    if int(p) > 15:
        raise ValueError("No. of Pregnancies: Given input beyond limit")
    elif int(p) < 0:
        raise ValueError("No. of Pregnancies: Value must be non-negative")

    g = st.text_input("Glucose Level (mg/dL)", "70")
    if float(g) > 350:
        raise ValueError("Glucose Level: Given input beyond limit")
    elif float(g) < 0:
        raise ValueError("Glucose Level: Value must be non-negative")

    bp = st.text_input("Blood Pressure (mm Hg)", "85")
    if float(bp) > 300:
        raise ValueError("Blood Pressure: Given input beyond limit")
    elif float(bp) < 0:
        raise ValueError("Blood Pressure: Value must be non-negative")

    stk = st.text_input("Skin Thickness (mm)", "30")
    if float(stk) > 120:
        raise ValueError("Skin Thickness: Given input beyond limit")
    elif float(stk) < 0:
        raise ValueError("Skin Thickness: Value must be non-negative")

    ins = st.text_input("Insulin Level (mIU/mL)", "80")
    if float(ins) > 500:
        raise ValueError("Insulin Level: Given input beyond limit")
    elif float(ins) < 0:
        raise ValueError("Insulin Level: Value must be non-negative")

    bmi = st.text_input("Body Mass Index", "25")
    if float(bmi) > 100:
        raise ValueError("Body Mass Index: Given input beyond limit")
    elif float(bmi) < 0:
        raise ValueError("Body Mass Index: Value must be non-negative")

    dpf = st.text_input("Diabetes Pedigree Function", "0.5")
    if float(dpf) > 10:
        raise ValueError(
            "Diabetes Pedigree Function: Given input beyond limit")
    elif float(dpf) < 0:
        raise ValueError(
            "Diabetes Pedigree Function: Value must be non-negative")

    age = st.text_input("Age (years)", "30")
    if int(age) > 120:
        raise ValueError("Age: Given input beyond limit")
    elif int(age) < 0:
        raise ValueError("Age: Value must be non-negative")

    safe_html = """
    <div style="background-color:#1D8348; padding:10px">
    <h2 style="color:white; text-align:center;">You don't have diabetes! &#128512;</h2>
    </div>
    """

    unsafe_html = """
    <div style="background-color:#CB4335; padding:10px">
    <h2 style="color:white; text-align:center;">You have diabetes. &#128577;</h2>
    </div>
    """

    if st.button("PREDICT"):
        output = predict_diabetes(p, g, bp, stk, ins, bmi, dpf, age)
        st.success("Data Processed")

        if output == 1:
            st.markdown(unsafe_html, unsafe_allow_html=True)
        else:
            st.markdown(safe_html, unsafe_allow_html=True)

    if st.button("LOOK ME UP"):
        st.info(
            "LinkedIn: https://www.linkedin.com/in/mohammed-misbahullah-sheriff-b684091a1")
        st.success("GitHub: https://github.com/MisbahullahSheriff")


if __name__ == "__main__":
    main()
