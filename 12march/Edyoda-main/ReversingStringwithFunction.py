#!/usr/bin/env python
# coding: utf-8

# In[3]:


def rev_string(str):  #Function Definition
    str1 = ""    
    for i in str:  
        str1 = i + str1  
    return str1    
     
str = "1234abcd"         
print("The original string is: ",str)  
print("The reversed string is: ",rev_string(str)) # Function call  


# In[ ]:




