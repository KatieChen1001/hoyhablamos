from bs4 import BeautifulSoup
import requests
import page_link

## Start the session
session = requests.Session()

# ===== I. LOGIN ===== ##

# Get header info from Chrome inspector -> network
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



# ===== II. Get individual podcast page link ===== ##
# 1.PODCAST DIARIO
# 2.PODCAST PREMIUM
# 3.PODCAST GRAMATICA

# Navigate to PODCAST DIARIO


pdf_links = []

for link in page_link.page_link:
    r = session.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    try:
        pdf_link = soup.find('a', attrs={'rel': 'noopener noreferrer'})['href']
        pdf_links.append(pdf_link)
    except(TypeError, KeyError) as e:
        pass

with open ("253_pdf_links.py", 'w') as f:
    for pdf_link in pdf_links:
        f.write('\"' + pdf_link + '\"' + ', ')

for pdf_link in pdf_links:
    pdf_content = session.get(pdf_link)
    pdf_name = pdf_link[58:len(pdf_link)]
    with open(pdf_name, 'wb') as f:
        f.write(pdf_content.content)

logout_url = 'https://www.hoyhablamos.com/wp-login.php?action=logout&redirect_to=https%3A%2F%2Fwww.hoyhablamos.com&_wpnonce=4590a2e413'
r = session.post(url, headers = headers)
