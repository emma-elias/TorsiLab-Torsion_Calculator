import streamlit as st
import os
import math
from streamlit_pdf_viewer import pdf_viewer
import base64
from pathlib import Path

# Configure page
st.set_page_config(page_title="TORSILAB\Learn", layout="wide")

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


tab1, tab2, = st.tabs(["IMAGE", "VIEW PDF"])

with tab1:
    st.image(os.path.join(os.getcwd(), "static", "Torsion1.png"),caption="Twisted Shaft")
    st.image(os.path.join(os.getcwd(), "static", "Torsion2.jpg"), caption="Solid Circular Shaft")
    st.image(os.path.join(os.getcwd(), "static", "Torsion3.jpg"), caption="Hollow Circular Shaft")
    st.image(os.path.join(os.getcwd(), "static", "Torsion4.jpg"), caption="Real life Torsion applications")
    #st.header("Side-by-Side Images")

with tab2:
#For displaying PDF
    pdf_path = os.path.join(os.getcwd(), "static", "TorsiLab_Torsion_Guide.pdf")
    st.download_button("Download PDF", pdf_path, file_name="TorsiLab_Torsion_Guide.pdf", mime="application/pdf")
    if os.path.exists(pdf_path):
        pdf_viewer(pdf_path)
    else:
        st.error(f"File not found at: {pdf_path}")


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


st.markdown("Click on the links below to learn more about torsion.")
st.video("https://youtu.be/Mc4-9nHOSMg?si=r7csRGeRCTRQ3xI7")
st.video("https://youtu.be/hvcvbPjdU6Y?si=KHmybMY_aAhGUVeA")
st.sidebar.write("App by [Elias](https://www.linkedin.com/in/e-elias/)")