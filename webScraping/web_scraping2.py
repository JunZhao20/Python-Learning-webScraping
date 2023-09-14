from bs4 import BeautifulSoup
import re

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tag = doc.find_all(["p", "div", "li"])

tag2 = doc.find_all(["option"], text="Undergraduate",
                    value='undergraduate', class_="btn-item")

# re.compile grabs the expression of any tag, attribute etc
tag3 = doc.find_all(text=re.compile("\$.*"), limit=1)

tag4 = doc.find_all("input", type="text")
for tag in tag4:
    tag['placeholder'] = 'i changed you'

with open("index.html", "w") as file:
    file.write(str(doc))
