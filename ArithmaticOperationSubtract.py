
#function name :
# def ArithmaticOperationSubtract(original):
def Subtraction(original,constant = 0):

    # the first for loob which catch the row:
    for i in range (len(original)):
        
        # the second for loob which catch the column:
        for j in range (len(original[0])):
            
            #we put the current point matrix in a varible:
            pixel = original[i,j]
            
            #Adding a constant :
            if pixel[0]>constant :
                pixel[0] =pixel [0] - constant
            else :
                pixel[0]=0
            
            if pixel[1]>constant :
                pixel [1]=pixel [1] - constant
            else :
                pixel[1]=0
            
            if pixel[2]>constant :
                pixel[2] =pixel [2] - constant
            else :
                pixel[2]=0

            original[i,j] = pixel
