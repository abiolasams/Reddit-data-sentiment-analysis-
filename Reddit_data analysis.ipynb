{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to /home/jupyterlab/nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n",
      "[nltk_data] Downloading package vader_lexicon to\n",
      "[nltk_data]     /home/jupyterlab/nltk_data...\n",
      "[nltk_data]   Package vader_lexicon is already up-to-date!\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import praw\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import nltk\n",
    "from IPython import display\n",
    "import math\n",
    "from pprint import pprint\n",
    "from nltk.tokenize import word_tokenize, RegexpTokenizer\n",
    "nltk.download('punkt')\n",
    "nltk.download('vader_lexicon')\n",
    "nltk.download('stopwords')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### utilizing praw reddit webscraper api"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "reddit = praw.Reddit(client_id='EL9uWf3ErWRD-A', client_secret='A_nwiG5rRFFww7NIOMbnug9ViLsntg', user_agent='brainstation123')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### reddit webscraping"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### first set of data webscraped from reddit "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#complaints from this weblink\n",
    "submission = reddit.submission(url='https://www.reddit.com/r/Design/comments/4e93zy/what_is_the_best_stock_photo_website_for_the_best/')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#webscraping the complaints \n",
    "a=[]\n",
    "submission.comments.replace_more(limit=1000)\n",
    "for comment in submission.comments.list():\n",
    "    a.append(comment.body)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### second set of data webscraped from reddit "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "#all posts from subbreddit r/shutterstock\n",
    "subreddit = reddit.subreddit('shutterstock') # Change the subreddit's name here \n",
    "sub_ids = []\n",
    "for submission in subreddit.hot(limit = 1000): # Define the limit here and filter method\n",
    "    sub_ids.append(submission.id)\n",
    "    \n",
    "top_level_comments = []\n",
    "second_level_comments = []\n",
    "title = []\n",
    "selftext = []\n",
    "for sub_id in sub_ids:\n",
    "    submission = reddit.submission(id = sub_id)\n",
    "    title.append(submission.title) # Get submission title\n",
    "    selftext.append(submission.selftext) # Get submission content\n",
    "    submission.comments.replace_more(limit = None)\n",
    "    for top_level_comment in submission.comments:\n",
    "        top_level_comments.append(top_level_comment.body) # Get top-level comments\n",
    "        for second_level_comment in top_level_comment.replies:\n",
    "            second_level_comments.append(second_level_comment.body) # Get second-level comments"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Oh Shutterstock. How I hate you.',\n",
       " 'You have to start somewhere, right?',\n",
       " 'Why is impossible to post question here on this subreddit?',\n",
       " '\\\\[I honestly have no idea bro. like can u even make money outa shutterstock?',\n",
       " 'thank you foe sharing.',\n",
       " \"I actually had my first photo that I ever submitted (a selfie) rejected because the model release wasn't correct? Thought I filled it out properly. Was given no explanation of how to resubmit.\",\n",
       " 'Hitler part 2 .',\n",
       " 'r/StockImageCaption',\n",
       " 'Cool.! :)',\n",
       " \"I'm a Shutterstock contributor. I wonder if there is a similar petition for us to sign.\",\n",
       " \"Hey, good luck on your start :) \\nNo, you don't need to add any watermark, shutterstock does that automatically once they accept your photo and publish it.\",\n",
       " 'You have to upload your photo as editorial.',\n",
       " 'I don’t think you can 😞',\n",
       " 'It might be due to the jpg preview file. Is this the right size?',\n",
       " 'ngl, your photos kinda suck alba',\n",
       " 'Take high resolution pictures.\\nMake sure you have even lighting!\\nDo not include any glare or speckles (since these can be added in later)\\nPlace the item in a blank white background\\n(The fur is a hell to remove)\\nTake basic angles (front view, top, side, 45*, etc)\\nMake sure to have pictures of the WHOLE item.\\n',\n",
       " 'Such shit,',\n",
       " 'Shutterstock is shit.',\n",
       " 'You gotta take it to the authorities.\\nI’ve used shutterstock for years in my old marketing job, but the quality of their work is really based on quantity. ',\n",
       " '[Walt Disney Concert Hall](https://twitter.com/elessardunedain/status/1046687658116870144)',\n",
       " 'No selfpromotion please. ',\n",
       " 'What kind of material are you looking for?',\n",
       " 'ShutterStock is one of the best source of photos and graphic vectors',\n",
       " \"Shutterstock downloader is your tool to download any image you want from shutterstock.com 100% Free. \\nNo registration needed, and no fees. it's totally free.\",\n",
       " 'Scam! It asks for verification, you have to do surveys',\n",
       " 'Write the names of those who are members',\n",
       " 'Write the names of those who are members',\n",
       " '[Christmas paper design](https://www.shutterstock.com/image-vector/christmas-paper-design-illustration-seamless-tree-747836350)',\n",
       " \"Incredibly common subject. You'll do better looking for more unique topics. \",\n",
       " 'Knowing what is shutter speed, could be one of the most primary steps to learn photography. Shutter speed is a part of the exposure triangle that also includes ISO and Aperture (but more on that later). The final appearance of your photos depends greatly on how you set the shutter speed on your camera, besides other factors.It is actually a very simple concept that once understood, will make the difference between ‘just another photo’ and ‘the shot.’',\n",
       " 'Lol']"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top_level_comments"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### third set of webscraped data from reddit "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "#obtaining another set of comments on reddit\n",
    "posts = []\n",
    "ml_subreddit = reddit.subreddit('Shutterstock')\n",
    "for post in ml_subreddit.hot():\n",
    "    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])\n",
    "posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])\n",
    "\n",
    "#extracting body to a list \n",
    "postToList = list(posts['body'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Let\\'s look back at some memorable moments and interesting insights from last year.\\n\\n**Your top 10 posts:**\\n\\n* \"[My Best and Worst Selling Photos and Images on Shutterstock](https://www.youtube.com/watch?v=MLThFSU5OQ4)\" by [u/NikoNomad](https://www.reddit.com/user/NikoNomad)\\n* \"[Hmm](https://i.redd.it/1mt7osbefu441.jpg)\" by [u/TheSexyCheeseGrader](https://www.reddit.com/user/TheSexyCheeseGrader)\\n* \"[Watermark on images](/r/shutterstock/comments/dpzd6r/watermark_on_images/)\" by [u/hawk16v](https://www.reddit.com/user/hawk16v)\\n* \"[Hey guys I’m just starting off and would love if you can check my images and maybe I can make a couple of bucks just in time for the holdays, thank you so much if you even just glance I know it’s not a lot.](https://www.shutterstock.com/g/Davis+Olive?rid=250198396&utm_medium=email&utm_source=ctrbreferral-link)\" by [u/Virdian\\\\_](https://www.reddit.com/user/Virdian_)\\n* \"[Shutterstock Is Latest Tech Company to Censor Itself for China](https://theintercept.com/2019/11/06/shutterstock-china-censorship-tech/)\" by [u/koavf](https://www.reddit.com/user/koavf)\\n* \"[Problems with the model release](/r/shutterstock/comments/ecuwka/problems_with_the_model_release/)\" by [u/andybjpg](https://www.reddit.com/user/andybjpg)\\n* \"[illustrations in jpeg and not png?](/r/shutterstock/comments/e9m57j/illustrations_in_jpeg_and_not_png/)\" by [u/johnpardon](https://www.reddit.com/user/johnpardon)\\n* \"[can\\'t upload png illustrations but the site claims they do sell them?](/r/shutterstock/comments/e6zkdi/cant_upload_png_illustrations_but_the_site_claims/)\" by [u/johnpardon](https://www.reddit.com/user/johnpardon)\\n* \"[BORDER DESIGN](http://www.shutterstock.com/en/image/image-1336157342)\" by [u/jdk5051](https://www.reddit.com/user/jdk5051)\\n* \"[Refferal Link](/r/shutterstock/comments/dunryx/refferal_link/)\" by [u/HillarysFloppyChode](https://www.reddit.com/user/HillarysFloppyChode)',\n",
       " '',\n",
       " \"Hi, I'm new to shutterstock and sotck photography in general. I did some pics of my hand holding my car keys and I sign the contract as the model and the photographer. I send the pics but it says the contract is wrong but it doesn't give me an explanation. So, I want to know if this is because maybe my handwriting was difficult to read for the AI or what I'm doing wrong.\\n\\nThanks.\",\n",
       " '',\n",
       " \"do people want cutout jpeg stock illustrations? i mean the background becomes white right if it's in jpeg?\\n\\nit takes some time to transform my illustrations to vector. haven't figured out how to do it yet.\\n\\nbut i somehow sold one image already. is it worth it to create jpeg illustrations with white backgrounds? or is there a way to upload png images?\",\n",
       " \"do they convert vector images to png?\\n\\ni export most of my illustrations into png. clip files are useless. can put them in illustrator and convert them to vector but that's too much work imo. \\n\\nthe primary reason i wanted to do stock is because the market is filled with cold dead illustrator images. \\n\\ni've been uploading to jpeg but i am not familiar with the format but it seems like you can't upload transparent backgrounds?\",\n",
       " '',\n",
       " '',\n",
       " '[https://www.shutterstock.com/g/Joseph98?rid=250247548&utm\\\\_medium=email&utm\\\\_source=ctrbreferral-link](https://www.shutterstock.com/g/Joseph98?rid=250247548&utm_medium=email&utm_source=ctrbreferral-link)',\n",
       " '',\n",
       " 'I recently started contributing in Shutterstock. Do we need to really add watermark to our photos and upload? Or Shutterstock themselves will take care of the copyrights? Can anyone suggest me a way to proceed with Shutterstock please. What else should I take care when I am a contributor and trying to find a niche out of it.....',\n",
       " 'every time I have a picture with a brand logo or name I get the image rejected because of it but when I search the thing in my picture on Shutterstock the logo and brand name are right in the picture, why can some people post such pictures but I cant?',\n",
       " '',\n",
       " '',\n",
       " '[http://www.shutterstock.com/g/ThatGermanGuy?rid=247082386](http://www.shutterstock.com/g/ThatGermanGuy?rid=247082386)',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " \"I'm either too stupid or too blind. How can I change the prices of my uploaded footage at Shutterstock Contributor?\\n\\n&#x200B;\\n\\nThanks and sorry.\",\n",
       " '',\n",
       " 'I\\'m not sure if this belongs here, but all that google shows me is how to download stock photos for free. \\n\\nI am trying to download thousands of photos from my download history. These are photos I have licensed already. I want to download them (ideally with keywords in the metadata) to keep in a local library of images. \\n\\nIs there a service or program that does this? I found \"Shutter Library\" but I\\'m not sure if it\\'s trustworthy (this is a company account and I do not want to compromise the password).\\n\\nThanks!',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " 'Photos seem to take only 2 days to review. Videos going on a week without review.',\n",
       " 'I get this error  \\n\"The size of your artwork (not the size of the artboard) must be at least 4 megapixels.\"\\n\\n&#x200B;\\n\\nBut the size of my file is 6mb... so what gives? I did resize the artboard, I don\\'t know how else they expect this file to get bigger. I\\'ve uploaded here like a year ago, not sure why it\\'s not working now.',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " \"So they are still billing me, even though I told them I expressly forbid them from charging me anymore. They don't care. They shut out my access to the Shutterstock account when I cancelled last year, I have to now either cancel the card or go into the bank and go through they fraud processes with printouts of emails and evidence and stuff, just to charge it all back. \\n\\nAdobe's billing is transparent and very professional, I'd never expect something like this from them. There's free services like Pexels, and there's free stock vector sites too. The last thing you should ever do is give Shutterstock your financial details. They spend big on their banner ads, but they operate outside of the laws of your country and charge you a fortune for doing literally nothing.\\n\\nIf you are already a subscriber with Shutterstock, you should be able to cancel by charging back what you've already paid on your credit card, just call your bank and tell them about the unauthorised charges that have come to your attention.\",\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " 'So I closed my Shutterstock account after talking to a customer service agent. The service was not as advertised and I had no use for it, so it was closed and I was charged an exit fee. But I noticed that they have started billing me again, and the customer service agent I\\'m speaking to claims I *must* stay subscribed or pay a $60 exit fee. I\\'m preparing a complaint with the government better business organisation, but just wondering has anyone else had this happened to them? I was fully exited from the service and was receiving \"we miss you, come back and we\\'ll give you 15% off\" emails.\\n\\nI feel like Shutterstock is nowhere near as legit as their advertising material suggests, it\\'s outright fraud. I can\\'t even fucking log in to my Shutterstock because the account is closed and I\\'m being held at random. Shutterstock does not feel like a legit stock image service like Adobe and I regret ever giving Shutterstock any of my details. I feel like I\\'m in store for months of grief to settle this, as well as taking time to register complaint with the government and dealing with tribunals and stuff, it\\'s going to take a bit of time which I had no idea I\\'d need to commit to when I signed up last year.\\n\\nDoes this echo anyone else\\'s experience?',\n",
       " \"If I'm in the wrong place, I apologize.\\n\\nI'm trying to understand if I'm okay in this scenario: We have a standard license for an image. We use the image to create an original design (like a FB advertisement, generic to our industry). We have customers who want to use our original design. Does our standard license allow us to sell or share our original design? I've read the Shutterstock TOS a hundred times and I'm still not fully clear if I'm allowed to create original designs that contain stock images and sell them to other people. \",\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " 'Hello! I just share my Shutterstock portfolio here:\\n\\n[**T R A V E L A R I U M**](https://www.shutterstock.com/g/travelarium?rid=196665972&utm_medium=email&utm_source=ctrbreferral-link)\\n\\nYou can find and buy photos of different subjects: animals, dog sledding, travel, nature, landscapes, macro, some objects, industrial, some isolated photos and much more.\\n\\n\\u200b',\n",
       " 'Here is my Shutterstock Referral page!\\n\\n[https://www.shutterstock.com/g/RyanPaulTroy?rid=192126996&utm\\\\_medium=email&utm\\\\_source=ctrbreferral-link](https://www.shutterstock.com/g/RyanPaulTroy?rid=192126996&utm_medium=email&utm_source=ctrbreferral-link)',\n",
       " 'Had an idea of coordinating with providers to get some slightly more specific stock- or don’t you guys need it?',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " 'It would seem taht since Friday 16 Mar 2018 the API is broken. Just curious if anyone else is experiencing any issues with getting access. At first I programmed a brand new custom library for ShutterStock API to grant my coapny access. On friday that code stopped working. I spent the next days trying to figure out what changed.\\n\\nstdClass Object\\n(\\n    [message] => Validation failed\\n    [errors] => Array\\n        (\\n            [0] => stdClass Object\\n                (\\n                    [code] => VALIDATION_OBJECT_REQUIRED\\n                    [message] => Missing required property: client_id\\n                    [path] => $.body.client_id\\n                )\\n\\n        )\\n\\n)\\n\\nThat is the response that I get when requesting a Access Code just to get an Access Token. When I use the online ShutterStock forms at https://developers.shutterstock.com/oauth/apis/get/oauth/authorize I get the exact same response. It is no matter what Client ID I use. I can create a new app and use it and then get the same response. Prior to this, there were no problems but now the API is unusable. Any one else?',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " '',\n",
       " \"Hi, I came here to ask if anyone around here happens to use a Shutterstock Account where more than 1 people uses to download images and everyone that uses this account shares the price that you need to pay in order to keep the account living.\\n\\nIf there is, I'd willing to take part of this because I'm currently working as a graphic designer and Shutterstock helps me a lot to save work and time, and because paying an account all by myself is too much, Shutterstock and stock image services are overall too expensive for me to pay alone.\",\n",
       " '',\n",
       " 'This subreddit is dedicated to discussing websites such as shutterstock, iphoto or any other related websites in the stock photo/video domain. ']"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "postToList"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# joining all webscraped data into one list\n",
    "everything=postToList+a+top_level_comments"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'compound': 0.6818,\n",
      "  'headline': \"Let's look back at some memorable moments and interesting insights from last year.\\n\"\n",
      "              '\\n'\n",
      "              '**Your top 10 posts:**\\n'\n",
      "              '\\n'\n",
      "              '* \"[My Best and Worst Selling Photos and Images on '\n",
      "              'Shutterstock](https://www.youtube.com/watch?v=MLThFSU5OQ4)\" by '\n",
      "              '[u/NikoNomad](https://www.reddit.com/user/NikoNomad)\\n'\n",
      "              '* \"[Hmm](https://i.redd.it/1mt7osbefu441.jpg)\" by '\n",
      "              '[u/TheSexyCheeseGrader](https://www.reddit.com/user/TheSexyCheeseGrader)\\n'\n",
      "              '* \"[Watermark on images](/r/shutterstock/comments/dpzd6r/watermark_on_images/)\" by '\n",
      "              '[u/hawk16v](https://www.reddit.com/user/hawk16v)\\n'\n",
      "              '* \"[Hey guys I’m just starting off and would love if you can check my images and '\n",
      "              'maybe I can make a couple of bucks just in time for the holdays, thank you so much '\n",
      "              'if you even just glance I know it’s not a '\n",
      "              'lot.](https://www.shutterstock.com/g/Davis+Olive?rid=250198396&utm_medium=email&utm_source=ctrbreferral-link)\" '\n",
      "              'by [u/Virdian\\\\_](https://www.reddit.com/user/Virdian_)\\n'\n",
      "              '* \"[Shutterstock Is Latest Tech Company to Censor Itself for '\n",
      "              'China](https://theintercept.com/2019/11/06/shutterstock-china-censorship-tech/)\" by '\n",
      "              '[u/koavf](https://www.reddit.com/user/koavf)\\n'\n",
      "              '* \"[Problems with the model '\n",
      "              'release](/r/shutterstock/comments/ecuwka/problems_with_the_model_release/)\" by '\n",
      "              '[u/andybjpg](https://www.reddit.com/user/andybjpg)\\n'\n",
      "              '* \"[illustrations in jpeg and not '\n",
      "              'png?](/r/shutterstock/comments/e9m57j/illustrations_in_jpeg_and_not_png/)\" by '\n",
      "              '[u/johnpardon](https://www.reddit.com/user/johnpardon)\\n'\n",
      "              '* \"[can\\'t upload png illustrations but the site claims they do sell '\n",
      "              'them?](/r/shutterstock/comments/e6zkdi/cant_upload_png_illustrations_but_the_site_claims/)\" '\n",
      "              'by [u/johnpardon](https://www.reddit.com/user/johnpardon)\\n'\n",
      "              '* \"[BORDER DESIGN](http://www.shutterstock.com/en/image/image-1336157342)\" by '\n",
      "              '[u/jdk5051](https://www.reddit.com/user/jdk5051)\\n'\n",
      "              '* \"[Refferal Link](/r/shutterstock/comments/dunryx/refferal_link/)\" by '\n",
      "              '[u/HillarysFloppyChode](https://www.reddit.com/user/HillarysFloppyChode)',\n",
      "  'neg': 0.033,\n",
      "  'neu': 0.886,\n",
      "  'pos': 0.081},\n",
      " {'compound': 0.0, 'headline': '', 'neg': 0.0, 'neu': 0.0, 'pos': 0.0},\n",
      " {'compound': -0.6918,\n",
      "  'headline': \"Hi, I'm new to shutterstock and sotck photography in general. I did some pics of my \"\n",
      "              'hand holding my car keys and I sign the contract as the model and the photographer. '\n",
      "              \"I send the pics but it says the contract is wrong but it doesn't give me an \"\n",
      "              'explanation. So, I want to know if this is because maybe my handwriting was '\n",
      "              \"difficult to read for the AI or what I'm doing wrong.\\n\"\n",
      "              '\\n'\n",
      "              'Thanks.',\n",
      "  'neg': 0.137,\n",
      "  'neu': 0.77,\n",
      "  'pos': 0.093}]\n"
     ]
    }
   ],
   "source": [
    "#sentiment analysis \n",
    "from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA\n",
    "\n",
    "sia = SIA()\n",
    "results = []\n",
    "\n",
    "for line in everything:\n",
    "    pol_score = sia.polarity_scores(line)\n",
    "    pol_score['headline'] = line\n",
    "    results.append(pol_score)\n",
    "\n",
    "pprint(results[:3], width=100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>neg</th>\n",
       "      <th>neu</th>\n",
       "      <th>pos</th>\n",
       "      <th>compound</th>\n",
       "      <th>headline</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.033</td>\n",
       "      <td>0.886</td>\n",
       "      <td>0.081</td>\n",
       "      <td>0.6818</td>\n",
       "      <td>Let's look back at some memorable moments and ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.000</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.0000</td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.137</td>\n",
       "      <td>0.770</td>\n",
       "      <td>0.093</td>\n",
       "      <td>-0.6918</td>\n",
       "      <td>Hi, I'm new to shutterstock and sotck photogra...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.000</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.0000</td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.000</td>\n",
       "      <td>0.889</td>\n",
       "      <td>0.111</td>\n",
       "      <td>0.7278</td>\n",
       "      <td>do people want cutout jpeg stock illustrations...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     neg    neu    pos  compound  \\\n",
       "0  0.033  0.886  0.081    0.6818   \n",
       "1  0.000  0.000  0.000    0.0000   \n",
       "2  0.137  0.770  0.093   -0.6918   \n",
       "3  0.000  0.000  0.000    0.0000   \n",
       "4  0.000  0.889  0.111    0.7278   \n",
       "\n",
       "                                            headline  \n",
       "0  Let's look back at some memorable moments and ...  \n",
       "1                                                     \n",
       "2  Hi, I'm new to shutterstock and sotck photogra...  \n",
       "3                                                     \n",
       "4  do people want cutout jpeg stock illustrations...  "
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#saving result of the sentiment analysis into a dataframe \n",
    "df = pd.DataFrame.from_records(results)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['headline'].replace('', np.nan, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "df=df.dropna(subset=['headline'])\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>neg</th>\n",
       "      <th>neu</th>\n",
       "      <th>pos</th>\n",
       "      <th>compound</th>\n",
       "      <th>headline</th>\n",
       "      <th>label</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.033</td>\n",
       "      <td>0.886</td>\n",
       "      <td>0.081</td>\n",
       "      <td>0.6818</td>\n",
       "      <td>Let's look back at some memorable moments and ...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.137</td>\n",
       "      <td>0.770</td>\n",
       "      <td>0.093</td>\n",
       "      <td>-0.6918</td>\n",
       "      <td>Hi, I'm new to shutterstock and sotck photogra...</td>\n",
       "      <td>-1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.000</td>\n",
       "      <td>0.889</td>\n",
       "      <td>0.111</td>\n",
       "      <td>0.7278</td>\n",
       "      <td>do people want cutout jpeg stock illustrations...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>0.101</td>\n",
       "      <td>0.859</td>\n",
       "      <td>0.040</td>\n",
       "      <td>-0.7149</td>\n",
       "      <td>do they convert vector images to png?\\n\\ni exp...</td>\n",
       "      <td>-1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>0.000</td>\n",
       "      <td>1.000</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.0000</td>\n",
       "      <td>[https://www.shutterstock.com/g/Joseph98?rid=2...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>0.000</td>\n",
       "      <td>0.844</td>\n",
       "      <td>0.156</td>\n",
       "      <td>0.8426</td>\n",
       "      <td>I recently started contributing in Shutterstoc...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>0.047</td>\n",
       "      <td>0.953</td>\n",
       "      <td>0.000</td>\n",
       "      <td>-0.2846</td>\n",
       "      <td>every time I have a picture with a brand logo ...</td>\n",
       "      <td>-1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>0.000</td>\n",
       "      <td>1.000</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.0000</td>\n",
       "      <td>[http://www.shutterstock.com/g/ThatGermanGuy?r...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>0.253</td>\n",
       "      <td>0.648</td>\n",
       "      <td>0.099</td>\n",
       "      <td>-0.5423</td>\n",
       "      <td>I'm either too stupid or too blind. How can I ...</td>\n",
       "      <td>-1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>0.040</td>\n",
       "      <td>0.795</td>\n",
       "      <td>0.165</td>\n",
       "      <td>0.9256</td>\n",
       "      <td>I'm not sure if this belongs here, but all tha...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      neg    neu    pos  compound  \\\n",
       "0   0.033  0.886  0.081    0.6818   \n",
       "2   0.137  0.770  0.093   -0.6918   \n",
       "4   0.000  0.889  0.111    0.7278   \n",
       "5   0.101  0.859  0.040   -0.7149   \n",
       "8   0.000  1.000  0.000    0.0000   \n",
       "10  0.000  0.844  0.156    0.8426   \n",
       "11  0.047  0.953  0.000   -0.2846   \n",
       "14  0.000  1.000  0.000    0.0000   \n",
       "19  0.253  0.648  0.099   -0.5423   \n",
       "21  0.040  0.795  0.165    0.9256   \n",
       "\n",
       "                                             headline  label  \n",
       "0   Let's look back at some memorable moments and ...      1  \n",
       "2   Hi, I'm new to shutterstock and sotck photogra...     -1  \n",
       "4   do people want cutout jpeg stock illustrations...      1  \n",
       "5   do they convert vector images to png?\\n\\ni exp...     -1  \n",
       "8   [https://www.shutterstock.com/g/Joseph98?rid=2...      0  \n",
       "10  I recently started contributing in Shutterstoc...      1  \n",
       "11  every time I have a picture with a brand logo ...     -1  \n",
       "14  [http://www.shutterstock.com/g/ThatGermanGuy?r...      0  \n",
       "19  I'm either too stupid or too blind. How can I ...     -1  \n",
       "21  I'm not sure if this belongs here, but all tha...      1  "
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# obtaining sentiments for each line of comment on reddit\n",
    "df['label'] = 0\n",
    "df.loc[df['compound'] > 0.2, 'label'] = 1\n",
    "df.loc[df['compound'] < -0.2, 'label'] = -1\n",
    "df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Positive headlines:\n",
      "\n",
      "[\"Let's look back at some memorable moments and interesting insights from last year.\\n\"\n",
      " '\\n'\n",
      " '**Your top 10 posts:**\\n'\n",
      " '\\n'\n",
      " '* \"[My Best and Worst Selling Photos and Images on Shutterstock](https://www.youtube.com/watch?v=MLThFSU5OQ4)\" by [u/NikoNomad](https://www.reddit.com/user/NikoNomad)\\n'\n",
      " '* \"[Hmm](https://i.redd.it/1mt7osbefu441.jpg)\" by [u/TheSexyCheeseGrader](https://www.reddit.com/user/TheSexyCheeseGrader)\\n'\n",
      " '* \"[Watermark on images](/r/shutterstock/comments/dpzd6r/watermark_on_images/)\" by [u/hawk16v](https://www.reddit.com/user/hawk16v)\\n'\n",
      " '* \"[Hey guys I’m just starting off and would love if you can check my images and maybe I can make a couple of bucks just in time for the holdays, thank you so much if you even just glance I know '\n",
      " 'it’s not a lot.](https://www.shutterstock.com/g/Davis+Olive?rid=250198396&utm_medium=email&utm_source=ctrbreferral-link)\" by [u/Virdian\\\\_](https://www.reddit.com/user/Virdian_)\\n'\n",
      " '* \"[Shutterstock Is Latest Tech Company to Censor Itself for China](https://theintercept.com/2019/11/06/shutterstock-china-censorship-tech/)\" by [u/koavf](https://www.reddit.com/user/koavf)\\n'\n",
      " '* \"[Problems with the model release](/r/shutterstock/comments/ecuwka/problems_with_the_model_release/)\" by [u/andybjpg](https://www.reddit.com/user/andybjpg)\\n'\n",
      " '* \"[illustrations in jpeg and not png?](/r/shutterstock/comments/e9m57j/illustrations_in_jpeg_and_not_png/)\" by [u/johnpardon](https://www.reddit.com/user/johnpardon)\\n'\n",
      " '* \"[can\\'t upload png illustrations but the site claims they do sell them?](/r/shutterstock/comments/e6zkdi/cant_upload_png_illustrations_but_the_site_claims/)\" by '\n",
      " '[u/johnpardon](https://www.reddit.com/user/johnpardon)\\n'\n",
      " '* \"[BORDER DESIGN](http://www.shutterstock.com/en/image/image-1336157342)\" by [u/jdk5051](https://www.reddit.com/user/jdk5051)\\n'\n",
      " '* \"[Refferal Link](/r/shutterstock/comments/dunryx/refferal_link/)\" by [u/HillarysFloppyChode](https://www.reddit.com/user/HillarysFloppyChode)',\n",
      " \"do people want cutout jpeg stock illustrations? i mean the background becomes white right if it's in jpeg?\\n\"\n",
      " '\\n'\n",
      " \"it takes some time to transform my illustrations to vector. haven't figured out how to do it yet.\\n\"\n",
      " '\\n'\n",
      " 'but i somehow sold one image already. is it worth it to create jpeg illustrations with white backgrounds? or is there a way to upload png images?',\n",
      " 'I recently started contributing in Shutterstock. Do we need to really add watermark to our photos and upload? Or Shutterstock themselves will take care of the copyrights? Can anyone suggest me a '\n",
      " 'way to proceed with Shutterstock please. What else should I take care when I am a contributor and trying to find a niche out of it.....',\n",
      " \"I'm not sure if this belongs here, but all that google shows me is how to download stock photos for free. \\n\"\n",
      " '\\n'\n",
      " 'I am trying to download thousands of photos from my download history. These are photos I have licensed already. I want to download them (ideally with keywords in the metadata) to keep in a local '\n",
      " 'library of images. \\n'\n",
      " '\\n'\n",
      " 'Is there a service or program that does this? I found \"Shutter Library\" but I\\'m not sure if it\\'s trustworthy (this is a company account and I do not want to compromise the password).\\n'\n",
      " '\\n'\n",
      " 'Thanks!',\n",
      " \"If I'm in the wrong place, I apologize.\\n\"\n",
      " '\\n'\n",
      " \"I'm trying to understand if I'm okay in this scenario: We have a standard license for an image. We use the image to create an original design (like a FB advertisement, generic to our industry). We \"\n",
      " \"have customers who want to use our original design. Does our standard license allow us to sell or share our original design? I've read the Shutterstock TOS a hundred times and I'm still not fully \"\n",
      " \"clear if I'm allowed to create original designs that contain stock images and sell them to other people. \"]\n",
      "\n",
      "Negative headlines:\n",
      "\n",
      "[\"Hi, I'm new to shutterstock and sotck photography in general. I did some pics of my hand holding my car keys and I sign the contract as the model and the photographer. I send the pics but it says \"\n",
      " \"the contract is wrong but it doesn't give me an explanation. So, I want to know if this is because maybe my handwriting was difficult to read for the AI or what I'm doing wrong.\\n\"\n",
      " '\\n'\n",
      " 'Thanks.',\n",
      " 'do they convert vector images to png?\\n'\n",
      " '\\n'\n",
      " \"i export most of my illustrations into png. clip files are useless. can put them in illustrator and convert them to vector but that's too much work imo. \\n\"\n",
      " '\\n'\n",
      " 'the primary reason i wanted to do stock is because the market is filled with cold dead illustrator images. \\n'\n",
      " '\\n'\n",
      " \"i've been uploading to jpeg but i am not familiar with the format but it seems like you can't upload transparent backgrounds?\",\n",
      " 'every time I have a picture with a brand logo or name I get the image rejected because of it but when I search the thing in my picture on Shutterstock the logo and brand name are right in the '\n",
      " 'picture, why can some people post such pictures but I cant?',\n",
      " \"I'm either too stupid or too blind. How can I change the prices of my uploaded footage at Shutterstock Contributor?\\n\\n&#x200B;\\n\\nThanks and sorry.\",\n",
      " 'I get this error  \\n'\n",
      " '\"The size of your artwork (not the size of the artboard) must be at least 4 megapixels.\"\\n'\n",
      " '\\n'\n",
      " '&#x200B;\\n'\n",
      " '\\n'\n",
      " \"But the size of my file is 6mb... so what gives? I did resize the artboard, I don't know how else they expect this file to get bigger. I've uploaded here like a year ago, not sure why it's not \"\n",
      " 'working now.']\n"
     ]
    }
   ],
   "source": [
    "print(\"Positive headlines:\\n\")\n",
    "pprint(list(df[df['label'] == 1].headline)[:5], width=200)\n",
    "\n",
    "print(\"\\nNegative headlines:\\n\")\n",
    "pprint(list(df[df['label'] == -1].headline)[:5], width=200)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#stopwords and tokenizer for the word count\n",
    "stop_words = stopwords.words('english')\n",
    "tokenizer = RegexpTokenizer(r'\\w+')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "#function to tokenize and convert the words to lower character\n",
    "def process_text(headlines):\n",
    "    tokens = []\n",
    "    for line in headlines:\n",
    "        toks = tokenizer.tokenize(line)\n",
    "        toks = [t.lower() for t in toks if t.lower() not in stop_words]\n",
    "        tokens.extend(toks)\n",
    "    \n",
    "    return tokens"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('shutterstock', 25),\n",
       " ('com', 21),\n",
       " ('www', 15),\n",
       " ('https', 14),\n",
       " ('images', 12),\n",
       " ('u', 11),\n",
       " ('use', 11),\n",
       " ('reddit', 10),\n",
       " ('user', 10),\n",
       " ('photos', 9),\n",
       " ('stock', 8),\n",
       " ('image', 7),\n",
       " ('want', 6),\n",
       " ('download', 6),\n",
       " ('free', 6),\n",
       " ('month', 6),\n",
       " ('r', 5),\n",
       " ('comments', 5),\n",
       " ('time', 5),\n",
       " ('illustrations', 5)]"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#printing out the most frequent words from the positive sentiments\n",
    "pos_lines = list(df[df.label == 1].headline)\n",
    "\n",
    "pos_tokens = process_text(pos_lines)\n",
    "pos_freq = nltk.FreqDist(pos_tokens)\n",
    "\n",
    "pos_freq.most_common(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('shutterstock', 16),\n",
       " ('like', 8),\n",
       " ('get', 8),\n",
       " ('else', 5),\n",
       " ('access', 5),\n",
       " ('service', 5),\n",
       " ('use', 4),\n",
       " ('new', 3),\n",
       " ('give', 3),\n",
       " ('vector', 3),\n",
       " ('stock', 3),\n",
       " ('time', 3),\n",
       " ('picture', 3),\n",
       " ('brand', 3),\n",
       " ('size', 3),\n",
       " ('year', 3),\n",
       " ('billing', 3),\n",
       " ('account', 3),\n",
       " ('last', 3),\n",
       " ('back', 3)]"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#printing out the most frequent words from the negative sentiments\n",
    "neg_lines = list(df[df.label == -1].headline)\n",
    "\n",
    "neg_tokens = process_text(neg_lines)\n",
    "neg_freq = nltk.FreqDist(neg_tokens)\n",
    "\n",
    "neg_freq.most_common(20)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### word count plot for positive words"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "frequency_dist = nltk.FreqDist(pos_tokens)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "from wordcloud import WordCloud\n",
    "wordcloud = WordCloud(background_color=\"white\", contour_width=3, contour_color='steelblue').generate_from_frequencies(frequency_dist)\n",
    "plt.imshow(wordcloud)\n",
    "plt.axis(\"off\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### tokenizing the data and using random forest classifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df2 = df[['headline', 'label']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "metadata": {},
   "outputs": [],
   "source": [
    "# store simplified data in X and y\n",
    "X = df2['headline']\n",
    "y = df2['label']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 218,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 219,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.datasets import load_files"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [],
   "source": [
    "tvec = TfidfVectorizer(stop_words='english', max_features=1000, ngram_range=[1,2])\n",
    "X_train_tvec = tvec.fit_transform(X_train)\n",
    "X_test_tvec = tvec.transform(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['shutterstock', 'com', 'stock', 'use', 'shutterstock com', 'photos', 'www', 'don', 'https', 'image', 'good', 'just', 'stocksy', 'need', 'time']\n"
     ]
    }
   ],
   "source": [
    "indices = np.argsort(tvec.idf_)[::]\n",
    "features = tvec.get_feature_names()\n",
    "top_n = 15\n",
    "top_features = [features[i] for i in indices[:top_n]]\n",
    "print(top_features)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### utilizing random forest classification"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/jupyterlab/conda/envs/python/lib/python3.6/site-packages/sklearn/ensemble/forest.py:246: FutureWarning: The default value of n_estimators will change from 10 in version 0.20 to 100 in 0.22.\n",
      "  \"10 in version 0.20 to 100 in 0.22.\", FutureWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',\n",
       "            max_depth=None, max_features='auto', max_leaf_nodes=None,\n",
       "            min_impurity_decrease=0.0, min_impurity_split=None,\n",
       "            min_samples_leaf=1, min_samples_split=2,\n",
       "            min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=None,\n",
       "            oob_score=False, random_state=None, verbose=0,\n",
       "            warm_start=False)"
      ]
     },
     "execution_count": 141,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rf = RandomForestClassifier()\n",
    "rf.fit(X_train_tvec,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.6904761904761905"
      ]
     },
     "execution_count": 142,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rf.score(X_test_tvec, y_test)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python",
   "language": "python",
   "name": "conda-env-python-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
