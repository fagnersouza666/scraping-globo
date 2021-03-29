import requests
from bs4 import BeautifulSoup as bs

#Pegando os dados da página
req = requests.get('https://www.globo.com/')

#acesso à página foi feita com sucesso
if req.status_code == 200:

	#Utiliza BS4 e pega toda arvore do HTML
	bsHtml = bs(req.text, 'html.parser')

	#Procura a primeira tag <h3> que tenha a 
	#classe highlight__title
	linha = bsHtml.find('h3',{'class':{'highlight__title'}})

	#exibe no console
	print(linha.getText())


















