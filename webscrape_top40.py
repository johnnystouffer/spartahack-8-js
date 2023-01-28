from bs4 import BeautifulSoup
import requests
from string import digits
res = requests.get('https://top40weekly.com/all-us-top-40-singles-for-2023/#January')
#print(res.text)
soup = BeautifulSoup(res.content,'html.parser')
page_title = soup.title.text
#print(page_title)

page_body = soup.body
#print(page_body)

text = soup.get_text()
text = str(text)
#print(text)
print(text.index("US Top 40 Singles – JANUARY 7, 2023"))
print(text.index("THIS WEEK’S DROP – JANUARY 7, 2023"))

text = text[1782:4676]


# #print(type(text))
# #text = text.split("(")
# text = str(text)
# text = text.split('–•–')
# print(text)

newtext = text.translate({ord(k): None for k in digits})
#print(type(text))
newtext = newtext.split("()")
newtext = str(newtext)
newtext = newtext.split('–•–')
print(newtext)