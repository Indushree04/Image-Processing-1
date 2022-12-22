#!/usr/bin/env python
# coding: utf-8

# In[1]:


#up sampling
import cv2

image = cv2.imread('apple.png')
print("Size of image before pyrUp: ", image.shape)

image = cv2.pyrUp(image)
print("Size of image after pyrUp: ", image.shape)
cv2.imshow('UpSample', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[2]:


#down sampling
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('apple.png')
print("Size of image before pyrUp: ", image.shape)

image = cv2.pyrDown(image)
print("Size of image after pyrUp: ", image.shape)
cv2.imshow('DownSample', image)
plt.imshow(image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[3]:


#quantization
# Importing Image module from PIL package
from PIL import Image
import PIL

# creating a image object (main image)
im1 = Image.open("panda.jfif")

# quantize a image
im1 = im1.quantize(6)

# to show specified image
im1.show()


# In[ ]:




