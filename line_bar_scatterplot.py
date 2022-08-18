#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[7]:


x = np.array(["A", "B", "C", "D", "E", "F"])
y = np.array([26, 31, 9, 17, 22, 87])

plt.bar(x,y)
plt.show()

plt.scatter(x,y)
plt.show()


# In[6]:


ypoints = np.array([13, 21, 17, 26, 9, 11])

plt.plot(ypoints, ls = ':')
plt.show()


# In[ ]:





# In[ ]:




