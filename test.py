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
z = soup.find_all('p')
st = str(z[1])
# print(pret)
z = soup.find_all('a')
# c =0
# for x in z:
# 	print(c,end="  ")
# 	print(x)
# 	c = c+1
# print(z)

st2 = str(z[10])

print(st2[33:-4])
print(st[32:-12])