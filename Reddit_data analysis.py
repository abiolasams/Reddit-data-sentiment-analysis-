#!/usr/bin/env python
# coding: utf-8

# In[27]:


import praw
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from IPython import display
import math
from pprint import pprint
from nltk.tokenize import word_tokenize, RegexpTokenizer
nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('stopwords')


# #### utilizing praw reddit webscraper api

# In[4]:


reddit = praw.Reddit(client_id='EL9uWf3ErWRD-A', client_secret='A_nwiG5rRFFww7NIOMbnug9ViLsntg', user_agent='brainstation123')


# ### reddit webscraping

# #### first set of data webscraped from reddit 

# In[5]:


#complaints from this weblink
submission = reddit.submission(url='https://www.reddit.com/r/Design/comments/4e93zy/what_is_the_best_stock_photo_website_for_the_best/')


# In[6]:


#webscraping the complaints 
a=[]
submission.comments.replace_more(limit=1000)
for comment in submission.comments.list():
    a.append(comment.body)


# #### second set of data webscraped from reddit 

# In[9]:


#all posts from subbreddit r/shutterstock
subreddit = reddit.subreddit('shutterstock') # Change the subreddit's name here 
sub_ids = []
for submission in subreddit.hot(limit = 1000): # Define the limit here and filter method
    sub_ids.append(submission.id)
    
top_level_comments = []
second_level_comments = []
title = []
selftext = []
for sub_id in sub_ids:
    submission = reddit.submission(id = sub_id)
    title.append(submission.title) # Get submission title
    selftext.append(submission.selftext) # Get submission content
    submission.comments.replace_more(limit = None)
    for top_level_comment in submission.comments:
        top_level_comments.append(top_level_comment.body) # Get top-level comments
        for second_level_comment in top_level_comment.replies:
            second_level_comments.append(second_level_comment.body) # Get second-level comments


# In[11]:


top_level_comments


# #### third set of webscraped data from reddit 

# In[13]:


#obtaining another set of comments on reddit
posts = []
ml_subreddit = reddit.subreddit('Shutterstock')
for post in ml_subreddit.hot():
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])

#extracting body to a list 
postToList = list(posts['body'])


# In[18]:


postToList


# In[15]:


# joining all webscraped data into one list
everything=postToList+a+top_level_comments


# In[28]:


#sentiment analysis 
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()
results = []

for line in everything:
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = line
    results.append(pol_score)

pprint(results[:3], width=100)


# In[29]:


#saving result of the sentiment analysis into a dataframe 
df = pd.DataFrame.from_records(results)
df.head()


# In[32]:


df['headline'].replace('', np.nan, inplace=True)


# In[33]:


df=df.dropna(subset=['headline'])
df.head()


# In[36]:


# obtaining sentiments for each line of comment on reddit
df['label'] = 0
df.loc[df['compound'] > 0.2, 'label'] = 1
df.loc[df['compound'] < -0.2, 'label'] = -1
df.head(10)


# In[39]:


print("Positive headlines:\n")
pprint(list(df[df['label'] == 1].headline)[:5], width=200)

print("\nNegative headlines:\n")
pprint(list(df[df['label'] == -1].headline)[:5], width=200)


# In[ ]:


#stopwords and tokenizer for the word count
stop_words = stopwords.words('english')
tokenizer = RegexpTokenizer(r'\w+')


# In[41]:


#function to tokenize and convert the words to lower character
def process_text(headlines):
    tokens = []
    for line in headlines:
        toks = tokenizer.tokenize(line)
        toks = [t.lower() for t in toks if t.lower() not in stop_words]
        tokens.extend(toks)
    
    return tokens


# In[46]:


#printing out the most frequent words from the positive sentiments
pos_lines = list(df[df.label == 1].headline)

pos_tokens = process_text(pos_lines)
pos_freq = nltk.FreqDist(pos_tokens)

pos_freq.most_common(20)


# In[47]:


#printing out the most frequent words from the negative sentiments
neg_lines = list(df[df.label == -1].headline)

neg_tokens = process_text(neg_lines)
neg_freq = nltk.FreqDist(neg_tokens)

neg_freq.most_common(20)


# #### word count plot for positive words

# In[65]:


frequency_dist = nltk.FreqDist(pos_tokens)


# In[66]:


from wordcloud import WordCloud
wordcloud = WordCloud(background_color="white", contour_width=3, contour_color='steelblue').generate_from_frequencies(frequency_dist)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


# ### tokenizing the data and using random forest classifier

# In[ ]:


df2 = df[['headline', 'label']]


# In[217]:


# store simplified data in X and y
X = df2['headline']
y = df2['label']


# In[218]:


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# In[219]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import load_files


# In[136]:


tvec = TfidfVectorizer(stop_words='english', max_features=1000, ngram_range=[1,2])
X_train_tvec = tvec.fit_transform(X_train)
X_test_tvec = tvec.transform(X_test)


# In[137]:


indices = np.argsort(tvec.idf_)[::]
features = tvec.get_feature_names()
top_n = 15
top_features = [features[i] for i in indices[:top_n]]
print(top_features)


# #### utilizing random forest classification

# In[141]:


rf = RandomForestClassifier()
rf.fit(X_train_tvec,y_train)


# In[142]:


rf.score(X_test_tvec, y_test)

