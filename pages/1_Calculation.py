import streamlit as st
import os
import math

import time
from streamlit_pdf_viewer import pdf_viewer
import base64
from pathlib import Path

# Configure page
st.set_page_config(page_title="TORSILAB\Calculation", layout="wide")

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

with st.spinner("Creating your experience...", show_time=True):
    time.sleep(2)

st.caption("Click on the shaft type below to select")
form1, form2 =st.tabs(["SOLID SHAFT", "HOLLOW SHAFT"]) #This creates two tabs and makes it easy to navigate
entries={
    "shaft_diameter": None,
    "shaft_length": None,
    "twist_angle": None,
    "shear_stress": None,
    "torque": None,
    "power_transmitted": None,
    "shaft_outer_diameter": None,
    "shaft_inner_diameter": None,
}



#Submit Buttons
buttons={
    "torsion":None,
    "polar_moment":None,
}

#form1 and form2 representing the Solid and Hollow shafts respectively.

with form1:
    with st.form(key="SOLIDSHAFT"):
        col1, col2 = st.columns([4,1])
        with col1:
            entries["shaft_diameter"] = st.number_input("Shaft Diameter")
        with col2:
            diameter_unit = st.selectbox("Units", ["mm", "cm", "m"])
        entries["shaft_length"] = st.number_input("Shaft Length")
        entries["twist_angle"] = st.select_slider("Twist Angle", options=range(10))
        col3, col4 = st.columns([4,1])
        with col3:
            entries["shear_stress"] = st.number_input("Shear Stress")
        with col4:
            stress_unit = st.selectbox("Select Unit", ["N/mm^2", "N/m^2", "Pa", "Bar"])
        entries["torque"] = st.number_input("Torque")
        entries["power_transmitted"] = st.number_input("Power Transmitted")

        # The math for solid Shaft
        torsion = math.pi / 16 * entries["shaft_diameter"] ** 3 * entries["shear_stress"]
        polar_moment_of_inertia = math.pi / 32 * entries["shaft_diameter"] ** 4

        # These buttons submit the form and gives the answer
        buttons["torsion"] = st.form_submit_button("Torsion")
        st.write("Torsion:", torsion)
        buttons["polar_moment"] = st.form_submit_button("Polar Moment of Inertia")
        st.write("Polar Moment of Inertia:", polar_moment_of_inertia)


#For Hollow Shaft
with form2:
    with st.form(key="HOLLOW SHAFT"):
        entries["shaft_outer_diameter"] = st.number_input("Shaft Outer Diameter")
        entries["shaft_inner_diameter"]=st.number_input("Shaft Inner Diameter")
        diameter_unit = st.selectbox("Units", ["mm", "cm", "m"])
        entries["shaft_length"] = st.number_input("Shaft Length")
        entries["twist_angle"] = st.select_slider("Twist Angle", options=[range(0,10)])
        entries["shear_stress"] = st.number_input("Shear Stress")
        stress_unit = st.selectbox("Select Unit", ["N/mm^2", "N/m^2", "Pa", "Bar"])
        entries["torque"] = st.number_input("Torque")
        entries["power_transmitted"] = st.number_input("Power Transmitted")

        # The math for the hollow Shaft
        torsion = math.pi / 16 * entries["shaft_diameter"] ** 3 * entries["shear_stress"]
        polar_moment_of_inertia = math.pi / 32 * (entries["shaft_outer_diameter"] ** 4-entries["shaft_inner_diameter"]**4)

        # These buttons submit the form and gives the answer
        buttons["torsion"] = st.form_submit_button("Torsion")
        st.write("Torsion:", torsion)
        buttons["polar_moment"] = st.form_submit_button("Polar Moment of Inertia")
        st.write("Polar Moment of Inertia:", polar_moment_of_inertia)


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