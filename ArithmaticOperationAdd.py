
#function name :
from ctypes import addressof
import numpy as np


def Addition(original,constant = 0):

    temp = np.zeros(original.shape).astype(np.uint8)
    # the first for loob which catch the row:
    for i in range (len(original)):
        
        # the second for loob which catch the column:
        for j in range (len(original[0])):
            
            #we put the current point matrix in a varible:
            pixel = original[i,j]
            
            #Adding a constant :
            if ((255 - pixel[0])>constant)  :
                red =pixel[0]+ constant
            else :
                red=255
            if ((255 - pixel[1])>constant)  :
                green=pixel[1]+ constant
            else :
                green=255
            if ((255 - pixel[2])>constant)  :
                blue=pixel[2]+ constant
            else :
                blue=255

            temp[i,j] = red , green , blue
            
    return temp
