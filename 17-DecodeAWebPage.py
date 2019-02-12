import requests

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(r_html,'lxml')
titles=soup.find_all('div',{'class':"css-1j836f9 esl82me3"})

for title in titles:
    print (title.get_text())