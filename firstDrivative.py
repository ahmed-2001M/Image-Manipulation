import numpy as np


def st1(img):
    temp = np.zeros(img.shape).astype(np.uint8)
    for i in range (len (img)-1):
        for j in range(len(img[0])-1):
            pixel = img[i][j]

            dif1 =img[i][j+1] - img[i][j]
            dif2 =img[i+1][j] - img[i][j]


            temp[i][j]=np.sqrt((dif1**2)+(dif2**2))
    return temp