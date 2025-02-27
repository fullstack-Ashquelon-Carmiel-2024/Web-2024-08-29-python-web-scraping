from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The first paragraph</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

## Get Title Tag
print(soup.find('title'))
# --> <title>The Dormouse's story</title>

## Get Title Tag Inner Text
print(soup.find('title').get_text())
# -->  "The Dormouse's story"

## Get First Paragraph
print(soup.find('p'))
# --> <p class="title"><b>The Dormouse's story</b></p>

## Get First <a> Tag
print(soup.find('a'))
# --> <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

## Get All <a> Tags
print(soup.find_all('a'))
# --> [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
