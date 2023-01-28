from bs4 import BeautifulSoup
import requests

res = requests.get('https://top40weekly.com/all-us-top-40-singles-for-2023/#January')
#print(res.text)
soup = BeautifulSoup(res.content,'html.parser')
page_title = soup.title.text
#print(page_title)

page_body = soup.body
#print(page_body)

text = soup.get_text()
#print(text)

jan7 = text.split('JANUARY 7',1)[0]
print(jan7)