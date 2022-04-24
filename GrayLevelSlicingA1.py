from tkinter import Image
from numpy import asarray
from matplotlib import pyplot as plt
import cv2 as cv
from PIL import Image

#function name :
def A1(original):

    max=255
    min=150
    img = asarray(original)
    # the first for loob which catch the row:
    for i in range (len(img)):
        
        # the second for loob which catch the column:
        for j in range (len(img[0])):
            
            #we put the current point matrix in a varible:
            pixel = img[i,j]

            #here we condition on the pixel:
            if pixel[0] >= min and pixel[0] <= max :
                pixel = 255
            
            else :
                pixel = 0
            
            img[i,j]=pixel
    original= Image.fromarray(img)
    #finally we return the new image :
    return(original)
