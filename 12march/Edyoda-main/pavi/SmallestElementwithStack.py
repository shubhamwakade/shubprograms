#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Python program to find smallest
# number in stack with list
 

stack = []
 
# asking number of elements to put in list
num = int(input("Enter number of elements in the stack: "))
 
# iterating till num to append elements in list
for i in range(1, num + 1):
    ele= int(input("Enter elements: "))
    stack.append(ele)
     
# print maximum element
print("Smallest element is:", min(stack))


# In[ ]:





# In[ ]:





# In[ ]:




