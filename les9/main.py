from urllib import request
import requests
from bs4 import BeautifulSoup
# opener = request.build_opener()
#
# response = opener.open("https://mystat.itstep.org")
#
# print(response.read())
#
# resp = requests.get("https://mystat.itstep.org/")
#
# print(resp.content)
#
# print(resp.text)


# payload = {'key1': 'value1', 'key2': 'value2'}
#

url = 'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

b = soup.find_all('div', "main-block")
print(b)