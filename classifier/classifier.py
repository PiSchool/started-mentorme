from web_functions import crawlData
from feature_extractor import extractFeature
from text_functions import processText, clean_txt
from feature_union_transformer import *
from colorama import init
from colorama import Fore, Back, Style

import pandas as pd

import pickle
import argparse
import validators

with open('pipeline.pkl', 'rb') as data:
    pipe = pickle.load(data)

with open('clf.pkl', 'rb') as data:
    clf = pickle.load(data)

clmns = ['text', 'img_count', 'input_count', 'polarity', 'subjectivity', 'len']

def isaStartup(url):
    init()
    global pipe, clf, clmns
    html, a_html, nil = crawlData(url)
    _, ic, im, text = extractFeature(html)
    _, _, _, a_text = extractFeature(a_html)
    text = ' '.join([text, a_text])
    pol, sub, len = processText(text)
    test_vec = pipe.transform(pd.DataFrame([[text, im, ic, pol, sub, len]], columns=clmns))
    return clf.predict(test_vec)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Startup/Not Startup classifier given a url')
    parser.add_argument('website_string', metavar='website_url', type=str,
                        help='a url of a website (possibly a company website)')
    args = parser.parse_args()
    url = args.website_string
    if not validators.url(url):
        print(Fore.RED + "Please insert a valid url")
    print(Fore.CYAN + "Checking website, please wait...")
    startup = isaStartup(url)
    if startup:
        print(Fore.GREEN + "According to our classifier, your website is a startup!")
    else:
        print(Fore.RED +  "According to our classifier, your website is NOT a startup")



