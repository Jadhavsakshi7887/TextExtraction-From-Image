import pytesseract
from PIL import Image, ImageOps
import cv2
import numpy as np
import os

# Set the path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Define the path to the image
image_path = r"C:\Users\Dell\Downloads\Task1-20241116T111717Z-001\Task1\capchas (1).jpeg"

# Check if the image exists at the given path
if os.path.exists(image_path):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to grayscale
    grayscale_img = ImageOps.grayscale(img)

    # Convert to numpy array
    open_cv_image = np.array(grayscale_img)

    # Apply adaptive thresholding (better for images with varying brightness)
    thresholded_img = cv2.adaptiveThreshold(open_cv_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    # Apply Gaussian Blur to remove noise
    blurred_img = cv2.GaussianBlur(thresholded_img, (5, 5), 0)

    # Perform dilation to connect broken characters
    kernel = np.ones((3, 3), np.uint8)
    dilated_img = cv2.dilate(blurred_img, kernel, iterations=1)

    # Convert back to PIL image for pytesseract
    thresholded_pil_image = Image.fromarray(dilated_img)

    # Extract text from the processed image
    text = pytesseract.image_to_string(thresholded_pil_image, config='--psm 6')

    # Remove unwanted newlines and extra spaces, print the text in one line
    text = " ".join(text.split())

    # Print the extracted text
    print(f"Extracted Text: {text}")
else:
    print("The image path is invalid or the file doesn't exist.")
