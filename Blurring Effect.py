#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2
import numpy as np
#read image
img=cv2.imread('feather.jfif',0)

#obtain no of rows and columns
m,n=img.shape

#Developing Averaging filter(3,3)
mask=np.ones([3,3],dtype=int)
mask=mask/9

#construct 3*3 mask image
img_new=np.zeros([m,n])
for i in range(1,m-1):
    for j in range(1,n-1):
        temp=img[i-1,j-1]*mask[0,0]+img[i-1,j]*mask[0,1]+img[i-1,j+1]*mask[0,2]+img[i,j-1]*mask[1,0]+img[i,j]*mask[1,1]+img[i,j+1]*mask[1,2]+img[i+1,j-1]*mask[2,0]+img[i+1,j]*mask[2,1]+img[i+1,j+1]*mask[2,2]
        img_new[i,j]=temp
        img_new=img_new.astype(np.uint8)
cv2.imshow('Blurred Image',img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




