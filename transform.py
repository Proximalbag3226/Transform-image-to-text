#To run this script you need to have the tesseract search engine installed, you can install it in this url: https://github.com/UB-Mannheim/tesseract/wiki
#Then save the engine path 

#Import the librarys
import pytesseract
import cv2

#We need the path of tesseract
pytesseract.pytesseract.tesseract_cmd = input("Enter the path of tesseract executable ").strip()

#Transfrom the image to a grayscale pass the values for transform every part of the image to a value un gray scale according to the configuration
gray_image = cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)
_, transform = cv2.threshold(gray_image, 138, 255, cv2.THRESH_BINARY)

#Show a window with the image 
cv2.imshow("Hi", transform)
cv2.waitKey(0)

#Return the obtain text 
text = pytesseract.image_to_string(transform)
print(text)