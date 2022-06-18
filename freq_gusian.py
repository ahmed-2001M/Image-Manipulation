import numpy as np
from scipy import misc
import matplotlib.pyplot as plt



pic=misc.face(gray=True).astype('float') #reading the image with all the pixels considered as float values
gauss_pic=ndimage.gaussian_filter(pic,5) #specifying the sigma value of the gaussian filter as 5
plt.imshow(gauss_pic,cmap='gray')