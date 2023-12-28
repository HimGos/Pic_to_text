import pytesseract
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Code Assistant")

st.title("Code Copy Assistant 👨🏽‍💻")

image = st.file_uploader(label="Upload your image.", type=['png', 'jpg'])

if image:
    img = Image.open(image)
    st.image(img, caption="Uploaded Image!",width=350)
    if st.button("Get the text!"):
        st.write("Here is the extracted text...")
        text = pytesseract.image_to_string(image=img)
        st.write(f"{text}")