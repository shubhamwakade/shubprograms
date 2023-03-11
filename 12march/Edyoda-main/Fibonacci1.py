#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = 0
b = 1
print("The Fibonacci series between 0 to 50 --> ",end="")
print(a,end=" ")
print(b,end=" ")
for i in range(50):
    c = a + b
    a = b
    b = c
    if(b>50):
        break
    else:
        print(c,end=" ")


# In[ ]:




