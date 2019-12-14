import re
import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from nltk.corpus import stopwords

from textblob import TextBlob

"""
Uncomment the first time!
"""
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('averaged_perceptron_tagger')

stop_words_ = set(stopwords.words('english'))
wn = WordNetLemmatizer()

my_sw = ['please', 'run', 'javascript', 'make', 'amp', 'news', 'new', 'time', 'u', 's', 'photos', 'get', 'say']

def black_txt(token):
    return token not in stop_words_ and token not in list(string.punctuation) and len(token) > 2 and token not in my_sw

def clean_txt(text):
    clean_text = []
    clean_text2 = []
    text = re.sub("'", "", text)
    text = re.sub("(\\d|\\W)+", " ", text)
    clean_text = [wn.lemmatize(word, pos="v") for word in word_tokenize(text.lower()) if black_txt(word)]
    clean_text2 = [word for word in clean_text if black_txt(word)]
    return " ".join(clean_text2)

def polarity_txt(text): return TextBlob(text).sentiment[0]

def subj_txt(text): return TextBlob(text).sentiment[1]

def len_text(text):
  l = len(text.split())
  if l>0: return len(set(clean_txt(text).split()))/ l
  else: return 0

def processText(text):
    pol = polarity_txt(text)
    sub = subj_txt(text)
    len = len_text(text)
    return pol, sub, len
