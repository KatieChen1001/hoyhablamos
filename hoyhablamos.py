from bs4 import BeautifulSoup
import requests

# Scrape data behind site logins
# get all the links for individual article on page one of "podcast diario"
# after page one, auto increase page number to get the links of other pages
# visit all links


# Start the session
session = requests.Session()

headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36'
}
url = "https://www.hoyhablamos.com/wp-login.php"

login_data = {
    'log': 'K80Chen',
    'pwd': 'hablamoshoy',
    'wp-submit': 'Acceder',
    'redirect_to': 'https://www.hoyhablamos.com/824-coronavirus/'
}
r = session.post(url, data = login_data, headers = headers)
r = session.get("https://www.hoyhablamos.com/824-coronavirus/")
soup = BeautifulSoup(r.content, 'lxml')
pdf_link = soup.find('a', attrs={'rel': 'noopener noreferrer'})['href']
print(pdf_link)

response = requests.get(pdf_link)

with open('soup.pdf', 'wb') as f:
    f.write(response.content)
