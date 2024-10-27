import numpy as np
import pickle
import pandas as pd
import streamlit as st 



pickle_in = open("Admission_predict.pkl","rb")
admis_predicter=pickle.load(pickle_in)
#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def admisssion_chance(GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research,Tancet,GATE):
    prediction=admis_predicter.predict([[GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research,Tancet,GATE]])
    prediction=prediction.astype('float64')
    return prediction



def main():
    st.title("ADMISSSION PREDICTOR")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">ADMISSION PREDICTION WEB APP  </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    GRE_Score = st.text_input("GRE Score","Type Here")
    TOEFL_Score = st.text_input("TOEFL_Score","Type Here")
    University_Rating = st.text_input(",University_Rating","Type Here")
    SOP= st.text_input("SOP","Type Here")
    LOR= st.text_input("LOR","Type Here")
    CGPA= st.text_input("CGPA","Type Here")
    Research= st.text_input("Research","Type Here")
    Tancet= st.text_input("Tancet","Type Here")
    GATE=st.text_input("gate score","Type Here")    
    result="YET TO BE PREDICTED"
    result1 = "YET TO BE PREDICTED"
    s=0.000
    if st.button("Predict"):
        result=admisssion_chance(float(GRE_Score),float(TOEFL_Score),float(University_Rating),float(SOP),float(LOR),float(CGPA),float(Research),float(Tancet),float(GATE))
        s=result[0]
        print(s,type(s))
    if(float(s)>=float(0.69)):
        result1="YOU HAVE MORE PROBABBILITY TO GET ADMISSION"
    else:
        result1="ITS LITTLE TOUGH TO GET ADMISSSION IN TOP UNIVERSITIES "
    st.success(result1)
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built BY SUBHASH TEAM")

if __name__=='__main__':
    main()
    