import pytesseract 
from PIL import Image
import numpy as np
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\ANIKET INAMDAR\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

def pytesseract_ocr(img):
    print(pytesseract.image_to_string(img))


pytesseract_ocr(Image.open('images/test2.png'))
