#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np

#read image
img_noisy1=cv2.imread("noisy.jfif",0)

#obtain no of rows and columns
m,n=img_noisy1.shape

#traverse the image
img_new1=np.zeros([m,n])
for i in range(1,m-1):
    for j in range(1,n-1):
        temp=[img_noisy1[i-1,j],
              img_noisy1[i-1,j+1],
              img_noisy1[i,j-1],
              img_noisy1[i,j],
              img_noisy1[i,j+1],
              img_noisy1[i+1,j-1],
              img_noisy1[i+1,j],
              img_noisy1[i-1,j-1],
              img_noisy1[i+1,j+1]]
        
        temp=sorted(temp)
        img_new1[i,j]=temp[4]
        img_new1=img_new1.astype(np.uint8)
        
cv2.imshow("Median filtered image",img_new1)
cv2.waitKey(0)
cv2.destroyAllWindows()

