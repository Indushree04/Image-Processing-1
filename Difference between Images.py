#!/usr/bin/env python
# coding: utf-8

# In[2]:


#find differnce between images
# import module
import matplotlib.pyplot as plt
from PIL import Image, ImageChops

# assign images
img1 = Image.open("diff1.jpg")
plt.imshow(img1)
plt.show()
img2 = Image.open("diff2.jpg")
plt.imshow(img2)
plt.show()

# finding difference
diff = ImageChops.difference(img1, img2)
plt.imshow(diff)
plt.show()


# In[1]:


# Importing ImageDraw for
# using floodfill function
from PIL import Image, ImageDraw

# Opening the image and
# converting its type to RGBA
img = Image.open("tottenham.jpg").convert('RGBA')

# Location of seed
seed = (0, 0)

# Pixel Value which would
# be used for replacement
rep_value = (50, 50, 100, 100)

# Calling the floodfill() function and
# passing it image, seed, value and
# thresh as arguments
ImageDraw.floodfill(img, seed, rep_value, thresh = 100)

img.show()


# In[ ]:




