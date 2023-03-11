#!/usr/bin/env python
# coding: utf-8

# In[7]:


def Getstring(s):
    d={"Upper":0, "Lower":0}
    for c in s:
        if c.isupper():
           d["Upper"]+=1
        elif c.islower():
           d["Lower"]+=1
    print ("Given String : ", s)
    print ("Count of Upper case characters : ", d["Upper"])
    print ("Count of Lower case Characters : ", d["Lower"])

Getstring('The quick Brow Fox')


# In[ ]:




