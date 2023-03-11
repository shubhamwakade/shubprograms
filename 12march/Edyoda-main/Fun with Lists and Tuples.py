#!/usr/bin/env python
# coding: utf-8

# In[1]:


def funlast(n):
    return n[-1]  
def sort(tuples):
    return sorted(tuples, key=funlast)
   
tup_list=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("Sorted list in the increasing order by the last element in each tuple:")
print(sort(tup_list))


# In[ ]:




