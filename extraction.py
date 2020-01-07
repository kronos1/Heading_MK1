from datetime import datetime
import requests
import re
from bs4 import BeautifulSoup



def scrape_headings():
    """
    Return all headings from a given URL
    :return:
    """

    url = input("What website would you like to crawl? ")

    start_time = datetime.now()

    html = requests.get("https://" + url).content

    unicode_str = html.decode("utf8")
    encoded_str = unicode_str.encode("ascii", 'ignore')
    news_soup = BeautifulSoup(encoded_str, "html.parser")

    headings = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']

    h1 = news_soup.find_all(headings[0])
    h2 = news_soup.find_all(headings[1])
    h3 = news_soup.find_all(headings[2])
    h4 = news_soup.find_all(headings[3])
    h5 = news_soup.find_all(headings[4])
    h6 = news_soup.find_all(headings[5])

    y = [re.sub(r'<.+?>', r'', str(a)) for a in (h1, h2, h3, h4, h5, h6)]

    for list_item in y:
        print(list_item)



scrape_headings()
