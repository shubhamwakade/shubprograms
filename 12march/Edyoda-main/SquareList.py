#!/usr/bin/env python
# coding: utf-8

# In[2]:


def squarenum(n):
  return n * n
num1 = [4, 5, 2, 9]
print("Given List: ",num1)
result = map(squarenum, num1)
print("Square of the elements:")
print(list(result))


# In[ ]:




