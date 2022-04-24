import numpy as np
from PIL import Image

def Threshold (original) :

    img = np.array(original)
    for i in range(len(img)) :
        for j in range(len(img[0])) :
            pixel=img[i][j][0]
            
            if(pixel>155) :
                pixel=255,255,255
            else :
                pixel=0,0,0
            img[i,j]=pixel
            
    res = Image.fromarray(img)
    return res



