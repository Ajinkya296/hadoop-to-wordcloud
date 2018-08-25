
# coding: utf-8

# In[1]:


from nytimesarticle import articleAPI
from bs4 import BeautifulSoup
import requests
import re
import io


# In[2]:


api = articleAPI("7b9a5b632d244ba281e306111824d31a")


# In[26]:


search_keyword = 'stormy daniels trump' 
articles = api.search(q=search_keyword,begin_date="20161001")


# In[27]:


for doc in articles['response']['docs']:
    arti_url = doc['web_url']
    print(arti_url)


# In[43]:


arti_url = "https://www.nytimes.com/2018/03/13/arts/television/stephen-colbert-trump-stormy-daniels.html"
page = requests.get(arti_url)
soup = BeautifulSoup(page.content,'html.parser')
para = soup.find_all('p',class_='story-body-text')
text = ""
filename = "trump13" +" "+doc['pub_date'][:10]+'.txt'
for p in para:
    text += p.get_text()
with io.open('NYArticles/'+filename, "w", encoding="utf-8") as f:
    f.write(text)


# In[15]:


i = 0
for doc in articles['response']['docs']:
    arti_url = doc['web_url']
    page = requests.get(arti_url)
    soup = BeautifulSoup(page.content,'html.parser')
    para = soup.find_all('p',class_='story-body-text')
    text = ""
    filename = "trump1" +" "+doc['pub_date'][:10]+'.txt'
    for p in para:
        text += p.get_text()
    with io.open('NYArticles/'+filename, "w", encoding="utf-8") as f:
        f.write(text)
    #f =  open('NYArticles/'+filename,'w')
    #text = re.sub('[^a-zA-Z0-9_, +]', '', text)
    #f.write(text)
    i+=1

