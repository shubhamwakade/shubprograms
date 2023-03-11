#!/usr/bin/env python
# coding: utf-8

# In[3]:


class findpower:
   def newpow(self, x, n):
        if x==0 or x==1 or n==1:
            return x 

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        val = self.newpow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

x=int(input("Enter x value :"))
n=int(input("Enter n value :"))
print("Output is",findpower().newpow(x, n));


# In[ ]:





# In[ ]:




