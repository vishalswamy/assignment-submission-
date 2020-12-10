#!/usr/bin/env python
# coding: utf-8

# # capitalize

# In[1]:


a="hello welcome to letsupgrade"
print(a)


# In[2]:


a.capitalize()


# In[3]:


print(a)


# In[8]:


res=a.capitalize()


# In[9]:


print(res)


# # center (width,fillchar)

# In[11]:


b="hello"


# In[12]:


print(b)


# In[13]:


b.center(11,"X")


# In[14]:


a.center(11,"X")


# # count (str,beg,end)

# In[16]:


a.count("o",0,len(a))


# In[17]:


a.endswith("e",0,len(a))


# In[18]:


a.endswith("x",0,len(a))


# In[21]:


a.find("w",0,len(a))


# # islower() isupper()

# In[22]:


print(a)


# In[23]:


a.islower()


# In[24]:


c="Hello"


# In[25]:


c.islower()


# In[26]:


print(a)


# In[27]:


a.isupper()


# In[28]:


c="HELLO"


# In[30]:


c.isupper()


# # istitle() len()

# In[31]:


d="Hello Welcome To Python "


# In[32]:


d.istitle()


# In[33]:


e="Hello welcome To python"


# In[34]:


e.istitle()


# In[35]:


print(a)


# In[36]:


len(a)


# In[37]:


f="welcome to python"


# In[38]:


len(f)


# # max(sring), startswith(string)

# In[39]:


print(c)


# In[41]:


max(c)


# In[42]:


max(a)


# In[43]:


max(d)


# In[44]:


print(a)


# In[45]:


a.startswith("hello",0,len(a))


# In[46]:


a.startswith("p",0,len(a))


# In[ ]:




