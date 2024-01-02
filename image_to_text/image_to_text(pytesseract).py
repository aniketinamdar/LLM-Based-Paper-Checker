import pytesseract
from PIL import Image
import numpy as np
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\ANIKET INAMDAR\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

def pytesseract_ocr(img):
    text = pytesseract.image_to_string(img) 
    print(text)

image_link = 'images/test2.png'  
image = cv2.imread(image_link)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
pytesseract_ocr(image)