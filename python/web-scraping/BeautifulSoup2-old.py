from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.wikipedia.org/')
bs = BeautifulSoup(html, "html.parser")
nameList = bs.findAll('a', {'class' : 'link-box'})
for name in nameList:
  print(name.get_text())
  