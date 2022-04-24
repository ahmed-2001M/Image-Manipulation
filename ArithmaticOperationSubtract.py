import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image
from numpy import asarray

#function name :
# def ArithmaticOperationSubtract(original):
def Subtraction(original):
    img= asarray(original)
    # the first for loob which catch the row:
    s=70
    for i in range (len(img)):
        
        # the second for loob which catch the column:
        for j in range (len(img[0])):
            
            #we put the current point matrix in a varible:
            pixel = img[i,j]
            
            #Adding a constant :
            if pixel[0]>s :
                pixel[0] =pixel [0] - s
            else :
                pixel[0]=0
            
            if pixel[1]>s :
                pixel [1]=pixel [1] - s
            else :
                pixel[1]=0
            
            if pixel[2]>s :
                pixel[2] =pixel [2] - s
            else :
                pixel[2]=0

            img[i,j] = pixel

        return (img)
