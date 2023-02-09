#!/usr/bin/env python
# coding: utf-8

# In[8]:


#segmentation
import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage.color import label2rgb

face_image=plt.imread('face1.jpg')

#obtain the segmentation with 400 regions
segments=slic(face_image,n_segments=400)

#Put segments on top of original image to compare
segmented_image=label2rgb(segments,face_image,kind='avg')

#show the original 
plt.title("Original")
plt.imshow(face_image.astype('uint8'))
plt.show()

#show the resulting image
plt.title("Segmented Image")
plt.imshow(segmented_image.astype('uint8'))
plt.show()


# In[11]:


#Contouring shapes
def show_image_contour(image, contours):
    plt.figure()
    for n, contour in enumerate(contours):
        plt.plot(contour[:,1], contour[:, 0], linewidth= 3)
    plt.imshow(image, interpolation = 'nearest', cmap= 'gray_r')
    plt.title("contours")
    plt.axis("off")


# In[13]:


from skimage import measure, data
import matplotlib.pyplot as plt
horse_image = data.horse()
contours = measure.find_contours(horse_image, level = 0.8)
show_image_contour(horse_image, contours)


# In[15]:


def show_image_contour(image, contours):
    plt.figure()
    for n, contour in enumerate(contours):
        plt.plot(contour[:,1], contour[:, 0], linewidth= 3)
    plt.imshow(image, interpolation = 'nearest', cmap= 'gray_r')
    plt.title("contours")
    plt.axis("off")


# In[17]:


from skimage.io import imread
from skimage.filters import threshold_otsu
from skimage import color

image_dices = imread("diceimg.png")

image_dices = color.rgb2gray(image_dices)

thresh = threshold_otsu(image_dices)

binary = image_dices > thresh

contours = measure.find_contours(binary, level = 0.8)

show_image_contour(image_dices, contours)


# In[18]:


def show_image_contour(image, contours):
    plt.figure()
    for n, contour in enumerate(contours):
        plt.plot(contour[:,1], contour[:, 0], linewidth= 3)
    plt.imshow(image, interpolation = 'nearest', cmap= 'gray_r')
    plt.title("contours")
    plt.axis("off")
import numpy as np
shape_contours  = [cnt.shape[0] for cnt in contours]
max_dots_shape = 50
dots_contours = [cnt for cnt in contours if np.shape(cnt)[0]<max_dots_shape]
show_image_contour(binary, contours)
print("dice dots number:{}.".format(len(dots_contours)))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




