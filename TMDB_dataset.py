#!/usr/bin/env python
# coding: utf-8

# ### INTRODUCTION

# In this project, I will analyze TMDB Dataset and communicate my findings using Numpy, Pandas and Seaborn Python Library.
# In this report, the data analysis will be used to answer the following questions:
# 
# - Which year has the highest release of Movie ?
# - Which genre has the  release of Movie ?
# - Which Month has the highest release of Movies?
# - Who is the Most Frequent Star cast

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# ### Data Gathering

# In[4]:


#Load dataset and view the first 5 dataset
df = pd.read_csv(r"C:\Users\BOUQSESH-PC\Downloads\tmdb-movies.csv")
df.head()


# ### Data wrangling

# In[6]:


df.shape


# The dataset contains 10866 rows and 21 columns

# In[6]:


# inspect data types and look for instance of missing data
df.info()


# In[8]:


# check for missing data
df.isnull().sum()


# In[9]:


# summary statistics of the dataset
df.describe()


# In[10]:


#check for duplicate rows
sum(df.duplicated())


# ### Data Cleaning
# - Delete duplicate rows
# - Remove Rows that are not necesary for analysis
# - Change column of the release date to datetime format

# In[11]:


#Drop duplicate row
df.drop_duplicates(inplace=True)


# In[12]:


#Drop column that are not necessary for the analysis
df.drop(["imdb_id","homepage","tagline","overview"],axis=1,inplace=True)


# In[13]:


#check for last rows of datasets
df.tail()


# In[14]:


#Convert releasedate from string format to datetime
df['release_date'] = pd.to_datetime(df['release_date'])
df['release_date'].head()


# ### Exploratory Data Analysis

# ### Q1: Which year has the highest release of movies?

# In[35]:


df.groupby('release_year').count()['id'].sort_values(ascending=False)


# 2014 is the year with the highest movie release

# ### Q2: Which Genres has the highest release of Movies?

# In[19]:


# split genres string, at |, explode the list to rows
genres_df = df.assign(genres=df['genres'].str.split('|')).explode('genres')
genres_df.head()


# In[21]:


# group exploded dataframe by genres, get average popularity
genres_df.groupby('genres').popularity.mean()


# In[22]:


genres_df.groupby('genres').popularity.mean().plot.pie(figsize=(10,8), autopct='%1.2f%%')
plt.title('Percentage of each Genre')
plt.show()


# Adventure has the highest release of Movie

# ### Which Month Has the highest release of movies in all the Movies

# In[24]:


df['month']= df['release_date'].dt.month
df['month'].value_counts().sort_index(). plot(kind='bar',figsize=(10,8),rot=0);
plt.title(f'Comparison of Monthly MOvie Release'.title() , fontsize=14, weight='bold')
plt.xlabel('month'.title(), fontsize=12, weight='bold')
plt.ylabel('Number Released'.title(), fontsize=12, weight='bold')


# September is the month with the highest movie release

# In[46]:


# for movies with positive revenue,which month has the highest average revenue?
df.query('revenue_adj > 0').groupby('month')['revenue_adj'].mean().sort_index().plot(kind='bar',figsize=(10,8),color="pink");
plt.title(f'Comparison of Month with highest average Revenue'.title() , fontsize=14, weight='bold')
plt.xlabel('month'.title(), fontsize=12, weight='bold')
plt.ylabel('Average Revenue'.title(), fontsize=12, weight='bold')


# June has the highest Average Revenue

# ### Q4 Who is the most Frequent Star Cast?

# In[39]:


pop_actor=data("cast")
#plot the bar plot.
pop_actor.iloc[:20].plot.bar(figsize=(15,6),fontsize=14)

#setup the title and the labels of the plot.
plt.title("Most Frequent Actor",fontsize=15)
plt.xticks(rotation = 80)
plt.xlabel('Actor',fontsize=13)
plt.ylabel("Number Of Movies",fontsize= 13)
sns.set_style("darkgrid")


# Robert De Niro is the Most Frequent Star

# ### Conclusions

# Based on the Analysis, the following conclusions can be drawn:
# - 2014 is the year with the highest release of Movie
# - Adventure is the most release genre of Movies
# - September is the month with the most release of movie
# - Robert De Niro is the Most Frequent Star
# 
# ### Limitation
# - Dropping Rows with missing data affected the overall analysis.

# In[ ]:




