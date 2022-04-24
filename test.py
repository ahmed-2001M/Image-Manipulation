from matplotlib import pyplot as plt
import numpy as np
from numpy import asarray
from PIL import Image
from gray_sacle import gray_scale3d



img = Image.open(r"C:\Users\Ahmed\Documents\PYTHON\DIP\tr.png")
res = gray_scale3d(img)


res.show()