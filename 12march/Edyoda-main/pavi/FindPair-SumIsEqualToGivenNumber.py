#!/usr/bin/env python
# coding: utf-8

# In[3]:


def addsum(nums,target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (nums[i]+nums[j]==target and i!=j):
                return([i,j])
print(addsum([3,7,11,15],18))


# In[ ]:




