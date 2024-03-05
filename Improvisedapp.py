import streamlit as st
import pickle
import numpy as np

# Load the model and dataframe
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Title of the app with custom CSS styling
st.markdown("""
    <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #2c3e50; /* Change the color to your preferred color */
            text-align: center;
            padding: 20px;
            background-color: #ecf0f1;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .container {
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }
        .input-label {
            font-weight: bold;
            margin-bottom: 10px;
        }
        .output-container {
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .output-label {
            font-weight: bold;
            font-size: 18px;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>Laptop Price Prediction </h1>", unsafe_allow_html=True)

# Create a sidebar for instructions
st.sidebar.markdown("### Instructions")
st.sidebar.markdown("1. Select the brand, operating system, CPU, and other specifications of the laptop.")
st.sidebar.markdown("2. Click on 'Predict' button to see the predicted price.")

# Main content area
with st.container():
    # Dropdowns for user inputs
    st.subheader("Enter Laptop Specifications:")
    
    # Bran
    company = st.selectbox('Brand',df['Company'].unique(), index=None, placeholder="choose brand")
    
    # Operating System
    os = st.selectbox('Operating System', df['OS'].unique(), index=None, placeholder="choose OS")

    # CPU or Processsor
    processor = st.selectbox('CPU', df['Processor'].unique(), index=None, placeholder="Choose processor")
    
    # Laptop type
    type = st.selectbox('Type', df['TypeName'].unique(), index=None, placeholder="choose laptop type")

    # Graphic Card
    graphics = st.selectbox('Graphics', df['VC'].unique(), index=None, placeholder="choose graphic brand")

    # RAM 
    ram = st.selectbox('RAM', [2,4,6,8,12,16,24, 32, 64], index= None, placeholder="choose RAM")
    
    #Touchscreen
    touchscreen = st.selectbox('Touchscreen', df['TS'].unique(), index=None, placeholder="Select 1 for touchscree else 0")

    #Weight
    weight = st.number_input('Weight of the Laptop (kg)', min_value=0.5, max_value=10.0, step=0.5)

    # HDD
    hdd = st.selectbox('HDD (GB)',[0, 128, 256, 512, 1024, 2048], index=None, placeholder="Choose HDD space")

    # SSD
    ssd = st.selectbox('SSD (GB)', [0, 8, 16, 32, 64, 128, 256, 512, 1024], index=None, placeholder="Choose SSD space")

    # IPS Display
    ips = st.selectbox('IPS Display', df['IPS'].unique(), index=None, placeholder="choose 1 for IPS display elso 0")
                       
    # Screen Size
    inches = st.selectbox('Screen Size (inches)', df['Inches'].unique(), index=None, placeholder="choose screen size")
    
    # PPI
    ppi = st.number_input('Pixels Per Inch (PPI)', min_value=50, max_value=1000, step=50)

    # Prediction button
    if st.button('Predict', key='predict_button'):
        query = np.array([company, os, processor, type, graphics, ram, touchscreen, hdd, ssd, ips, inches, weight, ppi])
        query = query.reshape(1, -1)  # Automatically compute the number of columns
        predicted_price = int(np.exp(pipe.predict(query)[0]))
        with st.container():
            st.subheader("Price Prediction Result:")
            st.markdown(f"<p class='output-label'>The predicted price of this configuration is <span style='color: #27ae60;'>{predicted_price} INR</span></p>", unsafe_allow_html=True)
