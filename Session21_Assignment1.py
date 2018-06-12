from bs4 import BeautifulSoup
import urllib.request
import nltk
from collections import Counter
from string import punctuation
from nltk.tokenize import RegexpTokenizer
import seaborn as sns
import matplotlib.pyplot as plt


response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text()

tokenizer = RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(text)
words = []
for word in tokens:
    words.append(word.lower())
sw = nltk.corpus.stopwords.words('english')
words_ns = []

for word in words:
    if word not in sw:
        words_ns.append(word)

%matplotlib inline
sns.set()

freqdist1 = nltk.FreqDist(words_ns)
freqdist1.plot(25)
