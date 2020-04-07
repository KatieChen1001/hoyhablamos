from bs4 import BeautifulSoup
import requests

## Start the session
session = requests.Session()

## ===== I. LOGIN ===== ##

## Get header info from Chrome inspector -> network
# headers = {
#     'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36'
# }
## Get API endpoint from <form action = "" on login page>
# url = "https://www.hoyhablamos.com/wp-login.php"
## Get POST request data from inspector -> network -> login URL (wp-login.php) -> Form Data
# login_data = {
#     'log': 'K80Chen',
#     'pwd': 'hablamoshoy',
#     'wp-submit': 'Acceder',
#     'redirect_to': 'https://www.hoyhablamos.com/824-coronavirus/'
# }
## POST request to login URL with login data and header info
# r = session.post(url, data = login_data, headers = headers)




## ===== II. Get individual podcast page link ===== ##
## 1.PODCAST DIARIO
## 2.PODCAST PREMIUM
## 3.PODCAST GRAMATICA

## Navigate to PODCAST DIARIO
page_num = 2
diario_starter_url = "https://www.hoyhablamos.com/category/podcast/page/1/"
diario_next_url =  "https://www.hoyhablamos.com/category/podcast/page/" + str(page_num) + "/"
if page_num <= 139:

    page_num = page_num + 1

r = session.get(diario_url)
soup = BeautifulSoup(r.content, 'lxml')




# get all links on page 1

# navigate to page 2: https://www.hoyhablamos.com/category/podcast/page/2/

# for every link gathered go to the link page, and then find the pdf link on the page:
# pdf_link = soup.find('a', attrs={'rel': 'noopener noreferrer'})['href']

# visit pdf link page and then download it as a pdf






podcast_diario_link =[]
for link in soup.find_all('a', attrs={'class': 'entry-image-link'}):
    podcast_diario_link.append(link['href'])
    session.get(link['href'])
    with open('/tmp/metadata.pdf', 'wb') as f:
    f.write(response.content)
print(podcast_diario_link)
