


#function name :
import numpy as np


def A2(original,min,max):

    temp = np.zeros(original.shape).astype(np.uint8)
    # the first for loob which catch the row:
    for i in range (len(original)):
        
        # the second for loob which catch the column:
        for j in range (len(original[0])):
            
            #we put the current point matrix in a varible:
            pixel = original[i,j]

            #here we condition on the pixel:
            if pixel[0] >= min and pixel[0] <= max :
                pixel = original[i,j]
            else :
                pixel = 0, 0, 0
            
            
            temp[i,j]=pixel
    return temp

