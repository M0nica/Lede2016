
# coding: utf-8

# In[10]:

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


# In[11]:


# grab the NYT homepage
response = requests.get("http://www.newyorktimes.com")

doc = BeautifulSoup(response.text, "html.parser")


# In[12]:

# Feed it into BeautifulSoup
stories = doc.find_all("article", {'class':'story'})
len(stories)


# In[13]:

# Get out the stories

# class name for story is story 
all_stories = []
for story in stories:
    
    this_story = story
    headline = story.find('h2',{'class':'story-heading'})
    byline = byline = story.find('p',{'class':'byline'})
    if headline:
        headline_text = headline.text.strip()
    if byline:
        byline_text = byline.text.strip()
        this_story['byline'] = byline_text
    all_stories.append(this_story)


# In[14]:

len(all_stories)


# In[ ]:

import pandas as pd


# In[ ]:

stories_df = pd.DataFrame(all_stories)


# In[ ]:

stories_df.to_csv("nyc-data.csv")


# In[ ]:

# Save the headlines and bylines to a timestamped CSV


# In[ ]:

import time


# In[ ]:

datestring = time.strftime("%Y-%m-%d-%H-%M")


# In[ ]:

filename = "nyt-data-" + datestring + ".csv"
stories_df.to_csv = (filename)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



