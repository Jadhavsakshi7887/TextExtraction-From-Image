import pytesseract
from PIL import Image, ImageOps
import cv2
import numpy as np
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_path = r"C:\Users\Dell\Downloads\Task1-20241116T111717Z-001\Task1\capchas (1).jpeg"

if os.path.exists(image_path):
    img = Image.open(image_path)

    grayscale_img = ImageOps.grayscale(img)

    open_cv_image = np.array(grayscale_img)

    thresholded_img = cv2.adaptiveThreshold(open_cv_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    blurred_img = cv2.GaussianBlur(thresholded_img, (5, 5), 0)

    kernel = np.ones((3, 3), np.uint8)
    dilated_img = cv2.dilate(blurred_img, kernel, iterations=1)

    thresholded_pil_image = Image.fromarray(dilated_img)

    text = pytesseract.image_to_string(thresholded_pil_image, config='--psm 6')

    text = " ".join(text.split())

    print(f"Extracted Text: {text}")
else:
    print("The image path is invalid or the file doesn't exist.")
