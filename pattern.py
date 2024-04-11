#!/usr/bin/env python
# coding: utf-8

# In[2]:


for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")


# In[3]:


for i in range(1,6):
    for j in range(6,i,-1):
        print("*",end=" ")
    print("\r")


# In[4]:


for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print("")


# In[5]:


for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print("")


# In[6]:


for i in range(1,6):
    for j in range(6,i,-1):
        print("*",end=" ")
    print("\r")


# In[7]:


for i in range(1,6):
    for j in range(1,i):
        print(" ",end="")
    for k in range(i,6):
        print("*",end="")
    print(" ")


# In[8]:


for i in range(1,6,2):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,7-i):
        print("* ",end="")
    print(" ")


# In[9]:


k=65
for i in range(1,6):
    for j in range(1,7-i):
        print(" ",end="")
    for l in range(1,i+1):
        print(chr(k),end=" ")
    print("")
    k=k+1


# In[10]:


k=5
for i in range(1,6):
    for j in range(1,7-i):
        print(" ",end="")
    for l in range(1,i+1):
        print(k,end=" ")
    print("")
    k=k-1


# In[11]:


k=6
for i in range(1,7):
    for j in range(1,8-i):
        print(k,end="")
    print(" ")
    k=k-1


# In[14]:


for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print("")

for i in range(1,6):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,7-i):
        print("* ",end="")
    print(" ")


# In[ ]:




