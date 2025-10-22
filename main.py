import cv2
import numpy as np
import streamlit as st
import edge_detection  # contains sobel_detection, laplacian_detection, canny_detection

st.set_page_config(page_title="🧠 Edge Detection Visualizer", layout="wide")

# ---- Title ----
st.title("🧠 Interactive Edge Detection Visualizer")

# ---- Upload Image ----
uploaded = st.file_uploader(
    "📤 Upload an image (JPG, JPEG, PNG, BMP)", 
    type=["jpg", "jpeg", "png", "bmp"]
)

# ---- Sidebar Controls ----
st.sidebar.header("⚙️ Controls")

if uploaded:
    # Decode uploaded image
    file_bytes = np.asarray(bytearray(uploaded.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    # ---- Algorithm Selection ----
    algo = st.sidebar.radio(
        "🧩 Select Edge Detection Algorithm:",
        ("Sobel", "Laplacian", "Canny")
    )

    # ---- Algorithm-specific Parameters ----
    params = {}
    if algo == "Sobel":
        params["ksize"] = st.sidebar.slider("Kernel Size (odd number)", 1, 7, 3, step=2)
        direction = st.sidebar.selectbox("Gradient Direction", ("X", "Y", "Both"), index=2)
        params["direction"] = direction

    elif algo == "Laplacian":
        params["ksize"] = st.sidebar.slider("Kernel Size (odd number)", 1, 7, 3, step=2)

    elif algo == "Canny":
        params["lower"] = st.sidebar.slider("Lower Threshold", 0, 255, 50)
        params["upper"] = st.sidebar.slider("Upper Threshold", 0, 255, 150)
        params["aperture"] = st.sidebar.selectbox("Aperture Size", (3, 5, 7), index=1)
        params["sigma"] = st.sidebar.slider("Gaussian Sigma", 0.0, 5.0, 1.0)

    apply_button = st.sidebar.button("🖼️ Apply / Update")

    # ---- Apply Algorithm ----
    if apply_button or algo != "Canny":  # Canny can auto-refresh quickly
        if algo == "Sobel":
            # Custom Sobel with direction
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            if params["direction"] == "X":
                sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=params["ksize"])
                result = cv2.convertScaleAbs(sobelx)
            elif params["direction"] == "Y":
                sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=params["ksize"])
                result = cv2.convertScaleAbs(sobely)
            else:
                result = edge_detection.sobel_detection(img, cv2.CV_64F, params["ksize"])

        elif algo == "Laplacian":
            result = edge_detection.laplacian_detection(img, params["ksize"])

        elif algo == "Canny":
            result = edge_detection.canny_detection(
                img, params["lower"], params["upper"], params["aperture"], params["sigma"]
            )

        # ---- Display Images Side by Side ----
        st.subheader(f"🔍 {algo} Edge Detection Result")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🖼️ Original Image")
            st.image(img, channels="BGR", use_container_width=True)
        with col2:
            st.markdown(f"### 🧾 {algo} Output")
            st.image(result, channels="GRAY", use_container_width=True)
else:
    st.info("📥 Please upload an image to start experimenting with edge detection.")
