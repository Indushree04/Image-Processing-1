#!/usr/bin/env python
# coding: utf-8

# #Image Sharpness
# from PIL import Image
# from PIL import ImageFilter
# import matplotlib.pyplot as plt
# #Load the image
# my_image=Image.open('flower2.jpg')
# #Use sharpen function
# sharp=my_image.filter(ImageFilter.SHARPEN)
# #Save the image
# sharp.save('D:/Indushree/image_sharpen.jpg')
# sharp.show()
# plt.imshow(sharp)
# plt.show()

# In[2]:


#Image flip
import matplotlib.pyplot as plt
#Load the image
img=Image.open('flower2.jpg')
plt.imshow(sharp)
plt.show()
#use the flip function
flip=img.transpose(Image.FLIP_LEFT_RIGHT)

#save the image
flip.save('D:/Indushree/image_flip.jpg')
plt.imshow(flip)
plt.show()


# In[36]:


#Importing Image class from PIL module
from PIL import Image
import matplotlib.pyplot as plt
#opens image in RGB mode
im=Image.open('flower2.jpg')

#size of img in pixels(size of original image)
#this is not mandatory
width,height=im.size

#cropped img of above dimension
#It will not change original image
im1=im.crop((40,0,180,300))

#shows image in image viewer
im1.show()
plt.imshow(im1)
plt.show()


# In[ ]:




