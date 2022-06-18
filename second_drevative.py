import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
from PIL import Image


def second_div(img):
    temp =np.zeros(img.shape)
    for i in range(1,len(img)-1):
        for j in range (1,len(img[0])-1):
            
            pixel = img[i,j]
            #composite laplasian filter :
            mask = 4*pixel-(img[i+1, j]+ img[i-1, j]+ img[i, j+1]+ img[i, j-1])
            if mask[0] > 200 and mask[1]>200 and mask[2]>200 :
                temp[i,j]=mask
    temp+=img
    temp = temp.astype(np.uint8)
    return temp

