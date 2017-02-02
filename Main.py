from __future__ import print_function
import sys
from PIL import Image
from PIL import PixelAccess

im_1 = Image.open("./Project1Images/1.png")
im_2 = Image.open("./Project1Images/2.png")
im_3 = Image.open("./Project1Images/3.png")
im_4 = Image.open("./Project1Images/4.png")
im_5 = Image.open("./Project1Images/5.png")
im_6 = Image.open("./Project1Images/6.png")
im_7 = Image.open("./Project1Images/7.png")
im_8 = Image.open("./Project1Images/8.png")
im_9 = Image.open("./Project1Images/9.png")

for x in range (0, 494):
    for y in range (0, 556):
        for once in range (0,1):
            pixel_list = {im_1(x,y), im_2(x,y),im_3(x,y), im_4(x,y),im_5(x,y), im_6(x,y),im_7(x,y), im_8(x,y), im_9(x,y)}