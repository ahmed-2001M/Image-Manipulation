from matplotlib import pyplot as plt
import numpy as np
import cv2
from numpy import asarray
from PIL import Image
from io import BytesIO 

def gray_scale2d(original,byets) :
    
    nd_array = asarray(original)
    hight,width,dt=nd_array.shape

    temp=np.zeros([hight,width])
    print(temp.shape)

    for i in range(len(nd_array)-1) :
        for j in range(len(nd_array[0])-1) :
            pixel=nd_array[i,j]
            temp[i,j]=(pixel[0]*.3 + pixel[1]*.59 + pixel[2]*.11) % (2**byets)
            
    res = Image.fromarray(temp.astype(np.uint8), 'L')
    
    return res



# def gray_scale3d(original,byets) :
    
    
#     nd_array = asarray(original)
#     hight,width,dt=nd_array.shape
#     print(nd_array.shape)

#     temp=np.zeros([hight,width,dt])
    
#     for i in range(len(nd_array)-1) :
#         for j in range(len(nd_array[0])-1) :
#             pixel=nd_array[i,j,0]
#             pixel = pixel % byets
#             temp[i,j]=pixel,pixel,pixel
            
#     res = Image.fromarray(temp,"RGB")
    
#     return res

