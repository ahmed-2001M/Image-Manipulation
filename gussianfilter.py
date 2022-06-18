from PIL import ImageFilter
import numpy as np

def gussian_filter(img):
    img = img.filter(ImageFilter.GaussianBlur)
    temp = np.asarray(img)
    return temp