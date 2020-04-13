from bs4 import BeautifulSoup
import requests
import page_link

session = requests.Session()

headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36'
}
# Get API endpoint from <form action = "" on login page>
url = "https://www.hoyhablamos.com/wp-login.php"
# Get POST request data from inspector -> network -> login URL (wp-login.php) -> Form Data
login_data = {
    'log': 'K80Chen',
    'pwd': 'hablamoshoy',
    'wp-submit': 'Acceder',
    'redirect_to': 'https://www.hoyhablamos.com/824-coronavirus/'
}
# POST request to login URL with login data and header info
r = session.post(url, data = login_data, headers = headers)

links = ["https://www.hoyhablamos.com/premium-1-presentamos-el-nuevo-podcast-premium-de-hoy-hablamos/",
"https://www.hoyhablamos.com/696-noticias-en-espanol/",
"https://www.hoyhablamos.com/695-expresiones-con-el-verbo-entrar/",
"https://www.hoyhablamos.com/694-la-guardia-civil/"]

pdf_links = []

for link in links:
    r = session.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    try:
        pdf_link = soup.find('a', attrs={'rel': 'noopener noreferrer'})['href']
        pdf_links.append(pdf_link)
    except(TypeError, KeyError) as e:
        pass

print(pdf_links)

logout_url = 'https://www.hoyhablamos.com/wp-login.php?action=logout&redirect_to=https%3A%2F%2Fwww.hoyhablamos.com&_wpnonce=4590a2e413'
r = session.post(url, headers = headers)

r = session.get(links[0])
soup = BeautifulSoup(r.content, 'lxml')
pdf_link = soup.find('a', attrs={'rel': 'noopener noreferrer'})['href']
print(pdf_link)
