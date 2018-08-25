
# coding: utf-8

# In[7]:


from twython import Twython
import json
import pandas as pd


# In[2]:


consumer_key    = "5RRobOAR92qXK0Oi6ETOoN3Vq"
consumer_secret = "PZn2pgtfnFkLKPSSEdBQywO6dDhHQDFvO12wwQxiZYN1dNX4Tv"


# In[11]:


python_tweets = Twython(consumer_key,consumer_secret)
query = {'q': 'trump',  
        'result_type': 'popular',
        'count': 100,
        'lang': 'en',
        }
dict_ = {'user': [], 'date': [], 'text': []}
status_list = python_tweets.search(**query)['statuses']
for status in status_list:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
dict_df = pd.DataFrame.from_dict(dict_)
print(dict_df)

