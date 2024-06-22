class Estudiante():
    def __init__(self , nombre , nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print (f"Nombre:{self.nombre} Nota: {self.nota}")

    def resultados(self):
        if self.nota >= 7:
            print("Haz APROBADO!")
        else:
            print("Haz Reprobado!")

estudiante1=Estudiante("Pedro" , 8)
estudiante1.imprimir()
estudiante1.resultados()