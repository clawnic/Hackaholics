import streamlit as st
import cv2
import numpy as np
from PIL import Image

def brighten_image(img, brightness_factor):
    # Convert BGR image to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Apply brightness adjustment
    img = img * brightness_factor

    # Clip the values to be in the valid range [0, 255]
    img = np.clip(img, 0, 255)

    # Convert back to BGR
    img = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_RGB2BGR)

    return img

st.title("Image Brightening App")

# Sidebar for options
st.sidebar.header("Settings")
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
brightness_factor = st.sidebar.slider("Brightness", 0.1, 3.0, 1.0)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    with col2:
        brightened_image = brighten_image(img_array, brightness_factor)
        st.image(brightened_image, caption='Brightened Image.', use_column_width=True)