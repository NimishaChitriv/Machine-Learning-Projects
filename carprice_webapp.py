import pandas as pd 
import datetime 
import xgboost as xgb 
import streamlit as st


import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size : auto;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
  

def main():
    html_temp = """

    <div style = "background-color:#FF8A8A ;padding:16px">
    <h1 style = "color:black;text-align:center;"> Car Price Predictor </h1>
    </div>
    """
    model = xgb.XGBRFRegressor()
    model.load_model('C:\\Users\\Nimisha\\xgb_model.txt') 
  
    

    st.markdown(html_temp,unsafe_allow_html = True)
    st.write(" ")
    st.write(" ")
    st.header("Are you planning to sell your old car?")
    st.subheader("Let's try predicting its price!")
    
    p1 = st.number_input("**What is the current ex-showroom price of the car**",2.5,25.0, step = 0.5)
    
    p2 = st.number_input("**What is the distance completed by the car**", 100, 5000000, step =100)
    
    s1 = st.selectbox(("**Fuel type of the car**"), ('Petrol','Diesel','CNG'))

    if s1 == "Petrol":
        p3 = 0
    elif s1 == "Diesel":
        p3 =1 
    elif s1 == "CNG":
        p3 = 2
        
    s2 = st.selectbox(("**Are you a Dealer or an Individual?**"), ('Dealer','Individual'))

    if s2 == "Dealer":
        p4 = 0
    elif s2 == "Individual":
        p4 = 1
    
    s3 = st.selectbox(("**What is the transmission type?**"), ('Manual','Automatic'))

    if s3 == "Manual":
        p5 = 0
    elif s3 == "Automatic":
        p5 = 1
        
    p6 = st.slider("**Number of owners the car previously had?**", 0, 10)
    
    date_time = datetime.datetime.now()
    
    
    years = st.slider("**In which year was the car purchased?**",1993, date_time.year)
    p7 = date_time.year-years
    
    
    
    data_new = pd.DataFrame({
        'Present_Price':p1,
        'Kms_Driven':p2,
        'Fuel_Type':p3,
        'Seller_Type':p4,
        'Transmission':p5,
        'Owner':p6,
        'Age':p7
    },index=[0]) 
    
    try:
        if st.button("Predict"):
            pred = model.predict(data_new)
            if pred>0:
                st.success("You can sell you car for {:.2f} lakhs".format(pred[0]))
            else:
                st.warning("You cannot sell this car")
     except:
        st.warning("Oops! Something went wrong")
                    
            
        
    
    
     


if __name__ == '__main__':
    add_bg_from_local('bg5.png')  
    main()
   
