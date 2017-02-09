#from __future__ import print_function
import sys
#import time
from PIL import Image

im_list = []
for i in range(9):
    im_list.append(Image.open("./Project1Images/" + str(i+1) + ".png"))

height, width = im_list[0].size

im_final = Image.new("RGB", (height, width), color=0)

list_of_pixels = []
i = 0

for x in range (0, (height - 1)):
    for y in range (0, (width - 1)):
        for once in range (0,1):
            p_l_r = [im_list[0].getpixel((x,y))[0], im_list[1].getpixel((x,y))[0], im_list[2].getpixel((x,y))[0], im_list[3].getpixel((x,y))[0], im_list[4].getpixel((x,y))[0], im_list[5].getpixel((x,y))[0], im_list[6].getpixel((x,y))[0], im_list[7].getpixel((x,y))[0], im_list[8].getpixel((x,y))[0]] 
            p_l_g = [im_list[0].getpixel((x,y))[1], im_list[1].getpixel((x,y))[1], im_list[2].getpixel((x,y))[1], im_list[3].getpixel((x,y))[1], im_list[4].getpixel((x,y))[1], im_list[5].getpixel((x,y))[1], im_list[6].getpixel((x,y))[1], im_list[7].getpixel((x,y))[1], im_list[8].getpixel((x,y))[1]] 
            p_l_b = [im_list[0].getpixel((x,y))[2], im_list[1].getpixel((x,y))[2], im_list[2].getpixel((x,y))[2], im_list[3].getpixel((x,y))[2], im_list[4].getpixel((x,y))[2], im_list[5].getpixel((x,y))[2], im_list[6].getpixel((x,y))[2], im_list[7].getpixel((x,y))[2], im_list[8].getpixel((x,y))[2]] 

            p_l_r.sort()
            p_l_g.sort()
            p_l_b.sort()
            
        list_of_pixels.append((p_l_r[5], p_l_g[5], p_l_b[5]))
        p_l_r = []
        p_l_g = []
        p_l_b = []
        
for x in range (0, (height - 1)):
    for y in range (0, (width - 1)):
        for once in range (0,1):
            im_final.putpixel((x, y), (list_of_pixels[i]))
            i = i + 1
            
im_final.save("Final.png")