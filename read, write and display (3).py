#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


image=cv2.imread("fall.jfif")
cv2.imshow('images',image)


# In[3]:


cv2.imwrite('D:\Indu.png',image)


# In[4]:


cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


#from eternal drive
image=cv2.imread("D:/Indushree/heart.png")
cv2.imshow('images',image)


# In[6]:


cv2.waitKey(0)
cv2.destroyAllWindows()


# In[7]:


#height and width
from PIL import Image
x="modi.jfif"
img=Image.open(x)
width=img.width
height=img.height
print("The Height of the Image is:",height)
print("The Width of the Image is:",width)


# In[8]:


import cv2
image=cv2.imread("heart.png",0)
print("No of Channels is:"+str(image.ndim))
print("No of Channels is:",image.shape)
cv2.imshow('images',image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[9]:


import cv2
image=cv2.imread("flower.jfif")
print("No of Channels is:"+str(image.ndim))
print("No of Channels is:",image.shape)
cv2.imshow('images',image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[10]:


from PIL import Image
filepath="dog.jfif"
im=Image.open(filepath)
new_im=im.resize((300,300))
new_im


# In[11]:


#matrix representation of image
import matplotlib.image as image
img=image.imread("flower.jfif")
print("The shape of the image is",img.shape)
print("The array of image is")
print(img)


# In[12]:


import cv2
img=cv2.imread("butterfly.jfif",0)
ret,bw_img=cv2.threshold(img,127,225,cv2.THRESH_BINARY)
bw=cv2.threshold(img,225,127,cv2.THRESH_BINARY)
cv2.imshow("Binary",bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[13]:


imgi=cv2.imread("modi.jfif",1)
cv2.imshow("original",imgi)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[14]:


cv2.imshow("BLUE",B)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


cv2.imshow("RED",R)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


cv2.imshow("GREEN",G)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


#aspect ratio
import cv2

img=cv2.imread("feather.jfif")
new_im=img.resize((400,200))
ar=1*(img.shape[1]/img.shape[0])
print("Aspect Ratio")
print(ar)


# In[15]:


from PIL import Image

x="panda.jfif"
img=Image.open(x)
hori_flip=img.transpose(Image.FLIP_LEFT_RIGHT)
hori_flip.show()
ver_flip=img.transpose(Image.FLIP_TOP_BOTTOM)
ver_flip.show()


# In[16]:


import cv2

im=cv2.imread("feather.jfif")
grey=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
LAB=cv2.cvtColor(im,cv2.COLOR_BGR2LAB)
RGB=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
HSV=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
HLS=cv2.cvtColor(im,cv2.COLOR_BGR2HLS)
YUV=cv2.cvtColor(im,cv2.COLOR_BGR2YUV)

cv2.imshow("Convert BGR to Grey",grey)
cv2.imshow("Convert BGR to LAB",LAB)
cv2.imshow("Convert BGR to Grey",RGB)
cv2.imshow("HSV",HSV)
cv2.imshow("HLS",HLS)
cv2.imshow("YUV",YUV)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[17]:


import cv2

a=cv2.imread("im2.jpg")
b=cv2.imread("im4.jpg")

sum=a+b
sub=a-b
mul=a*b
div=a/b

cv2.imshow("add",sum)
cv2.imshow("sub",sub)
cv2.imshow("mul",mul)
cv2.imshow("div",div)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




