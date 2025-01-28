import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar
from personas.lista_personas import ListaPersonas
from personas.persona import Persona

class VentanaPrincipal(tk.Tk):
    """
    Esta clase denominada VentanaPrincipal define una interfaz gráfica
    que permitirá crear una persona y agregarla a una lista de personas.
    Luego, se puede eliminar una persona seleccionada o borrar todas las personas.
    """
    def __init__(self):
        """
        Constructor de la clase VentanaPrincipal.
        """
        super().__init__()
        self.lista = ListaPersonas()
        self.title("Personas")
        self.geometry("270x350")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        """
        Método que crea la ventana con sus diferentes componentes gráficos.
        """
        # Etiquetas
        tk.Label(self, text="Nombre:").place(x=20, y=20)
        tk.Label(self, text="Apellidos:").place(x=20, y=50)
        tk.Label(self, text="Teléfono:").place(x=20, y=80)
        tk.Label(self, text="Dirección:").place(x=20, y=110)

        # Campos de texto
        self.campo_nombre = tk.Entry(self)
        self.campo_nombre.place(x=105, y=20, width=135)
        self.campo_apellidos = tk.Entry(self)
        self.campo_apellidos.place(x=105, y=50, width=135)
        self.campo_telefono = tk.Entry(self)
        self.campo_telefono.place(x=105, y=80, width=135)
        self.campo_direccion = tk.Entry(self)
        self.campo_direccion.place(x=105, y=110, width=135)

        # Botones
        self.boton_añadir = tk.Button(self, text="Añadir", command=self.añadir_persona)
        self.boton_añadir.place(x=105, y=150, width=80)
        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_persona)
        self.boton_eliminar.place(x=20, y=280, width=80)
        self.boton_borrar_lista = tk.Button(self, text="Borrar Lista", command=self.borrar_lista)
        self.boton_borrar_lista.place(x=120, y=280, width=120)

        # Lista de personas
        self.lista_nombres = Listbox(self, selectmode=tk.SINGLE)
        self.scroll_lista = Scrollbar(self, orient=tk.VERTICAL, command=self.lista_nombres.yview)
        self.lista_nombres.configure(yscrollcommand=self.scroll_lista.set)
        self.lista_nombres.place(x=20, y=190, width=220, height=80)
        self.scroll_lista.place(x=240, y=190, height=80)

    def añadir_persona(self):
        """
        Método que agrega una persona a lista de personas y a la lista
        gráfica de personas.
        """
        nombre = self.campo_nombre.get()
        apellidos = self.campo_apellidos.get()
        telefono = self.campo_telefono.get()
        direccion = self.campo_direccion.get()

        if nombre and apellidos and telefono and direccion:
            persona = Persona(nombre, apellidos, telefono, direccion)
            self.lista.añadir_persona(persona)
            self.lista_nombres.insert(tk.END, f"{nombre} - {apellidos} - {telefono} - {direccion}")
            self.campo_nombre.delete(0, tk.END)
            self.campo_apellidos.delete(0, tk.END)
            self.campo_telefono.delete(0, tk.END)
            self.campo_direccion.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Todos los campos deben estar completos")

    def eliminar_persona(self):
        """
        Método que elimina una persona del vector de personas y de la
        lista gráfica de personas en la ventana.
        """
        seleccionado = self.lista_nombres.curselection()
        if seleccionado:
            indice = seleccionado[0]
            self.lista.eliminar_persona(indice)
            self.lista_nombres.delete(indice)
        else:
            messagebox.showerror("Error", "Debe seleccionar un elemento")

    def borrar_lista(self):
        """
        Método que elimina todas las personas de la lista de personas.
        """
        self.lista.borrar_lista()
        self.lista_nombres.delete(0, tk.END)
