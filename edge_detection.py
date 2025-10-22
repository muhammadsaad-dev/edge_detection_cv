import cv2

import cv2
import numpy as np

def sobel_detection(img, ddepth, ksize):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Always compute gradients in float64 (to make cv2.magnitude happy)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=ksize)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=ksize)

    # Magnitude of gradients
    sobel_combined = cv2.magnitude(sobelx, sobely)

    # Convert to 8-bit for display
    sobel_combined = cv2.convertScaleAbs(sobel_combined)

    # If user selected a specific depth (e.g., CV_16S or CV_8U), convert accordingly
    if ddepth != cv2.CV_64F:
        sobel_combined = cv2.convertScaleAbs(
            sobel_combined.astype(np.float64), alpha=1.0
        )

    return sobel_combined


def laplacian_detection(img, ksize):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F, ksize=ksize)
    laplacian = cv2.convertScaleAbs(laplacian)
    return laplacian

def canny_detection(img, lower, upper, aperture, sigma):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), sigma)
    edges = cv2.Canny(blurred, lower, upper, apertureSize=aperture, L2gradient=True)
    return edges