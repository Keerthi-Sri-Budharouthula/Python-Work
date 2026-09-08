import requests
from bs4 import BeautifulSoup

URL ='https://codegnan.com/'

#loading the webpage in memory using requests library
page = requests.get(URL)

#check status code of the page
page.status_code

htmlCode=page.text
print(htmlCode)

soup=BeautifulSoup(htmlCode,'html.parser')
print(soup)

title = soup.title.text
print("Website Title:", title)

headings = soup.find_all("h3")
for heading in headings:
    print(heading.text.strip())

links = soup.find_all("a")
for link in links[:10]:     #first 10 links
    print(link.get("href"))

images = soup.find_all("img")
for image in images[:10]:
    print(image.get("src"))

description = soup.find("meta", attrs={"name": "description"})
if description:
  print("Description:")
  print(description.get("content"))

for tag in soup.find_all():
  if tag.get("class"):
    print(tag.get("class"))

scripts = soup.find_all("script")
for script in scripts:
    print(script.get("src"))

logo = soup.find("img")
print(logo.get("src"))

og_image = soup.find("meta", attrs={"property": "og:image"})

print(og_image["content"])


meta_tags = soup.find_all("meta")
for tag in meta_tags:
    print(tag.get("name"))

menus = soup.find_all("li")
for menu in menus:
    print(menu.text.strip())

paragraphs = soup.find_all("p")
for p in paragraphs[:10]:
    print(p.text.strip())

buttons = soup.find_all("button")
for button in buttons:
    print(button.text.strip())