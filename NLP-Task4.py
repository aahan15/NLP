#!/usr/bin/env python
# coding: utf-8

# In[4]:


#TASK 4
pip install jieba


# In[5]:


#chinese segmentation using jieba
#pip install jieba
import jieba
seg = jieba.cut('誰もが彼の顔にパンチを持っているまで、彼の戦闘戦略を持っています。')
print(" ".join(seg))


# In[ ]:




