import numpy as np




def gray_scale3d(original,byets = 1) :
    
    temp = np.zeros(original.shape).astype(np.uint8)
    
    for i in range(len(original)) :
        for j in range(len(original[0])) :
            
            pixel=original[i,j]
            x = (pixel[0]*.299 + pixel[1]*.587 + pixel[2]*.114) % (2**byets)
            
            temp[i,j]=int(x) , int(x) ,int(x)
    return temp


