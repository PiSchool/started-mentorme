from bs4 import BeautifulSoup as bs
from cleantext import clean
from langdetect import detect

def form_elements(soup):
    form_count = 0
    input_count = 0
    for form in soup.find_all("form"):
        form_count += 1
        for input_element in form.find_all("input"):
            input_count += 1
    return form_count, input_count

def img_elements(soup):
    return len(soup.find_all("img",{"src":True}))

def getHtmlFea(soup):
    fc, ic = form_elements(soup)
    im = img_elements(soup)
    return fc, ic, im

def checkEnglish(text):
    if detect(text) == 'en': return text
    return ''

def getEnglishText(soup):
    try:
        for script in soup(["script", "style"]): script.extract()
        rawtext = soup.get_text()
        s = '\n'.join([line.strip() for line in rawtext.splitlines() if len(line.strip()) > 0])
        return checkEnglish(s)
    except Exception as e: pass
    return  ''

def extractFeature(html):
    try:
        soup = bs(html, "html.parser")
        fc, ic, im = getHtmlFea(soup)
        text = getEnglishText(soup)
        return fc, ic, im, text
    except Exception as e: pass
    return 0,0,0,'',''


