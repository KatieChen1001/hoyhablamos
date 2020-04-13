from bs4 import BeautifulSoup
import requests

session = requests.Session()

podcast_diario_link =[]
for page_num in range(24,140):
    diario_url =  "https://www.hoyhablamos.com/category/podcast/page/" + str(page_num) + "/"
    r = session.get(diario_url)
    soup = BeautifulSoup(r.content, 'lxml')
    for link in soup.find_all('a', attrs={'class': 'entry-image-link'}):
        podcast_diario_link.append(link['href'])

with open("pdf_link.py", 'w') as file:
    for link in podcast_diario_link:
        file.write('\"' + link + '\"' + ', ')
