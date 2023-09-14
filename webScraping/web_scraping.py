from bs4 import BeautifulSoup

import requests

url = "https://www.newegg.com/p/pl?d=graphics+cards"

# contents of url is stored in result
result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')

prices = doc.find_all(string='$')


parent = prices[0].parent
strong = parent.find_all("strong")

print(strong.string)
