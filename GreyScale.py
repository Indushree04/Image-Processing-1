#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2


# In[6]:


image=cv2.imread("fall.jfif",0)
cv2.imshow('images',image)


# In[3]:


cv2.imwrite('D:\Indu.png',image)


# In[4]:


cv2.waitKey(0)
cv2.destroyAllWindows()

