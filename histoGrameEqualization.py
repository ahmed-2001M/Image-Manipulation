import collections
import itertools
import numpy as np 
def hiso_grame_equalization(original):
    
    
    img=original
    
    red=[ img[r][j][0] for r in range(len(original)) for j in range(len(original[0])) ]
    red=sorted(red)
    green=[ img[r][j][1] for r in range(len(original)) for j in range(len(original[1])) ]
    green=sorted(green)
    blue=[ img[r][j][2] for r in range(len(original)) for j in range(len(original[2])) ]
    blue=sorted(red)
    
    
    m  = len(img)
    n = len(img[0])
    
    l=256
    
    
    
    cred = list(itertools.accumulate(red))
    cgreen = list(itertools.accumulate(green))
    cblue = list(itertools.accumulate(blue))
    
    print(type(cred))
    
    
    cred = [max(0,round((l*x)/(m*n)-1)) for x in cred]
    cgreen = [max(0,round((l*x)/(m*n)-1)) for x in cgreen]
    cblue = [max(0,round((l*x)/(m*n)-1)) for x in cblue]
    
    cred = np.ndarray(cred)
    cgreen = np.ndarray(cgreen)
    cblue = np.ndarray(cblue)
    original = original.astype(np.uint8)
    original = cred , cgreen , cblue
    
    print(type(original))
    return original

    
    # ans = np.array(res,dtype=np.uint8)
    # print(ans)
    # return ans
    
    
