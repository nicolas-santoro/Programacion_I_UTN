class Boligrafo:
    capacidad_tinta_maxima = 100
    cantidad_tinta = 80

    def __init__(self, grosor_punta: str, color: str):
        self.grosor_punta = grosor_punta
        self.color = color
    

    def escribir(self, texto: str) -> str:
        caracteres = len(texto)
    

        if self.cantidad_tinta >= caracteres:
            self.cantidad_tinta -= caracteres

            print(f"{texto} \n")

            print(f"Usted gasto {caracteres} de tinta y le queda {self.cantidad_tinta} \n")

        else:
            falta = caracteres - self.cantidad_tinta

            print(f"Tinta insuficiente, le queda {self.cantidad_tinta} de tinta, a usted le falta {falta} tinta \n")

    def recargar(self, tinta: int) -> str:
        self.cantidad_tinta += tinta

        if self.cantidad_tinta > 100:
            sobra = self.cantidad_tinta - 100

            self.cantidad_tinta = 100

            print(f"Se recargó la lapicera y sobró {sobra} cantidad de tinta \n")

        else:
            print(f"Lapicera recargada, tiene en total {self.cantidad_tinta} \n")