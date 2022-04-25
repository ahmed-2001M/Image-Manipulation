

# def gray_scale2d(original,byets = 1) :
    
#     nd_array = asarray(original)
#     hight,width,dt=nd_array.shape

#     temp=np.zeros([hight,width])

#     for i in range(len(nd_array)-1) :
#         for j in range(len(nd_array[0])-1) :
#             pixel=nd_array[i,j]
#             temp[i,j]=(pixel[0]*.299 + pixel[1]*.587 + pixel[2]*.114) % (2**byets)
            
#     res = Image.fromarray(temp.astype(np.uint8), 'L')
    
#     return res



def gray_scale3d(original,byets = 1) :
    

    for i in range(len(original)) :
        for j in range(len(original[0])) :
            pixel=original[i,j,0]
            pixel = pixel % (2**byets)
            original[i,j]=pixel,pixel,pixel
            


