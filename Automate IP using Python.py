#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
import os
os.getcwd()


# In[2]:


# Let us import one image in our Jupyter environment and open that in the notebook itself

image1 = Image.open("snow.png")

image1


# In[3]:


image1.show()


# In[4]:


image1.save("pic1.png")


# In[5]:


# lists all the files and folders in the current working directory
os.listdir()


# In[6]:


for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        print(fn, "&", fext)


# In[7]:


#Looping over the image files
for f in os.listdir("."):
    if f.endswith(".jpg"):
        print(f)


# In[8]:


# Creating new Directory using OS library
os.mkdir('NewExtnsn')
# Note: If you already have a directory with this name, you will get error.


# In[9]:


for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.save("newExtnsn/{}.pdf".format(fn))


# In[10]:


# Creating new multiple Directories using OS library
os.makedirs('resize//small')
os.makedirs('resize//tiny')
# Note: If you already have a directory with this name, you will get error.


# In[11]:


size_small = (600,600) # small images of 600 X 600 pixels
size_tiny = (200,200)  # tiny images of 200 X 200 pixels
for f in os.listdir("."):
    if f.endswith(".png"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.thumbnail(size_small)
        i.save("resize/small/{}_small{}".format(fn, fext))
        i.thumbnail(size_tiny)
        i.save("resize/tiny/{}_tiny{}".format(fn, fext))


# In[12]:


image2 = Image.open("im3.jpg")
image2 = image2.convert(mode='L')
image2


# In[13]:


# Creating new Directory using OS library
os.mkdir('b&w')


# In[14]:


for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        im = i.convert(mode = 'L')
        im.save("b&w/{}_bw.{}".format(fn, fext))


# In[17]:


#rotating the image to 55 Degree angle
image3 = Image.open("im3.jpg")
image3.rotate(55).save("im2.jpg")
Image3 = Image.open("im2.jpg")


# In[18]:


Image3


# In[19]:


# Creating new Directory using OS library
os.mkdir('rotate')


# In[21]:


for f in os.listdir("."):
    if f.endswith(".png"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        im = i.rotate(90)
        im.save("rotate/{}_rot.{}".format(fn, fext))
 


# In[ ]:




