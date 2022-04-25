

#function name :
def A1(original,min,max):


    for i in range (len(original)):
        
        # the second for loob which catch the column:
        for j in range (len(original[0])):
            
            #we put the current point matrix in a varible:
            pixel = original[i,j]

            #here we condition on the pixel:
            if pixel[0] >= min and pixel[0] <= max :
                pixel = 255
            
            else :
                pixel = 0
            
            original[i,j]=pixel


