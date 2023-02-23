from tkinter import  filedialog

import re
import Funcionamiento
Datos = Funcionamiento.Peliculas()

def menu():
    Instruciones=None
    opcion = 0
    condicion = True
    while (condicion == True):
        print("┌-----MENU DE INICIO------┐")
        print("|1.Cargar Archivo         |")
        print("|2.Gestion Peliculas      |")
        print("|3.Filgrado               |")
        print("|4.Grafica                |")
        print("|5.Salir                  |")
        print("└-------------------------┘")
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion < 6 and opcion > 0 :
                if opcion == 1:
                    CargarData()
                elif opcion == 2:
                    Peliculas()
                elif opcion== 3:
                    Filtrado()
                elif opcion == 4:
                    print("Grafica")
                elif opcion== 5:
                    exit()
            else:
                print("La opcion ingresada no existe")

        except  ValueError:
            print("El caracter ingresado no es valido")

def CargarData():
    print("CARGA DE DATOS")
    ruta = filedialog.askopenfilename(initialdir="C:", title="Selecione Archivo", filetypes=(
        ("data files", "*.lfp"), ("todos los archivos", "*.*")))
    Datos.Guardar(ruta)
    
def Peliculas():
   condicion = True
   op_peliculas = 0
   while (condicion == True):
       print("┌-----MENU DE PELICULAS------┐")
       print("|1.Mostrar Peliculas         |")
       print("|2.Mostrar Actores           |")
       print("|3.Regresar a Menu           |")
       print("└----------------------------┘")
       try: 
            op_peliculas = int(input("Ingrese una opcion: "))
            if op_peliculas < 4 and op_peliculas > 0:
                if op_peliculas == 1:
                    Datos.imprimir(op_peliculas)
                elif op_peliculas == 2:
                    Datos.imprimir(op_peliculas)
                elif op_peliculas == 3:
                    menu()
            else:
                print("Numero ingresado fuera de rango")
       except ValueError:
          print("El caracter ingresado no es valido")

def Filtrado():
   condicion2 = True
   op_filtro = 0
   while (condicion2 == True):
       print("┌-----MENU DE FILTRO---------┐")
       print("|1.Filtrado de Actor         |")
       print("|2.Filtrado de Año           |")
       print("|3.Filtrado por Genéro       |")
       print("|4.Regresar a Menu           |")
       print("└----------------------------┘")
       try: 
            op_filtro = int(input("Ingrese una opcion: "))
            if op_filtro < 5 and op_filtro > 0:
                if op_filtro == 1:
                    print("Filtrado Actor")
                elif op_filtro == 2:
                    print("Filtrado de Año")
                elif op_filtro == 3:
                    print("Filtrado por Género")
                elif op_filtro == 4:
                    menu()
            else:
                print("Numero ingresado fuera de rango")
       except ValueError:
          print("El caracter ingresado no es valido")

    
def main():
    Menu = menu()
    return


if __name__== '__main__':
        main()
