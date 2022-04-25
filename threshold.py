

def Threshold (original,constant = 0) :


    for i in range(len(original)) :
        for j in range(len(original[0])) :
            pixel=original[i][j][0]
            
            if(pixel>constant) :
                pixel=255,255,255
            else :
                pixel=0,0,0
            original[i,j]=pixel
            




