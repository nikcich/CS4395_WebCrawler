# from urllib import request

# url = "https://en.wikipedia.org/wiki/Breaking_Bad"

# with request.urlopen(url) as f:
#     raw = f.read().decode('utf-8-sig')
# print("len=", len(raw))
# print(raw[:200])



from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Vince_Gilligan"

r = requests.get(url)

data = r.text
soup = BeautifulSoup(data, features="html.parser")

counter = 0
with open('urls.txt', 'w') as f:
    for link in soup.find_all('a'):
        link_str = str(link.get('href'))
        #print(link_str)
        if 'Gilligan' in link_str or 'gilligan' in link_str:
            if link_str.startswith('/url?q='):
                link_str = link_str[7:]
                print('MOD:', link_str)
            if '&' in link_str:
                i = link_str.find('&')
                link_str = link_str[:i]
            if link_str.startswith('http') and 'google' not in link_str:
                f.write(link_str+'\n')

print("END")

with open('urls.txt', 'r') as f:
    urls = f.read().splitlines()
for u in urls:
    print(u)

