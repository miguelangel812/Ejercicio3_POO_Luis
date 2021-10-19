"""
    Implementa los anteriores métodos en las clases Videojuego y Serie. Ahora crea una aplicación  y realiza lo siguiente:

    Crea dos listas, uno de Series y otro de Videojuegos, de 5 posiciones cada uno.
    Crea un objeto en cada posición de la lista, con los valores que desees.
    Entrega algunos Videojuegos y Series con el método entregar().
    Cuenta cuantos Series y Videojuegos hay entregados. Al contarlos, devuélvelos.
    Por último, indica el Videojuego tiene más horas estimadas y la serie con mas temporadas.

"""


from Videojuego import Videojuego
from Serie import Serie

lista_videojuegos = ()
lista_videojuegos = list(lista_videojuegos)

lista_series = ()
lista_series = list(lista_series)

lista_series.insert(-1, Serie(titulo="Vikingos", numero_temporadas=5, genero="Aventura", creador="Michael Hirst"))
lista_series.insert(-1, Serie(titulo="Dragon Ball", numero_temporadas=4, genero="Aventura", creador="Akira Toriyama"))
lista_series.insert(-1, Serie(titulo="Juego de Tronos", numero_temporadas=8, genero="Aventura", creador="George R. R. Martin"))
lista_series.insert(-1, Serie(titulo="Peaky Blinders", numero_temporadas=5, genero="Drama Historica", creador="Steven Knight"))
lista_series.insert(-1, Serie(titulo="Sherlock Holmes", numero_temporadas=4, genero="Investigacion", creador=" Arthur Conan Doyle"))

lista_videojuegos.insert(-1,Videojuego(titulo="League of Legends", horas_estimadas=720, genero="MOBA", compania="Riot Games"))
lista_videojuegos.insert(-1,Videojuego(titulo="Fifa", horas_estimadas=888, genero="Simulacion", compania="EA"))
lista_videojuegos.insert(-1,Videojuego(titulo="Counter Strike", horas_estimadas=1000, genero="Shooter", compania="Steam"))
lista_videojuegos.insert(-1,Videojuego(titulo="Valorant", horas_estimadas=508, genero="Shooter", compania="Riot Games"))
lista_videojuegos.insert(-1,Videojuego(titulo="Apex Legends", horas_estimadas=300, genero="Shooter", compania="Origin"))


mayor_temporadas = 0
cont = 0

for ele in lista_series:
    if (ele.numero_temporadas > mayor_temporadas):
        mayor_temporadas = ele.numero_temporadas
        posicion = cont
    cont = cont + 1

print(lista_series[posicion])

mayor = 0
cont = 0

for ele in lista_videojuegos:
    if (ele.horas_estimadas > mayor):
        mayor = ele.horas_estimadas
        posicion = cont
    cont = cont + 1


print(lista_videojuegos[posicion])

def entregar(self, entrega):
    entrega = True
    return entrega