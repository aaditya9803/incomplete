from bs4 import *

with open("beautiful soup\website.html", encoding="utf-8") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents,"html.parser")
all_a_tags = soup.find_all(name="a")
print(all_a_tags)