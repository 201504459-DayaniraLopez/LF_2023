

class Peliculas:
    def __init__(self):
        # crearemos una lista que almacenara diccionarios
        self.listadepeliculas = []
        self.listaactores=[]

    def Guardar(self, ruta):
        index = ""  # optendremos la ruta del archivo a analizar
        archivo = open(ruta, "r", encoding="utf-8")
        for line1 in archivo:
            cadena = line1.split(sep=";")
            if len(cadena) != 1:
                datos = {
                    "Nombre": cadena[0],
                    "Actores": cadena[1].strip(),
                    "Año": cadena[2].strip(),
                    "Genero": cadena[3].strip()
                }
                for actor in cadena[1].split(","):
                    if len(self.listaactores) == 0:
                        self.listaactores.append(actor.strip())
                    else:
                        self.listaactores.append(actor.strip())                   

            if len(self.listadepeliculas) == 0:
                self.listadepeliculas.append(datos)
                
            else:
                buscar = self.ValidarP(cadena[0])
                if buscar == 0:
                    self.listadepeliculas.append(datos)
                else:
                    index = self.BuscarP(cadena[0])
                    print(index)
                    self.listadepeliculas.pop(index)
                    print("Se encontraron Peliculas duplicadas en el Archivo de Datos")
                    self.listadepeliculas.append(datos)

    def BuscarP(self, nombre):
        for dato in self.listadepeliculas:
            if dato["Nombre"] == nombre:
                return self.listadepeliculas.index(dato)

    def ValidarP(self, nombre):
        for dato in self.listadepeliculas:
            if dato["Nombre"] == nombre:
                return True

        return False

    def imprimir(self,op):
        n = 0
        x = 0
      
        if op==1:
            print("")
            print("********************************PELICULAS REGISTRADAS*******************************************")
            print("------------------------------------------------------------------------------------------------")
            for i in self.listadepeliculas:
                for key, value in i.items():
                    print(key, "-", value )
                print("------------------------------------------------------------------------------------------------\n")      
            print("------------------------------------------------------------------------------------------------\n")
        elif op==2:
            npelicula=0
            print("\n-----------------------------------------")
            print("*********PELICULAS REGISTRADAS*************")
            print("-------------------------------------------")
           
            for x in self.listadepeliculas:
                n=n+1
                print(str(n)+'.'+ str(x["Nombre"]) )

            print("-----------------------------------------")
            try:
                npelicula= int(input("Eliga la pelicula: "))
                try:
                    peli=self.listadepeliculas[npelicula-1]
                    actores = peli["Actores"].split(",")
                    print("\n----------------------------------------")
                    print("*********PELICULAS Elegida****************")
                    print("------------------------------------------")
                    print(""+str(peli["Nombre"])+"")
                    print("-------------------------------------------")
                    print("***************ACTORES*********************")
                    print("-------------------------------------------\n")
                    for a in actores:
                        print(a)
                    print("-------------------------------------------\n")
                except IndexError:
                    print("La pelicula elegida no existe")
              
            except ValueError:
                    print("El caracter ingresado no es valido")
                    
        
        elif op==3:
            npelicula = 0
            print("\n----------------------------------------")
            print("**********ACTORES REGISTRADOS**************")
            print("------------------------------------------")
            self.Eliminar(self.listaactores)
            try:
                nactor = int(input("Eliga el Actor que desea: "))
                try:
                    actor = self.listaactores[nactor-1]
                    print("\nActor Elegido: " +actor)
                    print("\n----------------------------------------")
                    print("****PELICULAS EN LAS QUE HAN ACTUADO******")
                    print("------------------------------------------")
                    for pelitem in self.listadepeliculas:
                        temp = pelitem["Actores"].split(",")
                        for p in temp:
                            if p.strip() == actor:
                                print(pelitem["Nombre"])
                    print("------------------------------------------\n")
                except IndexError:
                    print("El actor elegida no existe")

            except ValueError:
                    print("El caracter ingresado no es valido")
        elif op==4:
            listaaño = []
            print("\n----------------------------------------")
            print("*************AÑOS REGISTRADOS*************")
            print("------------------------------------------")
            
            for year in self.listadepeliculas:
                listaaño.append(year["Año"].strip())
            self.Eliminar(listaaño)
            try:
                nyear = int(input("Eliga el año que desea: "))
                if listaaño.count(str(nyear))>0:
                        print("\nAño Elegido: " + str(nyear))
                        print("\n--------------------------------------------")
                        print("****************PELICULAS*********************")
                        print("----------------------------------------------")
                        for movie in self.listadepeliculas:
                            if nyear== int(movie["Año"]):
                                    print("Nombre: "+movie["Nombre"])
                                    print("Género: "+movie["Genero"])
                                    print("----------------------------------------------")
                else:
                    print("El año ingresado no esta registrado.")
            except ValueError:
                print("El caracter ingresado no es valido")
           
        elif op == 5:
            listagenero = []
            print("\n----------------------------------------")
            print("***********GENERO REGISTRADOS*************")
            print("------------------------------------------")
            for genero in self.listadepeliculas:
                listagenero.append(genero["Genero"])
            
            self.Eliminar(listagenero)
            
            ngenero = input("Escriba el Genero que desea: ")
            if listagenero.count(ngenero) > 0:
                print("\nGenero elegido: " + ngenero)
                print("\n------------------------------------------")
                print("****************PELICULAS*******************")
                print("--------------------------------------------")
                for movie in self.listadepeliculas:
                    if ngenero.strip() == movie["Genero"]:
                            print("*"+movie["Nombre"])
            else:
                print("El genero seleccionado no esta en la lista")
                
    def Eliminar(self, lista):
        x=0
        for p in lista:
            if lista.count(p)==1:
                next
            elif lista.count(p)>1:
                 while lista.count(p)>1:
                     lista.pop(lista.index(p))


        for a in lista:
            x = x + 1
            print(str(x)+'. ' + a+"")
        print("")


