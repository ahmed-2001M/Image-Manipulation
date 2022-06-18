
import numpy as np


def min_filter(original):
    temp = np.zeros(original.shape).astype(np.uint8)
    const = 3
    img = original.tolist()
    for i in range(len(img)):
        for j in range(len(img[0])):
            red =[]
            green = []
            blue = []
            f=0
            for x in range(i-const , i+const):
                for y in range(j-const , j+const):
                    if x>=0 and y>=0 and x<len(img) and y<len(img[0]):
                        red.append(img[x][y][0])
                        green.append(img[x][y][1])
                        blue.append(img[x][y][2])
                        f+=1
            if i>=0 and i<len(img) and j>=0 and j<len(img[0]):        
                red.sort()
                green.sort()
                blue.sort()
                temp[i][j] = np.min(red) ,np.min(green) , np.min(blue)
    return temp
