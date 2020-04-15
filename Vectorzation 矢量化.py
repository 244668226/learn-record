#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


a = np.random.rand(1000000)
b = np.random.rand(1000000)


# In[9]:


import time
tic = time.time()
c = np.dot(a,b)
toc = time.time()
print(c)
print('need time is:' + str(1000 * (toc - tic)) + 'ms')


# In[11]:


tic = time.time()
c = 0
tic = time.time()
for i in range(1000000):
    c += a[i] * b[i]
toc = time.time()
print(c)
print('need time is:' + str(1000 * (toc - tic)) + 'ms')


# In[ ]:




