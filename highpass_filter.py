import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter

def high_gussian_filter(img):
    # image with gaussian
    imgpls = img.filter(ImageFilter.GaussianBlur)
    imgpls=np.asarray(imgpls)
    img=np.asarray(img)
    # subtract the original image from the image with filter to take the filter
    fil=imgpls-img
    # reverse filter
    temp= 1-fil
    # adding the image with the reverse filter
    img1=img+temp
    return img1 