#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd

data = pd.read_csv(r'C:\Users\SATGOSWAMI\Documents\t-test.csv')
print(data)
data.head()


# In[28]:


data['diff'] = data['After Course'] - data['Before Course']
data['diff^2'] = data['diff'] ** 2
data.head()


# In[23]:


len(data)


# In[33]:


from math import sqrt
numerator = sum(data['diff'])
denominator = sqrt(((len(data)*sum(data['diff^2']) - (sum(data['diff']))**2) / (len(data)-1)))
t = numerator/denominator
print(t)


# In[ ]:


## degree of freedom is 11, At 5% significance level critical t-value is 0.6979. Since t> critical t value we reject null hypothesis.


# In[ ]:




