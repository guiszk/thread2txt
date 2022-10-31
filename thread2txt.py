from bs4 import BeautifulSoup as bs
import requests

def gettxt(url):
    url = str(url).replace('twitter.com', 'nitter.it')
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')

    alltxt = []

    for i in soup.findAll('div', {'class':'tweet-content'}):
        alltxt.append(i.text)

    with open("results.txt", 'w') as f:
        for i in alltxt:
            f.write(i)
            f.write('\n')

    return alltxt