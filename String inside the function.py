#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to reverse a string.
# 

# In[1]:


samplestring=input("Entre The Words: ")
def reverse(samplestring):
    str = ""
    for i in samplestring:
        str = i + str
    return str
print("The reverse output is: ",end="")
print(reverse(samplestring))


# In[ ]:




