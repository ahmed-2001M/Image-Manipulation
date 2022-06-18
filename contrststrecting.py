import numpy as np


def contrast_stretching(img):
    temp = np.zeros(img.shape).astype(np.uint8)
    rmx=np.max(img)
    rmn=np.min(img)
    smx = 255
    smn = 0

    for i in range(len(img)) :
        for j in range(len(img[0])) :
            pixel=img[i,j]
            
            pixel=((smx-smn)/(rmx-rmn)) * (pixel-rmn) + smn

            temp[i,j]=pixel
    
    return (temp)