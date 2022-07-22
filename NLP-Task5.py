#!/usr/bin/env python
# coding: utf-8

# In[2]:


#TASK 5
import nltk
nltk.download('punkt')


# In[4]:


import nltk
texts = "Who would ever suspect that a tiny little mouse could wear out an energetic young boy? Well, if you're going to go around giving an exuberantly bossy rodent a cookie, you'd best be prepared to do one or two more favors for it before your day is through. For example, he'll certainly need a glass of milk to wash down that cookie, won't he? And you can't expect him to drink the milk without a straw, can you? By the time our hero is finished granting all the mouse's very urgent requests--and cleaning up after him--it's no wonder his head is becoming a bit heavy. Laura Joffe Numeroff's tale of warped logic is a sure-fire winner in the giggle-generator category. But concerned parents can rest assured, there's even a little education thrown in for good measure: underneath the folly rest valuable lessons about cause and effect."
for text in texts:
    sentences = nltk.sent_tokenize(texts)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(words)
        print(tagged)


# In[ ]:




