import requests
from bs4 import BeautifulSoup

url = 'https://g1.globo.com/'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.feed-post-body'):
    titulo = pergunta.select_one('.feed-post-link')
    print(titulo.text)
