import streamlit as st
import os
import math

import time
from streamlit_pdf_viewer import pdf_viewer
import base64
from pathlib import Path

# Configure page
st.set_page_config(page_title="TORSILAB\Home", layout="wide")
# st.sidebar.title("Navigation Bar")
# st.sidebar.divider()

#Define your local image path
image_path = Path(r"C:\Users\elias\my_python_project\logo.png")

#Read the image and encode it to base64
try:
    img_bytes = image_path.read_bytes()
    encoded_img = base64.b64encode(img_bytes).decode()
    img_data_uri = f"data:image/png;base64,{encoded_img}"
except FileNotFoundError:
    img_data_uri = ""
    st.error(f"Could not find the logo at: {image_path}")

#Render the tight widget container with a border
if img_data_uri:
    with st.container():
        st.markdown(
            f"""
            <div style="
                display: flex; 
                align-items: center; 
                width: fit-content;
                padding: 15px 20px; 
                border: 4px solid #D97757; 
                border-radius: 20px;
                background-color: #8c8376;
            ">
                <img src="{img_data_uri}" style="height: 8rem; margin-right: 12px;">
                <span style="font-size: 1.5rem; font-weight: 700; letter-spacing: -0.5px;"></span>
            </div>
            """,
            unsafe_allow_html=True
        )

#
# #You can use this for a pop up on your web app.
# st.toast("JIIIII")
# st.spinner("HIIII")

#Import a Google Font and apply artistic CSS
st.markdown(
    """
    <style>
    @import url('https://googleapis.com');

    .artistic-title {
        font-family: sans serif;
        font-size: 3.5rem;
        font-weight: 700;
        font-style: italic;
        text-align: center;
        background: linear-gradient(45deg, #FF4B4B, #FF8E53, #FE6B8B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 2px 4px 10px rgba(0,0,0,0.15);
        margin-bottom: 0px;
    }

    .artistic-subtitle {
        font-family: sans serif;
        font-text-align: center;
        font-size: 1.2rem;
        text-align: center;
        color: #555555;
        letter-spacing: 1.5px;
        margin-top: -10px;
        margin-bottom: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
#Render the stylized title
st.markdown('<h1 class="artistic-title">TORSILAB</h1>', unsafe_allow_html=True)
st.markdown('<p class="artistic-subtitle">INTERACTIVE TORSION CALCULATOR</p>', unsafe_allow_html=True)



with st.container(border=True):
    st.write("Torsion is the twisting moment that circular shaft experiences when subjected to shear stress. "
              "Torsion is evident in our daily lives and its applications in industries is vast - from rotating automotive components to even medical devices. "
             "A human body experiences torsion in the muscles.")

# with st.sidebar:
#     with st.spinner("Loading sidebar details..."):
#         time.sleep(2)


with st.sidebar.container():
    st.sidebar.caption("This app is under constant development. If you are a fan and want to be notified and follow our next update, consider dropping your details with us.")
    with st.sidebar.form(key = "fan_info_form"):
        st.write("Please enter your details")
        name=st.text_input("Name")
        email=st.text_input("Email")
        submit_button=st.form_submit_button("Submit")
        if submit_button:
            if not name or not email:
                st.warning("⚠️ Oops! Your details are not complete")
            else:
                st.success("✅ Thank You!")



st.sidebar.write("App by [Elias](https://www.linkedin.com/in/e-elias/)")