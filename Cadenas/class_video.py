from datetime import datetime

class Video:
    def __init__(self, titulo: str, vistas: int, tiempo: int, url_youtube: str, fecha_lanzamiento: str):
        self.titulo = titulo
        self.vistas = vistas
        self.tiempo = tiempo
        self.url_youtube = url_youtube
        self.fecha_lanzamiento = fecha_lanzamiento
        self.sesion = None
        self.colaborador = None
        self.codigo_url = None
        
    def mostrar_tema(self):
        #Agregar los datos pertinentes para que a la hora de mostrar se vean los datos completos del video
        print(f"Titulo: {self.titulo}")
        print(f"Vistas: {self.vistas}")
        print(f"Duración: {self.tiempo} segundos")
        print(f"URL de YouTube: {self.url_youtube}")
        print(f"Fecha de Lanzamiento: {self.fecha_lanzamiento.strftime("%d-%m-%Y")}")
        print("*"*30)


    def dividir_titulo(self):
        #Debe setear el atributo sesion y colaborador con los datos obtenidos del titulo del video
        lista_titulo = self.titulo.split("|")

        self.colaborador = lista_titulo[0].strip()

        self.sesion = lista_titulo[1].replace("Sesión #", "").strip()

    
    def obtener_codigo_url(self):
        #Debe setear el atributo codigo_url con el codigo obtenido del atributo url_youtube
        #Por ej: si la url es https://www.youtube.com/watch?v=nicki13 el codigo seria nicki13
        self.codigo_url = self.url_youtube.replace("https://www.youtube.com/watch?v=", "")
    
    def formatear_fecha(self):
        #Necesitamos que la fecha de lanzamiento sea un objeto de la clase datetime (investigar).
        #Para ello deberan dividir la fecha (en formato string) en dia, mes y año y a partir de esos datos, crear la nueva fecha. 
        fecha_string = self.fecha_lanzamiento.split('-')

        anio = int(fecha_string[0])
        mes = int(fecha_string[1])
        dia = int(fecha_string[2])

        fecha = datetime(anio, mes, dia)

        self.fecha_lanzamiento = fecha


def ordenar_lista(lista: list[Video]):
    for i in range(len(lista)):
        for j in range(len(lista) -1 -i):
            if lista[j].sesion() > lista[j + 1].sesion():
                auxiliar = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = auxiliar

def calcular_promedio_vistas(lista: list[Video]) -> float:
    acumulador_vistas = 0

    for i in range(len(lista)):
        for j in range(len(lista)):
            vistas = lista[j].vistas

            acumulador_vistas += vistas
    
    promedio = acumulador_vistas / len(lista)

    
    return promedio


def calcular_maxima_reproducción(lista: list[Video]) -> int:
    maximo = None

    for i in range(len(lista)):
        for j in range(len(lista)):
            vistas = lista[j].vistas

            if maximo == None or vistas > maximo:
                maximo = vistas

                titulo = lista[j].titulo

    return f'{titulo}, con {maximo} vistas'

def busqueda_por_codigo(lista: list[Video]):
    for i in range(len(lista)):
        buscar = lista[i].url_youtube
        buscar = buscar.count('nick')

        if buscar >= 1:
            lista[i].mostrar_tema()

def listar_por_colaborador(lista: list[Video]):
    colaborador = input('Ingrese el nombre del colaborador a buscar (sin usar espacios): ')
    colaborador = colaborador.upper()
    
    for i in range(len(lista)):
        buscar = lista[i].titulo
        buscar = buscar.count(colaborador)

        if buscar >= 1:
            lista[i].mostrar_tema()