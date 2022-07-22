#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task 2
import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
example = "The quick brown fox jumps over a lazy dog"
example = [stemmer.stem(token) for token in example.split(" ")]
print(" ".join(example))


# In[3]:


stemmer = PorterStemmer()
myfile = open("btime.txt")
eg = myfile.read()
eg = [stemmer.stem(token) for token in eg.split(" ")]
print(" ".join(eg))


# In[ ]:




