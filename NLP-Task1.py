#!/usr/bin/env python
# coding: utf-8

# In[1]:


#TASK 1
import nltk


# In[2]:


from nltk.stem import PorterStemmer
stemmerporter = PorterStemmer()


# In[3]:


stemmerporter.stem('happiness')


# In[4]:


import nltk
from nltk.stem import LancasterStemmer
stemmerLen= LancasterStemmer()
stemmerLen.stem('happiness')


# In[5]:


import nltk
from nltk.stem import RegexpStemmer
stemmerregexp = RegexpStemmer('ing')
stemmerregexp.stem('singing')


# In[6]:


import nltk
from nltk.stem import SnowballStemmer
SnowballStemmer.languages
frenchstemmer= SnowballStemmer('french')
frenchstemmer.stem('manges')


# In[7]:


stemmerLen.stem('being')


# In[8]:


stemmerporter.stem('being')

