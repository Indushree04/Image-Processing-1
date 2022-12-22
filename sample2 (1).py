#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
image = Image.open('im1.jfif')
 
# Converting an image from PNG to WEBP format
image.save("image1.webp")
print("Image successfully converted!")


# In[2]:


#print mode
print(image.mode)


# In[3]:


#Cropping
import cv2
image = cv2.imread("flower.jfif")
cropped_image = image[50:200, 100:400]
cv2.imshow("Original Image", image)
cv2.imshow("Cropped Image", cropped_image )
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[58]:


#Writing on image
from PIL import Image,ImageDraw,ImageFont

img=Image.open("modi.jfif")
d1=ImageDraw.Draw(img)
font=ImageFont.truetype("calibri.ttf",50)
d1.text((50,60),"Namasthe",fill=(255,0,0),font=font)
img.show()


# In[ ]:


#Blending an image
im1=Image.open("im2.jpg")
im2=Image.open("im4.jpg")

alphablend1=Image.blend(im1,im2,alpha=.4)
alphablend2=Image.blend(im1,im2,alpha=.2)

alphablend1.show()
alphablend2.show()


# In[22]:


#RGB Channels
import matplotlib.pyplot as plt
im1=Image.open("modi.jfif")
ch_r,ch_g,ch_b=im1.split()
plt.figure(figsize=(18,6))
plt.subplot(1,3,1);
plt.imshow(ch_r,cmap=plt.cm.Reds);plt.axis('off')
plt.subplot(1,3,2);
plt.imshow(ch_g,cmap=plt.cm.Greens);plt.axis('off')
plt.subplot(1,3,3);
plt.imshow(ch_b,cmap=plt.cm.Blues);plt.axis('off')
plt.tight_layout()
plt.show()


# In[9]:


#negating the image
im=Image.open("rose.jfif")
im_t=im.point(lambda x:255-x)
im_t.show()


# In[41]:


#histogram
import matplotlib.pyplot as plt
im=Image.open("panda.jfif")


pl=im.histogram()
plt.bar(range(256),pl[:256],color='r',alpha=0.5)
plt.bar(range(256),pl[:256:2*256],color='g',alpha=0.4)
plt.bar(range(256),pl[2*256:],color='b',alpha=0.3)


# In[44]:


#statistics
from PIL import Image,ImageStat
im=Image.open('flower.jfif')
stat=ImageStat.Stat(im)
print(stat.mean)


# In[43]:


from PIL import Image,ImageStat
im=Image.open('flower.jfif')
stat=ImageStat.Stat(im)
print(stat.median)


# In[46]:


from PIL import Image,ImageStat
im=Image.open('flower.jfif')
stat=ImageStat.Stat(im)
print(stat.stddev)


# In[48]:


#Drawing on an image
from PIL import Image,ImageDraw
img=Image.open('emoji.jfif')
draw=ImageDraw.Draw(img)
draw.rectangle(xy=(50,50,150,150),
              fill=(0,127,0))
img.show()


# In[64]:


#Slicing
from skimage.io import imshow,imread
import matplotlib.pyplot as plt
im=imread('panda.jfif')
imshow(im)
fig,ax=plt.subplots(1,3,figsize=(6,4),sharey=True)
ax[0].imshow(im[:,0:130])
ax[0].set_title('First split')

ax[1].imshow(im[:,130:260])
ax[1].set_title('Second split')

ax[2].imshow(im[:,260:390])
ax[2].set_title('Third split')


# In[ ]:




