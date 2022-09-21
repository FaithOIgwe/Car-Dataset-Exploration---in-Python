#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


#import csv file


# In[3]:


car = pd.read_csv(r"C:\Users\AKHIGBE\Downloads\2. Cars Data1.csv")


# In[4]:


car.head()


# In[5]:


car.shape


# In[10]:


#checking for null values, and if there is fill it in with the mean of that column
car.isnull().sum()


# In[12]:


car['Cylinders'].fillna(car['Cylinders'].mean(), inplace = True)


# In[13]:


#Exploring the Value Counts : What are the differnet  types of make in our dataste, and what is the count occurence  of each make in the data?
car.head(2)


# In[14]:


car['Make'].value_counts()


# In[15]:


#Exploring all the records where origin is Asia or Europe?
car.head(2)


# In[17]:


car[car['Origin'].isin(['Asia', 'Europe'])]


# In[18]:


#Removing all the records where weight is above 4000

car.head(2)


# In[22]:


car[~(car['Weight'] > 4000)]


# In[24]:


#how many cars left that do not have the weight 4000
432 - 329


# In[25]:


#Increase all the values of 'MPG_City' column by 3
car.head(2)


# In[27]:


car['MPG_City'] - car['MPG_City'].apply(lambda x:x+3)


# In[35]:


car


# In[ ]:




