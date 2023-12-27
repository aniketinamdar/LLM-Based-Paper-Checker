import pytesseract 
from PIL import Image
import numpy as np
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\ANIKET INAMDAR\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

def pytesseract_ocr(img):
    print(pytesseract.image_to_string(img))

# def grayscale_image(img):
#     return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# def remove_noise(img):
#     return cv2.medianBlur(img,5)

# def thresholding(img):
#     return cv2.threhsold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]


image_link = 'images/work2.jpg'
# image_link = grayscale_image(image_link)
# image_link = thresholding(image_link)
# image_link = remove_noise(image_link)

pytesseract_ocr(Image.open(image_link))
# print(pytesseract.get_languages(config=''))
