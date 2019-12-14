from web_functions import crawlData
from feature_extractor import extractFeature
from text_functions import processText, clean_txt
from feature_union_transformer import *
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
import pickle

with open('pipeline.pkl', 'rb') as data:
    pipe = pickle.load(data)

with open('clf.pkl', 'rb') as data:
    clf = pickle.load(data)

clmns = ['text', 'img_count', 'input_count', 'polarity', 'subjectivity', 'len']

def isaStartup(url):
    global pipe, clf, clmns
    html, a_html, nil = crawlData(url)
    _, ic, im, text = extractFeature(html)
    _, _, _, a_text = extractFeature(a_html)
    text = ' '.join([text, a_text])
    pol, sub, len = processText(text)
    test_vec = pipe.transform(pd.DataFrame([[text, im, ic, pol, sub, len]], columns=clmns))
    return clf.predict(test_vec)

print(isaStartup('http://www.inscribe.ai'))