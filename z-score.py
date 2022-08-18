#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import random
import numpy as np
import pandas as pd
import math


# In[2]:


df = pd.DataFrame(np.random.normal(loc=5, scale=4,size=100),columns = ['x'])
df.to_csv("normal.csv")
data=pd.read_csv('normal.csv')
data=data.loc[:,"x"]
print("Mean = ",data.mean())
print("Variance = ",data.var())


# In[3]:


z_score=(data-data.mean())/math.sqrt(data.var())
from matplotlib import pyplot as plt
plt.plot(data,label="Actual data",color='red')
plt.plot(z_score,label="Z-Score",color='blue')
plt.legend()
plt.show() 

