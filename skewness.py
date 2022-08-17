#!/usr/bin/env python
# coding: utf-8

# In[15]:


from math import sqrt


# In[ ]:


def var():
    vary = 0
    for i in range(2):
        var+=Py[i]*(y[i]-Ey)**2
        stdy = sqrt(vary)
        return stdx,stdy


# In[8]:


def skewness():
    avg=x.mean()
    mod=x.mode()
    vari=x.var()
    std=sqrt(vari)
    skew = (avg-mod)/std
    return skew


# In[ ]:





# In[ ]:





# In[ ]:




