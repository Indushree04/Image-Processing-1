#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Adding Noise
import matplotlib.pyplot as plt
from skimage.util import random_noise
fruit=plt.imread("fruit.jpg")

#Add noise to the image
noisy_image=random_noise(fruit)

#show the original
plt.title("Original")
plt.imshow(fruit)
plt.show()

#show noisy image
plt.title("Noisy Image")
plt.imshow(noisy_image)
plt.show()


# In[4]:


#reducing noisy
import matplotlib.pyplot as plt
from skimage.restoration import denoise_tv_chambolle
noisy_image = plt.imread("noise1.jpg")
denoised_image = denoise_tv_chambolle(noisy_image, multichannel = True)
plt.title("original")
plt.imshow(noisy_image)
plt.show()
plt.title("noisy reduced image")
plt.imshow(denoised_image)
plt.show()


# In[7]:


#Reducing Noise while preserving edges
import matplotlib.pyplot as plt
from skimage.restoration import denoise_bilateral
landscape_img = plt.imread("noisy.jfif")
denoised_img = denoise_bilateral(landscape_img, multichannel = True)
plt.title("original")
plt.imshow(landscape_img)
plt.show()
plt.title("DEnoised")
plt.imshow(denoised_img)
plt.show()


# In[ ]:




