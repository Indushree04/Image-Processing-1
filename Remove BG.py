#!/usr/bin/env python
# coding: utf-8

# In[21]:


#Remove BG
import cv2
from PIL import Image,ImageDraw,ImageFilter
im1=Image.open('im2.jpg')
im2=Image.open('baloon.jfif')
mask_im=Image.new("L",im2.size,0)
draw=ImageDraw.Draw(mask_im)
draw.ellipse((20,11,200,200),fill=225)
mask_im_blur=mask_im.filter(ImageFilter.GaussianBlur(10))
back_im=im1.copy()
back_im.paste(im2,(0,0),mask_im_blur)
back_im.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

