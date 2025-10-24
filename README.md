# Interactive Edge Detection Application

**CS-4218 Introduction to Computer Vision - Assignment 1**

A web-based interactive application for experimenting with edge detection algorithms including Sobel, Laplacian, and Canny edge detectors.

## Project Description

This application provides an intuitive interface to upload images and apply various edge detection algorithms with real-time parameter adjustment. Users can compare the original and edge-detected images side-by-side, helping visualize how different parameters affect edge detection results.

### Supported Algorithms

- **Sobel**: Gradient-based edge detection with adjustable kernel size
- **Laplacian**: Second derivative-based edge detection with adjustable kernel size
- **Canny**: Multi-stage edge detection with adjustable thresholds and Gaussian blur parameters

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- uv (fast Python package installer)

### Installation Steps

1. **Clone the repository**:

```bash
git clone https://github.com/muhammadsaad-dev/edge_detection_cv.git
cd edge-detection-cv
```

2. **Create a virtual environment using uv**:

```bash
uv venv
```

3. **Activate the virtual environment**:

   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**:

```bash
uv sync
```

This will install all dependencies specified in `pyproject.toml` and `uv.lock`.

## How to Run

1. Ensure your virtual environment is activated

2. Run the application:

```bash
streamlit run main.py
```

3. The app will open automatically in your browser at `http://localhost:8501`

## Usage

1. **Upload Image**: Click "Upload an Image" in the sidebar and select a JPG, PNG, or BMP file
2. **Select Algorithm**: Choose from Sobel, Laplacian, or Canny
3. **Adjust Parameters**: Use sliders to modify algorithm parameters in real-time
4. **View Results**: See the edge-detected output alongside the original image
5. **Download**: Save the processed image using the download button

## Project Structure

```
edge-detection-app/
├── main.py              # Streamlit UI application
├── edge_detection.py    # Edge detection algorithm implementations
├── pyproject.toml       # Project configuration and dependencies
├── uv.lock             # Locked dependency versions
├── README.md           # This file
└── .venv/              # Virtual environment (not committed)
```

## Features

✅ Interactive web-based interface  
✅ Real-time parameter adjustment  
✅ Side-by-side image comparison  
✅ Three edge detection algorithms  
✅ Download processed images  
✅ Support for multiple image formats

## Algorithm Parameters

### Sobel

- **Kernel Size**: Controls the size of the Sobel operator (1-31, odd numbers only)

### Laplacian

- **Kernel Size**: Controls the size of the Laplacian kernel (1-31, odd numbers only)

### Canny

- **Lower Threshold**: Lower bound for hysteresis thresholding (0-255)
- **Upper Threshold**: Upper bound for hysteresis thresholding (0-255)
- **Sigma**: Standard deviation for Gaussian blur (0.1-5.0)

## Screenshots

### Canny

![Canny algorithm](screenshots\canny.png)

### Sobel

![Sobel algorithm](screenshots\sobel.png)

### Laplacian

![Laplacian algorithm](screenshots\laplacian.png)

## Author

Muhammad Saad  
0042-BSCS-22
CS-4218 Introduction to Computer Vision

## Acknowledgments

- Course: CS-4218 Introduction to Computer Vision
- Project built using Streamlit, OpenCV, and Python
- Virtual environment managed with uv
