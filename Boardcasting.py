#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
A = np.array([[56.0, 0.0, 4.4, 68.0],[1., 104.0, 52.0, 8.0],[1.8, 135.0, 99.0, 0.9]])
print(A)


# In[20]:


cal = A.sum(axis = 0) #计算每列的和， 如果axis = 1 则是每行求和
print(cal)


# In[17]:


percentage = 100*A/cal.reshape(1,4) #不加.reshape也可以得到结果 但是加上可以确保矩阵是你想要的矩阵维度


# In[18]:


print(percentage)


# In[ ]:




