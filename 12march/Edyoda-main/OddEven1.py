#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Method 1 Getting starting and ending number for the range

seriesstart=int(input("Enter your start number: "))
series = int(input("Enter your end number: "))
oddno = 0
evenno = 0
for i in range(seriesstart,series+1):
        if (i % 2)==0:
            evenno+=1
        else:
            oddno+=1
print("Number of even numbers :",evenno)
print("Number of odd numbers :",oddno)


# In[2]:


#Method 2

series = [1,2,3,4,5,6,7,8,9]
oddno = 0
evenno = 0
for i in series:
        if (i % 2)==0:
            evenno+=1
        else:
            oddno+=1
print("Number of even numbers :",evenno)
print("Number of odd numbers :",oddno)


# In[ ]:




