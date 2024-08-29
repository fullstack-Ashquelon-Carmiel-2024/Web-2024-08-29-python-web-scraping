import requests
from bs4 import BeautifulSoup

url1 = 'https://www.amazon.com/PINECIL-%D7%9E%D7%9C%D7%97%D7%9D-%D7%9E%D7%99%D7%A0%D7%99-%D7%A0%D7%99%D7%99%D7%93-%D7%97%D7%9B%D7%9D/dp/B096X6SG13/ref=pd_rhf_d_ee_s_pd_crcd_sccl_1_2/147-7057278-1801918?pd_rd_w=nz0Rb&content-id=amzn1.sym.840d50bc-9f73-460b-8793-15925b0bb70e&pf_rd_p=840d50bc-9f73-460b-8793-15925b0bb70e&pf_rd_r=RHFR6185PRJTX2DHWJTZ&pd_rd_wg=BDbW2&pd_rd_r=0836b360-f62e-41fc-b564-9b03e83ee398&pd_rd_i=B096X6SG13&psc=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

response = requests.get(url1, headers=headers)

webpage = response.content

print(response.status_code)

# create BeautifulSoup object (we could use different parsers)
soup = BeautifulSoup(webpage,"html.parser")

# Seeing the whole HTML with indentation
print(soup.prettify())

# Seeing the soup object properties by tag names (tag name brings only the first element
#   with this tag name)
#print(soup.body.prettify())
#print(soup.head.prettify())
#print(soup.p.prettify())

# Shows all the children of <head> as a list, but with "new line" characters
# between them. 
# print(soup.head.contents)

# To see only one child:
#print(soup.head.contents[1])
#print(soup.head.contents[3])

#And to see child's name:
#print(soup.head.contents[1].name)
#print(soup.head.contents[3].name)

# We can see also all the children of "soup" as this list - and they are only <html>:
# print(soup.contents[1])

# Using .children generator
# for child in soup.body.children:
#     if (child != '\n'):
#         print(child)

#or
# for child in soup.body.children:
#     if (child != '\n'):
#         print(child.name)

# "descendants" mean not only the children, but also the children of the children
# children = [child for child in soup.head.children if child != '\n']
# descendants = [desc for desc in soup.head.descendants if desc != '\n']
# print(len(children))
# print(len(descendants))
# print(children)
# print(descendants)
# In the case of <title> for example, it's text node is a child

# Using .parent:
# print(soup.title.parent)
# print(soup.title.parent.name) # it's "document"

# print(soup.html.parent) # yes, it's a whole document
# print(type(soup.html.parent)) #<class 'bs4.BeautifulSoup'>
# print(soup.parent) #None

# Using .parents:
# for parent in soup.p.parents:
#     print(parent.name)
# The result is : body
#                 html
#                 [document]

# Using .next_sibling and .previous_sibling:
# <p>This paragraph has a <b>bold</b> text. </p>
# "This paragraph has a " - is a previous sibling of <b>
# " text. " - is a next sibling of <b>

""" print(soup.b.next_sibling)
print(soup.b.previous_sibling) """

# Using .next_siblings and .previous_siblings

""" for sibling in soup.img.previous_siblings:
    print(sibling) """

# Navigable strings. If we don't want tags to be displayed

""" print(soup.title.string) # it works for one string only
# if there is more than one string, it won't work and will got "None", like here:
print(soup.body.string) """ # interpreter cannot decide which string is mentioned

""" for string in soup.body.strings:
    print(string) """
    
# there are too many white spaces between the strings, so we'll use .stripped_strings:
""" for string in soup.body.stripped_strings:
    print(string) """
    
# .find_all()
""" print(soup.find_all('p')) # we've got all the instances of 'p' in a list 

print(soup.find_all('p')[1]) # extracting the second "p" tag
print(soup.find_all('p')[1].string) 
print(soup.find_all('p')[1].text) # the same as .string

print(soup.find_all('div', class_ = 'myDiv')) #we also could use key-value pairs  """
    # in the searches with ".find_all()" and ".find()", like here:
    
""" print(soup.find_all('div', {'class':'myDiv'})) """

# if there would be more than one class for example:
""" print(soup.find_all('div', {'class':'myDiv','class':'myDiv2'})) """

# id should not have an underscore as class had:
""" print(soup.find_all('table', id = 'blogs')) """

# we could find the elements by the list of tags, like:
""" print(soup.find_all(['div','img'])) """

# .find_all got an attribute that can limit amount of instances of the given tag:
""" print(soup.find_all('p',limit = 2)) """

# soup.find('p') brings only the first <p> like soup.p does, but we can 
# use in .find() more identifiers, like in .find_all():
""" print(soup.find('p',class_ = 'myDiv2')) """