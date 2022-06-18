import numpy as np

def Threshold (original,constant = 1) :

    temp = np.zeros(original.shape).astype(np.uint8)
    
    for i in range(len(original)) :
        for j in range(len(original[0])) :
            pixel = original[i,j]
            pixel = (pixel[0]*.299 + pixel[1]*.587 + pixel[2]*.114)
            
            if(pixel>constant) :
                pixel=255,255,255
            else :
                pixel=0,0,0
            temp[i,j]=pixel
    return temp




