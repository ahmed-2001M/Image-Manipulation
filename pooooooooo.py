from numpy import asarray
from matplotlib import pyplot as plt
import cv2 as cv
from PIL import Image

img =plt.imread(r'C:\\Users\\Ahmed\\Documents\\PYTHON\DIP\\tr2.jpg')
img1 =plt.imread(r'C:\\Users\\Ahmed\\Documents\\PYTHON\DIP\\tr2.jpg')
#def nd(img):
temp = img
for i in range(1,len(img)-1):
    for j in range (1,len(img[0])-1):
        
        pixel = img[i,j]
        #composite laplasian filter :
        red = -5*pixel[0] + (img[i+1, j,0]+ img[i-1, j,0]+ img[i, j+1,0]+ img[i, j-1,0]) 
        green = -5*pixel[1] + (img[i+1, j,1]+ img[i-1, j,1]+ img[i, j+1,1]+ img[i, j-1,1])
        blue = -5*pixel[2] + (img[i+1, j,2]+ img[i-1, j,2]+ img[i, j+1,2]+ img[i, j-1,2])
        print(red)
        temp[i,j]=red , green , blue

#return(img)
plt.subplot(1,2,1)
plt.imshow(temp)
plt.subplot(1,2,2)
plt.imshow(img1)
plt.show()