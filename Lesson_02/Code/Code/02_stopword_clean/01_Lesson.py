
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
html='<h2 class="block-title">news</h2>'
soup = BeautifulSoup(html, 'lxml')
soup.get_text()


# In[3]:


import nltk
nltk.download()
nltk.download('punkt')


# In[4]:


from nltk import sent_tokenize
# load data
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
# split into sentences
sentences = sent_tokenize(text)
print(sentences[0])


# In[5]:


from nltk.tokenize import word_tokenize
# load data
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
# split into words
tokens = word_tokenize(text)
print(tokens[:100])


# In[6]:


from nltk.tokenize import word_tokenize
# load data
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
# split into words
tokens = word_tokenize(text)
# remove all tokens that are not alphabetic
words = [word for word in tokens if word.isalpha()]
print(words[:100])


# In[7]:


from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = stopwords.words('english')
print(stop_words)
# chinese
#https://github.com/dongxiexidian/Chinese/blob/master/stopwords.dat


# In[8]:


import string
# regular expression
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# load data
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
print(text)


# In[12]:


# split into words
tokens = word_tokenize(text)
# convert to lower case
tokens = [w.lower() for w in tokens]
print(tokens)


# In[10]:


# prepare regex for char filtering
re_punc = re.compile('[%s]' % re.escape(string.punctuation))
print(re_punc)


# In[15]:


# remove punctuation from each word
print(re_punc.sub(' ha', 'i\'ve'))
stripped = [re_punc.sub('', w) for w in tokens]
print(stripped)


# In[17]:


# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]
# filter out stop words
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
print(words[:100])
print(len(words))


# In[20]:


from nltk.stem.porter import *
stemmer = PorterStemmer()
print(stemmer.stem('identified'))
print(stemmer.stem('nonsensical'))


# In[18]:


from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
# load data
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
# split into words
tokens = word_tokenize(text)
print(tokens[:100])


# In[19]:


# stemming of words
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in tokens]
print(stemmed[:100])

