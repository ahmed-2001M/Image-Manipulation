from matplotlib import pyplot as plt
import numpy as np
import cv2

def gray_scale2d(src,bytes) :
    img =plt.imread(src)
    hight,width,dt=img.shape
    print(img.shape)

    temp=np.zeros([hight,width])
    print(temp.shape)

    for i in range(len(img)-1) :
        for j in range(len(img[0])-1) :
            pixel=img[i,j]
            temp[i,j]=(pixel[0]*.3 + pixel[1]*.59 + pixel[2]*.11) % (2**bytes)
            
    # print(temp)
            
    return temp



# def gray_scale3d(src,byets) :
#     img =plt.imread(src)
#     hight,width,dt=img.shape
    
#     temp=np.zeros([hight,width,dt])
    
#     for i in range(len(img)-1) :
#         for j in range(len(img[0])-1) :
#             pixel=img[i,j,0]
#             temp[i,j]=pixel,pixel,pixel
            
            
#     return temp

