import requests
from bs4 import BeautifulSoup as bs

x = requests.get("https://fileinfo.com/extension/cpp")
# print(x.content)

soup = bs(x.content,'html.parser')
# pret = soup.prettify()
# ls = list(soup.children)
# ls = str(ls)
# # print(ls)
# z = '\n\n\n'.join(ls)
# print(z)
# <p><span itemprop="description">
z = soup.find_all('p')
st = str(z[1])
print(st[32:-12])
