#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd


# In[28]:


titanic = pd.read_csv ( r"C:\Users\hp\Desktop\titanic.csv")



# In[29]:


titanic


# In[38]:


#OPTION FOR MAX ROWS 
pd.options.display.min_rows =20


# In[39]:


titanic


# In[40]:


#FIRST ROWSالصفوف الاولى 
titanic.head(20)


# In[41]:


#LAST ROWS
titanic.tail(20)


# In[42]:


#INFO METHODيطلع لي الداتا فريم 
titanic.info()


# In[43]:


titanic.describe()


# In[47]:


#FIND DATA THAT IS DATA TYPE IS OBJECT فلترة
titanic.describe(include = "float")


# In[ ]:


#BUILT FUNCTIONS & DATA FRAMES ATTRIBUTES AND METHODS


# In[48]:


type(titanic)


# In[49]:


len(titanic) #HOW MANY ROWS


# In[50]:


round(titanic,0) #MAKE THE VALUE .0 VALUE


# In[51]:


min(titanic) #LESS VALUE


# In[52]:


max(titanic) #MORE VALUE


# In[53]:


titanic.shape #NUMBER OF ROWS AND COULM


# In[54]:


titanic.size #THE SIZE OF THE FILE 


# In[55]:


titanic.index


# In[57]:


titanic.columns


# In[ ]:


#DATA FRAM METHODS 


# In[58]:


titanic.head(n=2) #FIRST 2 ROWS


# In[59]:


titanic.mean()


# In[61]:


#METHOD CHINING
titanic.mean().sort_values().head(2)


# In[62]:


titanic["age"]


# In[63]:


type(titanic["age"])


# In[64]:


titanic[["age" , "sex"]]


# In[65]:


titanic[["age" , "sex" , "fare"]]


# In[ ]:





# In[ ]:


#SELECT ONE COLUNM WITH DOT NOTATION


# In[66]:


titanic.age.equals(titanic['age'])


# In[68]:


titanic[titanic.sex=='female']


# In[72]:


titanic[titanic.sex=='male'].head(15)


# In[73]:


titanic[titanic.sex=='female']['fare']


# In[ ]:




