"""

    Sus atributos son titulo, horas estimadas, entregado, genero y compañía.
    Por defecto, las horas estimadas serán de 10 horas y entregado false. El resto de atributos serán valores por defecto según el tipo del atributo.
    Crearemos un constructor  con todos los atributos, excepto de entregado.

    Los métodos que se implementara serán:
        Métodos get de todos los atributos, excepto de entregado.
        Métodos set de todos los atributos, excepto de entregado.


"""
class Videojuego():
    titulo = ""
    horas_estimadas = 10
    entregado = False
    genero = ""
    compania = ""

    def __init__(self, titulo="", horas_estimadas=10, genero="", compania=" "):
        self.titulo = titulo
        self.horas_estimadas = horas_estimadas
        self.genero = genero
        self.compania = compania


    def getTitulo(self,titulo):
        self.titulo = titulo
    def getHoras_estimadas(self,horas_estimadas):
        self.horas_estimadas = horas_estimadas
    def getGenero(self,genero):
        self.genero = genero
    def getCompania(self,compania):
        self.compania = compania

    def setTitulo(self,titulo):
        self.titulo = titulo
    def setHoras_estimadas(self,horas_estimadas):
        self.horas_estimadas = horas_estimadas
    def setGenero(self,genero):
        self.genero = genero
    def setCompania(self,compania):
        self.compania = compania




    def __str__(self):

        return "%s %s %s %s %s" % (self.titulo, self.horas_estimadas, self.entregado, self.genero, self.compania)
