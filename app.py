import streamlit as st
import pickle
import numpy as np

# Load the model and dataframe
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Title of the app
st.title("Laptop Price Predictor")

# Dropdowns for user inputs
company = st.selectbox('Brand', df['Company'].unique(), index=0)

os = st.selectbox('OS', df['OS'].unique())
processor = st.selectbox('CPU', df['Processor'].unique())
type = st.selectbox('Type', df['TypeName'].unique())
graphics = st.selectbox('Graphics', df['VC'].unique())
ram = st.selectbox('RAM', df['Ram'].unique())

touchscreen = st.selectbox('Touchscreen',df['TS'].unique())
weight = st.number_input('Weight of the Laptop')

hdd = st.selectbox('HDD', df['HDD'].unique())
ssd = st.selectbox('SSD', df['SSD'].unique())
ips = st.selectbox('IPS',df['IPS'].unique())

inches = st.selectbox('Screen Size', df['Inches'].unique())
ppi=st.selectbox('PPi', df['PPI'].unique())

# Prediction button
if st.button('Predict Price'):
    query = np.array([company, os, processor, type, graphics, ram, touchscreen, weight,hdd, ssd, ips, inches,ppi])
    query = query.reshape(1, 13)  # Automatically compute the number of columns
    predicted_price = int(np.exp(pipe.predict(query)[0]))
    st.text(f"The predicted price of this configuration is {predicted_price}INR")