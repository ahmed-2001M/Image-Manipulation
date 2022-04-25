
def median_filter(original):
    img = original.tolist()
    for i in range(len(img)):
        for j in range(len(img[0])):
            red =[]
            green = []
            blue = []
            f=0
            for x in range(i-5 , i+5):
                for y in range(j-5 , j+5):
                    if x>=0 and y>=0 and x<len(img) and y<len(img[0]):
                        red.append(img[x][y][0])
                        green.append(img[x][y][1])
                        blue.append(img[x][y][2])
                        f+=1
            if i>=0 and i<len(img) and j>=0 and j<len(img[0]):        
                red.sort()
                green.sort()
                blue.sort()
                original[i][j] = red[len(red)//2] ,green[len(green)//2] ,blue[len(blue)//2 ]
