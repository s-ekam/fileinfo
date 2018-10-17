import requests
from bs4 import BeautifulSoup as bs

x = requests.get("https://fileinfo.com/extension/pdf")
# print(x.content)

soup = bs(x.content,'html.parser')
pret = soup.prettify()
# ls = list(soup.children)
# ls = str(ls)
# # print(ls)
# z = '\n\n\n'.join(ls)
# print(z)
# <p><span itemprop="description">
desc = soup.find_all('p')
str_desc = str(desc[1])
# print(pret)
typ = soup.find_all('a')
# c =0
# for x in z:
# 	print(c,end="  ")
# 	print(x)
# 	c = c+1
# print(z)

str_typ = str(typ[10])

print(str_typ[33:-4])
print(str_desc[32:-12])