#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
vidcap = cv2.VideoCapture('sample.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1


# In[10]:


pip install tensorflow==2.7.0


# In[16]:


pip install keras==2.4.3


# In[ ]:




