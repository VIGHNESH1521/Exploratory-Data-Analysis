#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('zomato.csv',encoding='latin-1')
df.head()


# In[3]:


df.columns


# In[4]:


df.info()


# In[5]:


#checking for missing values
df.isnull().sum()


# In[6]:


#Checking for feature with null values
[features for features in df.columns if df[features].isnull().sum()>0]


# In[7]:


df.describe()


# In[8]:


sns.heatmap(df.isnull(),yticklabels=False,xticklabels=True,cmap='viridis')


# In[9]:


df_country = pd.read_excel('Country-Code.xlsx')
df_country.head()


# In[10]:


final_df = pd.merge(df, df_country, on = 'Country Code', how = 'left')


# In[11]:


final_df.head()


# In[12]:


final_df.dtypes


# In[13]:


# how many different countries are there in the dataset
country_names = final_df.Country.value_counts().index


# In[14]:


country_values = final_df.Country.value_counts().values


# In[15]:


# pie chart to show the top 3 countries using ZOMATO
plt.pie(country_values[:3],labels=country_names[:3],autopct='%1.2f%%',rotatelabels=True)


# Observation
# Zomato's maximum records or business is from INDIA, then from USA & UK

# In[16]:


ratings = final_df.groupby(['Aggregate rating', 'Rating color','Rating text']).size().reset_index().rename(columns = {0:'Rating Count'})


# In[17]:


ratings


# OBSERVATION
# 
# 1. When ratings is between 4.5 to 4.9 --> Excellent
# 2. When ratings is between 4.0 to 4.4 --> Very Good
# 3. When ratings is between 3.5 to 3.9 --> Good
# 4. When ratings is between 2.5 to 3.4 --> Average
# 5. When ratings is between 1.8 to 2.4 --> Poor
# 6. When ratings is 0 ie., No ratings has been given

# In[18]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12,6)
sns.barplot(x ='Aggregate rating', y = 'Rating Count', data = ratings, hue = 'Rating color',palette=['white','red','orange','yellow','green', 'green'])


# In[19]:


sns.countplot(x ='Rating color', data = ratings,palette=['grey','red','orange','yellow','green', 'green'])


# In[20]:


## The countries which has given 0 rating
final_df[final_df['Rating color']=='White'].groupby('Country').size().reset_index()


# In[21]:


final_df.columns


# In[22]:


final_df[['Country', 'Currency']].groupby(['Country','Currency']).size().reset_index()


# In[23]:


final_df[final_df['Has Online delivery'] == 'Yes'].Country.value_counts()


# In[24]:


final_df[final_df['Has Online delivery'] == 'No'].Country.value_counts()


# # OBSERVATION
# 
# 1. Online deliveries are available in INDIA and UAE

# In[25]:


final_df.City.value_counts().index


# In[26]:


city_values = final_df.City.value_counts().values
city_labels = final_df.City.value_counts().index


# In[27]:


plt.pie(city_values[:5], labels = city_labels[:5],autopct='%1.2f')


# In[ ]:




