#!/usr/bin/env python
# coding: utf-8

# In[1]:


#TASK 3
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("formulae"))


# In[2]:


print(lemmatizer.lemmatize("better", pos = 'a'))


# In[3]:


print(lemmatizer.lemmatize("am", pos = 'v'))


# In[ ]:




