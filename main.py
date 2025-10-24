import streamlit as st
import cv2
import numpy as np


# Set page configuration
st.set_page_config(
    page_title="Interactive Edge Detection",
    layout="wide"
)

# Title
st.title("Interactive Edge Detection Application")
st.markdown("### CS-4218 Computer Vision - Assignment 1")

# Initialize session state for the uploaded image
if 'original_image' not in st.session_state:
    st.session_state.original_image = None

# File uploader
uploaded_file = st.file_uploader(
    "Upload an image (JPG, PNG, BMP)",
    type=['jpg', 'jpeg', 'png', 'bmp']
)

if uploaded_file is not None:
    # Read and convert the uploaded image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    original_image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    st.session_state.original_image = original_image

# Only show the interface if an image is uploaded
if st.session_state.original_image is not None:
    original_image = st.session_state.original_image
    
    # Sidebar for algorithm selection and parameters
    st.sidebar.header("Edge Detection Settings")
    
    # Algorithm selection
    algorithm = st.sidebar.selectbox(
        "Select Edge Detection Algorithm",
        ["Sobel", "Laplacian", "Canny"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.subheader(f"{algorithm} Parameters")
    
    # Algorithm-specific parameters
    if algorithm == "Canny":
        lower_threshold = st.sidebar.slider(
            "Lower Threshold",
            min_value=0,
            max_value=255,
            value=50,
            step=5
        )
        upper_threshold = st.sidebar.slider(
            "Upper Threshold",
            min_value=0,
            max_value=255,
            value=150,
            step=5
        )
        kernel_size = st.sidebar.slider(
            "Kernel Size (for Gaussian blur)",
            min_value=3,
            max_value=15,
            value=5,
            step=2
        )
        sigma = st.sidebar.slider(
            "Sigma (Gaussian blur)",
            min_value=0.1,
            max_value=5.0,
            value=1.4,
            step=0.1
        )
        
        # Apply Canny edge detection
        gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (kernel_size, kernel_size), sigma)
        edges = cv2.Canny(blurred, lower_threshold, upper_threshold)
        
    elif algorithm == "Sobel":
        kernel_size = st.sidebar.slider(
            "Kernel Size",
            min_value=1,
            max_value=7,
            value=3,
            step=2
        )
        gradient_direction = st.sidebar.radio(
            "Gradient Direction",
            ["Both (X and Y)", "X Direction", "Y Direction"]
        )
        
        # Apply Sobel edge detection
        gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        
        if gradient_direction == "X Direction":
            edges = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=kernel_size)
            edges = np.absolute(edges)
        elif gradient_direction == "Y Direction":
            edges = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=kernel_size)
            edges = np.absolute(edges)
        else:  # Both directions
            sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=kernel_size)
            sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=kernel_size)
            edges = np.sqrt(sobel_x**2 + sobel_y**2)
        
        # Normalize to 0-255 range
        edges = np.uint8(255 * edges / np.max(edges))
        
    elif algorithm == "Laplacian":
        kernel_size = st.sidebar.slider(
            "Kernel Size",
            min_value=1,
            max_value=31,
            value=3,
            step=2
        )
        
        # Apply Laplacian edge detection
        gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Laplacian(gray, cv2.CV_64F, ksize=kernel_size)
        edges = np.absolute(edges)
        # Normalize to 0-255 range
        edges = np.uint8(255 * edges / np.max(edges))
    
    # Display images side by side
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Input Image")
        # Convert BGR to RGB for display
        original_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
        st.image(original_rgb, use_container_width=True)
    
    with col2:
        st.subheader(f"Output Image ({algorithm})")
        st.image(edges, use_container_width=True, clamp=True)
    
    # Display current parameter values
    st.sidebar.markdown("---")
    st.sidebar.info(f"**Currently using:** {algorithm} edge detection")

else:
    st.info("👆 Please upload an image to begin edge detection")
    st.markdown("""
    ### Supported Algorithms:
    - **Sobel**: Gradient-based edge detection (X, Y, or both directions)
    - **Laplacian**: Second derivative-based edge detection
    - **Canny**: Multi-stage edge detection with hysteresis thresholding
    
    ### Features:
    - Real-time parameter adjustment
    - Side-by-side comparison of original and processed images
    - Support for JPG, PNG, and BMP formats
    """)