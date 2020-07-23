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

    st.write("""
    # My First ML Web App!

    #### Mohammed Misbahullah Sheriff""")

    head_html = """
    <div style="background-color:#3498DB; padding:10px">
    <h2 style="color:white; text-align:center;">DIABETES PREDICTOR</h2>
    </div>
    """
    st.markdown(head_html, unsafe_allow_html=True)

    p = st.text_input("No. of Pregnancies", "Type Here")
    g = st.text_input("Glucose Level (mg/dL) (eg. 70)", "Type Here")
    bp = st.text_input("Blood Pressure (mmHg) (eg. 70)", "Type Here")
    stk = st.text_input("Skin Thickness (mm) (eg. 30)", "Type Here")
    ins = st.text_input("Insulin Level (IU/mL) (eg. 80)", "Type Here")
    bmi = st.text_input("Body Mass Index (eg. 25)", "Type Here")
    dpf = st.text_input("Diabetes Pedigree Function (eg. 0.55)", "Type Here")
    age = st.text_input("Age (years)", "Type Here")

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


if __name__ == "__main__":
    main()
