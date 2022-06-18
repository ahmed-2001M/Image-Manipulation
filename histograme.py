from matplotlib import pyplot as plt
import numpy as np
import collections
import cv2
from PIL import Image
from io import BytesIO 
import matplotlib
import collections




def draw_histo_RGP(original1) :
    fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=90)

    original = cv2.imread(original1)

    img=original.tolist()
    red=[ img[r][j][0] for r in range(len(original)) for j in range(len(original[0])) ]
    red=sorted(red)
    green=[ img[g][j][1] for g in range(len(original)) for j in range(len(original[0])) ]
    green=sorted(green)
    blue=[ img[b][j][2] for b in range(len(original)) for j in range(len(original[0])) ]
    blue=sorted(blue)

    countred = collections.Counter(red)
    countgreen = collections.Counter(green)
    countblue = collections.Counter(blue)
    plt.legend()


    fig.add_subplot(111).plot(countred.keys(),countred.values(),'r', countgreen.keys(),countgreen.values(),'g',countblue.keys(),countblue.values(),'b')
    return fig

