from bs4 import BeautifulSoup
from requests import get

URL = "http://www.legaseriea.it/it/serie-a-tim/squadre/atalanta/squadra"

response = get(URL)
#print(response.text[:500])
#la sentencia de arriba sirve para ver las primeras 500 letras de lo que has extraido de la pagina
html_soup = BeautifulSoup(response.text, 'html.parser')

contenedor = html_soup.find_all('table', class_ = 'tabella colonne9')
#la sentencia de arriba sirve para capturar todas las tablas presentes en la pagina
#print(type(contenedor))
#print(len(contenedor))

primeratabla = contenedor[0]
#print(type(primeratabla))
#print(len(primeratabla))
#print(primeratabla)

jugadores = primeratabla.find_all('tr')
#print(type(jugadores))
#print(len(jugadores))
#print(jugadores)
tope = len(jugadores)

for i in range(1, tope): 
	primerjugador = jugadores[i]
	#print(primerjugador)

	datos =  primerjugador.find_all('td')
	#print(datos)

	numero = datos[0].text
	#print(numero)
	jugador = datos[1].span.text
	#print(jugador)
	fechanac = datos[2].text
	#print(fechanac)
	rol = datos[3].text
	#print(rol)
	nacion = datos[4].find('img')
	nacion = nacion['title']
	#print(nacion)
	partidosjugados = datos[5].text
	#print(partidosjugados)
	goles = datos[6].text
	goles = goles.strip()
	#print(goles)
	amarillas = datos[7].text
	#print(amarillas)
	amarillasrojas = datos[8].text
	#print(amarillasrojas)
	rojas = datos[9].text
	#print(rojas)
	print(numero + "\t" + jugador + "\t" + fechanac + "\t" + rol + "\t" + nacion + "\t" + partidosjugados + "\t" + goles + "\t" + amarillas + "\t" + amarillasrojas + "\t" + rojas + "\n")
