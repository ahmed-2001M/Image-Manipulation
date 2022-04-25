
def Avg_filter(original):
    for i in range(len(original)):
        for j in range(len(original[0])):
            red =0
            green = 0
            blue = 0
            f=0
            for x in range(i-3 , i+3):
                for y in range(j-3 , j+3):
                    if x>=0 and y>=0 and x<len(original) and y<len(original[0]):
                        red+=original[x][y][0]
                        green+=original[x][y][1]
                        blue+=original[x][y][2]
                        f+=1
            if i>=0 and i<len(original) and j>=0 and j<len(original[0]):        
                original[i][j] = red / f , green / f , blue / f
