#!/usr/bin/env python
# coding: utf-8

# In[3]:


n = input("Enter your word to reverse: ")
a=[]
for i in range(len(n) - 1, -1, -1):
    a.append(n[i])
print("Reverse of string :","".join(a))


# In[ ]:




