import pytesseract
import cv2 as cv
import string
chars= string.digits
count = 0 
for c in chars:
    img = cv.imread(f"chars/character_{c}.png")
    ocr_result= pytesseract.image_to_string(img,config='--psm 10')
    if(ocr_result.strip()!=c):
        print(c," Extracted text: ",ocr_result)
    else:
        count+=1
print("Accuracy",count/26)