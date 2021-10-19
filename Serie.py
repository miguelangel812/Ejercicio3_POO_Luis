"""
Sus atributos son titulo, numero de temporadas, entregado, genero y creador.
    Por defecto, el numero de temporadas es de 3 temporadas y entregado false. El resto de atributos serán valores por defecto según el tipo del atributo.
    Crearemos un constructor con todos los atributos, excepto de entregado.

    Los métodos que se implementara serán:
        Métodos get de todos los atributos, excepto de entregado.
        Métodos set de todos los atributos, excepto de entregado.
        Sobreescribe los métodos toString.

"""

class Serie():
    titulo = ""
    numero_temporadas = 3
    entregado = False
    genero = ""
    creador = ""

    def __init__(self, titulo="", numero_temporadas=3, genero="", creador=" "):
        self.titulo = titulo
        self.numero_temporadas = numero_temporadas
        self.genero = genero
        self.creador = creador


    def getTitulo(self,titulo):
        self.titulo = titulo
    def getNumero_temporadas(self,numero_temporadas):
        self.numero_temporadas = numero_temporadas
    def getGenero(self,genero):
        self.genero = genero
    def getCreador(self,creador):
        self.creador = creador

    def setTitulo(self,titulo):
        self.titulo = titulo
    def setNumero_temporadas(self,numero_temporadas):
        self.numero_temporadas = numero_temporadas
    def setGenero(self,genero):
        self.genero = genero
    def setCreador(self,creador):
        self.creador = creador




    def __str__(self):
        #self.titulo , "  Temporadas --> " , self.numero_temporadas ," la entrega esta: " , self.entregado , " Genero: ", self.genero , " El director es: " , self.creador
        return "%s %s %s %s %s" % (self.titulo, self.numero_temporadas, self.entregado, self.genero, self.creador)
