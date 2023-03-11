#!/usr/bin/env python
# coding: utf-8

# In[5]:


def reverse(alist):

   #intializing pointers
   left = 0
   right = len(alist)-1

   #condition for termination
   while left<right:

       #swapping
       temp = alist[left]
       alist[left] = alist[right]
       alist[right] = temp

       #updating pointers
       left += 1
       right -= 1

   return alist

a=[1,2,3,4,5]
print("The original array", a)
reverse(a)
print("The reversed array in place",a)


# In[ ]:




