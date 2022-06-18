import numpy as np


def power_low(img,const):

    gamma_corrected=np.array(255*(img/255)**const,dtype=np.uint8)
        
        
    print(gamma_corrected.shape)

    return gamma_corrected