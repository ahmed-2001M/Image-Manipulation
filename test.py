import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
img = Image.open(r"C:\Users\Ahmed\Documents\PYTHON\DIP\retina.jpg")
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

plt.subplot(1,2,1)
plt.imshow(img)
plt.subplot(1,2,2)
plt.imshow(img1)
plt.show()