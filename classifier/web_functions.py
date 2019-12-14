from bs4 import BeautifulSoup, SoupStrainer
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests

about_terms = ['about', 'aboutus', 'about-us']
target_terms = about_terms
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',}

def getHtml(url):
    try:
        html = requests.get(url, verify=False, timeout=10)
        if html.status_code == 200: return html.content
    except Exception as e: pass
    return ''

def isaTargetLink(url):
    url = url.lower()
    for t in (target_terms):
        if url.endswith(t): return True
    return False

def checkList(url, link):
    if link.startswith(url): return link
    elif link.startswith('/'):
        if url.endswith('/'): return url + link[1:]
        else: return url + link
    return None

def get_internal_links(url, html):
    l = set()
    for link in BeautifulSoup(html, 'html.parser', parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            curr_link = checkList(url, link['href'])
            if curr_link and isaTargetLink(curr_link): l.add(curr_link)
    return l

"""
crawlData returns a tuple made by 
    (html_source, about_page_source, numb_of_internal_link)
"""
def crawlData(url):
    a = ''
    html = getHtml(url)
    il = get_internal_links(url, html)
    nil = len(il)
    if nil>0:
        al = min(il, key=len)
        a = getHtml(al)
    return (html, a, nil)