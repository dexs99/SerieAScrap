from bs4 import BeautifulSoup
from requests import get

URL = "http://www.legaseriea.it/it/serie-a-tim/squadre/atalanta/squadra"

response = get(URL)
html_soup = BeautifulSoup(response.text, 'html.parser')

contenedor = html_soup.find_all('table', class_ = 'tabella colonne9')

primeratabla = contenedor[0]

jugadores = primeratabla.find_all('tr')
tope = len(jugadores)

for i in range(1, tope): 
	primerjugador = jugadores[i]

	datos =  primerjugador.find_all('td')

	numero = datos[0].text

	jugador = datos[1].span.text

	fechanac = datos[2].text

	rol = datos[3].text

	nacion = datos[4].find('img')
	nacion = nacion['title']

	partidosjugados = datos[5].text

	goles = datos[6].text
	goles = goles.strip()

	amarillas = datos[7].text

	amarillasrojas = datos[8].text
	
	rojas = datos[9].text

	print(numero + "\t" + jugador + "\t" + fechanac + "\t" + rol + "\t" + nacion + "\t" + partidosjugados + "\t" + goles + "\t" + amarillas + "\t" + amarillasrojas + "\t" + rojas + "\n")
