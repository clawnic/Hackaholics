
import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt

def dark_channel_prior(img, size=15):
    """Compute the dark channel prior of an image."""
    # Compute the minimum value over a window for each channel
    min_img = cv2.erode(img, np.ones((size, size), np.uint8))
    dark_channel = np.min(min_img, axis=2)
    return dark_channel

def estimate_airlight(img, dark_channel, percentile=0.001):
    """Estimate the airlight from the image based on the dark channel."""
    flat_dark = dark_channel.flatten()
    threshold = int(len(flat_dark) * percentile)
    brightest_pixels = np.argpartition(-flat_dark, threshold)[:threshold]
    airlight = np.max(img.reshape(-1, 3)[brightest_pixels], axis=0)
    return airlight

def dehaze(img, airlight, omega=0.95, t0=0.1):
    """Perform the dehazing operation on the image."""
    img = img.astype(np.float64)  # Convert to float for calculations
    transmission = 1 - omega * dark_channel_prior(img / airlight)
    transmission = np.maximum(transmission, t0)  # Avoid division by zero
    dehazed = np.zeros_like(img)
    for i in range(3):  # Dehaze each channel separately
        dehazed[:, :, i] = (img[:, :, i] - airlight[i]) / transmission + airlight[i]
    return np.clip(dehazed, 0, 255).astype(np.uint8)

# Streamlit app
st.title("Image Dehazing App")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    hazy_img = cv2.imdecode(file_bytes, 1)

    # Sliders for parameters
    omega = st.slider("Omega (for transmission estimation)", 0.0, 1.0, 0.95, 0.05)
    t0 = st.slider("t0 (minimum transmission)", 0.0, 1.0, 0.1, 0.05)
    patch_size = st.slider("Patch Size (for dark channel prior)", 5, 25, 15, 2)

    # Compute dark channel prior
    dark_channel = dark_channel_prior(hazy_img, size=patch_size)

    # Estimate airlight
    airlight = estimate_airlight(hazy_img, dark_channel)

    # Perform dehazing
    dehazed_img = dehaze(hazy_img, airlight, omega=omega, t0=t0)

    # Display images
    st.image(cv2.cvtColor(hazy_img, cv2.COLOR_BGR2RGB), caption='Hazy Image', use_column_width=True)
    st.image(cv2.cvtColor(dehazed_img, cv2.COLOR_BGR2RGB), caption='Dehazed Image', use_column_width=True)