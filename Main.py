#from __future__ import print_function
import sys
#import time
from PIL import Image

im_list = []
for i in range(9):
    im_list.append(Image.open("./Project1Images/" + str(i+1) + ".png"))
    #opens all images as new image objects, images must be stored in the /Project1Images/ directory, and must be named #.png, for numbers 1-9
    
height, width = im_list[0].size
#finds size of the images

im_final = Image.new("RGB", (height, width), color=0)
#creates new image for the program to output to

list_of_pixels = []
i = 0
#initializes a list to hold pixels and a variable to iterate through that list later

#loop for obtaining the RGB data from each image
for x in range (0, (height - 1)):
    for y in range (0, (width - 1)):
        for once in range (0,1):
            p_l_r = [im_list[0].getpixel((x,y))[0], im_list[1].getpixel((x,y))[0], im_list[2].getpixel((x,y))[0], im_list[3].getpixel((x,y))[0], im_list[4].getpixel((x,y))[0], im_list[5].getpixel((x,y))[0], im_list[6].getpixel((x,y))[0], im_list[7].getpixel((x,y))[0], im_list[8].getpixel((x,y))[0]] 
            p_l_g = [im_list[0].getpixel((x,y))[1], im_list[1].getpixel((x,y))[1], im_list[2].getpixel((x,y))[1], im_list[3].getpixel((x,y))[1], im_list[4].getpixel((x,y))[1], im_list[5].getpixel((x,y))[1], im_list[6].getpixel((x,y))[1], im_list[7].getpixel((x,y))[1], im_list[8].getpixel((x,y))[1]] 
            p_l_b = [im_list[0].getpixel((x,y))[2], im_list[1].getpixel((x,y))[2], im_list[2].getpixel((x,y))[2], im_list[3].getpixel((x,y))[2], im_list[4].getpixel((x,y))[2], im_list[5].getpixel((x,y))[2], im_list[6].getpixel((x,y))[2], im_list[7].getpixel((x,y))[2], im_list[8].getpixel((x,y))[2]] 
            #gets the R/G/B value for the given pixel of the x,y coord. in the loop and puts each into into a list containing the same color info from all images
            
            p_l_r.sort()
            p_l_g.sort()
            p_l_b.sort()
            #sorts each list from low to high
            
        list_of_pixels.append((p_l_r[5], p_l_g[5], p_l_b[5]))
        #appends to the list list_of_pixels a tuple for the median RGB values for the given x,y
        p_l_r = []
        p_l_g = []
        p_l_b = []
        #clears out each of the RGB lists for the next iteration of the loop
        
#loop for placing the the pixels on the new image        
for x in range (0, (height - 1)):
    for y in range (0, (width - 1)):
        for once in range (0,1):
            im_final.putpixel((x, y), (list_of_pixels[i]))
            #places pixel at x,y using the given index for the tuple that contains the RGB info
            i = i + 1
            #iterates to the next tuple in the list for the next iteration of the loop
            
im_final.save("Final.png")
#saves the combined image as final.png