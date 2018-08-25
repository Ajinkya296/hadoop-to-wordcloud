
# coding: utf-8

# In[29]:


import pandas as pd
import re
import string
import io


# In[40]:


tweets_df =  pd.read_csv('D:\Academics\Spring 2018\Data Intensive Computing\Lab2\\tweets.csv',encoding = "ISO-8859-1")


# In[41]:


print(tweets_df['text'][:10])


# In[42]:


num_sentences = 1000
sentences = []
sentence = ""
i = 0
for tweet in tweets_df['text'][:1500]:
    words = tweet.split(" ")
    for word in words:
        word = re.sub(r'[^\x00-\x7F]+',' ', word)
        word = word.replace("\r\n","")
        word = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', word)
        if " " in word:
            camelCase_words = word.split(" ")
            word = camelCase_words[0]
            for cc_word in camelCase_words[1:]:
                words += [cc_word]
        word = word.translate(str.maketrans({key: None for key in string.punctuation}))
        if len(word) > 0:
            if word!="RT" and word[0] != "@" and "U0" not in word and word[0] != "\\" and "http" not in word:                
                if word[0] == "#":
                    word = word[1:]
                sentence += " " + word
                print(word," " , i)
                i+=1
    sentences += [sentence]
    


# In[48]:


filename = "Trump Rest Tweets"
with io.open('D:/Academics/Spring 2018/Data Intensive Computing/Lab2/Tweets/Trump/'+filename, "w", encoding="utf-8") as f:
        for text in sentences[500:]:
            f.write(text)

