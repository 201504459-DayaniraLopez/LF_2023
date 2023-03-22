import tkinter as tk
from tkinter import *
from functools import partial
from tkinter import Menu, filedialog, messagebox as MessageBox
fuente = 'Lucida Sans Typewriter'


class Ventana():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("PROYECTO 1")
        self.window.geometry("400x350")
        self.window['bg'] = '#E9E9D3'

        menu_bar = tk.Menu(self.window)
        self.doc=tk.StringVar()
       # Crear el primer menú desplegable
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Abrir", command=self.abrir)
        file_menu.add_command(label="Guardar",command=self.guardar)
        file_menu.add_command(label="Guardar Como")
        file_menu.add_command(label="Analizar")
        file_menu.add_command(label="Error")
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.window.quit)

        menu_bar.add_cascade(label="Archivo", menu=file_menu)

        ayuda_menu = tk.Menu(menu_bar, tearoff=0)

        ayuda_menu.add_command(label="Manual de Usuario")
        ayuda_menu.add_command(label="Manual Técnico")
        ayuda_menu.add_command(label="Temas de Ayuda")

        # Agregar el segundo menú desplegable a la barra de menú
        menu_bar.add_cascade(label="Ayuda", menu=ayuda_menu)
        self.window.config(menu=menu_bar)

        self.text_area = tk.Text(self.window, height=21, width=48)
        self.text_area.place(x=10, y=350)
        
        self.text_area.pack()
        self.window.mainloop()

    def abrir(self):
        cadena=""
        self.ruta = filedialog.askopenfilename(initialdir="C:/Users/Dayanira (Trabajo)/Documents/LF 2023/Proyecto 1", title="Selecione Archivo", filetypes=(
            ("data files", "*.json"), ("todos los archivos", "*.*")))
        self.archivo = open(self.ruta,"r")
        for linea1 in self.archivo:
             cadena = cadena + linea1


        self.text_area.insert(tk.END, cadena)


    def guardar(self):
        print(self.text_area.get())   

def main():
    Ventana()
    return 0


if __name__ == '__main__':
    main()
