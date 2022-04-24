import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image

#function name :
def ArithmaticOperationSubtract(PATH):
    original = cv.imread(r'{PATH}')   
    constant =70
    # the first for loob which catch the row:
    for i in range (len(original)):
        
        # the second for loob which catch the column:
        for j in range (len(original[0])):
            
            #we put the current point matrix in a varible:
            pixel = original[i,j]
            
            #Adding a constant :
            if ((255 - pixel[0])>constant)  :
                pixel[0] =pixel[0]+ constant
            else :
                pixel[0]=255
            if ((255 - pixel[1])>constant)  :
                pixel [1]=pixel[1]+ constant
            else :
                pixel[1]=255
            if ((255 - pixel[2])>constant)  :
                pixel [2]=pixel[2]+ constant
            else :
                pixel[2]=255

            original[i,j] = pixel
    

    return Image.fromarray(original)