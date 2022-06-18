import numpy as np

def _and0(original):
    temp = np.zeros(original.shape).astype(np.uint8)
    
    for i in range(len(original)):
        for j in range(len(original[0])):
            pixel = original[i][j]
            if ((pixel[0]*.299 + pixel[1]*.587 + pixel[2]*.114) and 0):
                temp[i][j] = 255 , 255 ,255
            else :
                temp[i][j] = 0 , 0 , 0
            
    return temp

def _and1(original):
    temp = np.zeros(original.shape).astype(np.uint8)
    
    for i in range(len(original)):
        for j in range(len(original[0])):
            pixel = original[i][j]
            if ((pixel[0]*.299 + pixel[1]*.587 + pixel[2]*.114) and 1):
                temp[i][j] = 255 , 255 ,255
            else :
                temp[i][j] = 0 , 0 , 0
            
    return temp