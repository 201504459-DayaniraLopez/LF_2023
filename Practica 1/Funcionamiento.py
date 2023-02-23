

class Peliculas:
    def __init__(self):
        # crearemos una lista que almacenara diccionarios
        self.listadepeliculas = []

    def Guardar(self, ruta):
        index = ""  # optendremos la ruta del archivo a analizar
        archivo = open(ruta, "r", encoding="utf-8")
        for line1 in archivo:
            cadena = line1.split(sep=";")
            if len(cadena) != 1:
                datos = {
                    "Nombre": cadena[0],
                    "Actores": cadena[1],
                    "Año": cadena[2],
                    "Genero": cadena[3]
                }
            if len(self.listadepeliculas) == 0:
                self.listadepeliculas.append(datos)
            else:
                buscar = self.Validar(cadena[0])
                if buscar == 0:
                    self.listadepeliculas.append(datos)
                else:
                    index = self.Buscar(cadena[0])
                    print(index)
                    self.listadepeliculas.pop(index)
                    print("Se encontraron Peliculas duplicadas en el Archivo de Datos")
                    self.listadepeliculas.append(datos)

       

    def Buscar(self, nombre):
        for dato in self.listadepeliculas:
            if dato["Nombre"] == nombre:
                return self.listadepeliculas.index(dato)

    def Validar(self, nombre):
        for dato in self.listadepeliculas:
            if dato["Nombre"] == nombre:
                return True

        return False

    def imprimir(self,op):
        n = 0
        if op==1:
            print("")
            print("********************************PELICULAS REGISTRADAS*******************************************")
            print("------------------------------------------------------------------------------------------------")
            for i in self.listadepeliculas:
                for key, value in i.items():
                    print(key, "-", value )
            print("------------------------------------------------------------------------------------------------\n")
        elif op==2:
            npelicula=0
            print("\n-----------------------------------------")
            print("*********PELICULAS REGISTRADAS***********")
            print("-----------------------------------------")
           
            for x in self.listadepeliculas:
                n=n+1
                print(str(n)+'.'+ str(x["Nombre"]) )

            print("-----------------------------------------")
            npelicula= int(input("Eliga la pelicula: "))
            peli=self.listadepeliculas[npelicula-1]
            actores = peli["Actores"].split(",")
            
            print("\n----------------------------------------")
            print("*********PELICULAS Elegida****************")
            print("------------------------------------------")
            print(""+str(peli["Nombre"])+"")
            print("-------------------------------------------")
            print("\n********ACTORES************")
            for a in actores:
                print(a)
            
            print("-------------------------------------------\n")

