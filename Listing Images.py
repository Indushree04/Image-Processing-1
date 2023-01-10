#!/usr/bin/env python
# coding: utf-8

# In[1]:


#listing only png Images
#import the modules
import os
from os import listdir

#get the path/directory
folder_dir="D:/Indushree"
for images in os.listdir(folder_dir):
    
    #check if the images end with png
    if(images.endswith(".png")):
        print(images)


# In[2]:


#Listing all the images
#import the modules
import os
from os import listdir

#get the path/directory
folder_dir="D:/Indushree"
for images in os.listdir(folder_dir):
        print(images)


# In[10]:


#Display all the images
#import necessary packages 
import cv2 
import os 
import glob 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
 
#Set the path where images are stored 
img_dir = "D:/Indushree" # Enter Directory of all images  
data_path = os.path.join(img_dir,'*') 
files = glob.glob(data_path) 
data = [] 
for f1 in files: 
    img = cv2.imread(f1) 
    data.append(img) 
    plt.figure() 
    plt.imshow(img) 


# In[ ]:




