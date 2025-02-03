import tkinter as tk
from tkinter import messagebox
from notas.notas import Notas

class VentanaPrincipal(tk.Tk):
    """
    Esta clase denominada VentanaPrincipal define una interfaz gráfica
    que permitirá crear una lista de notas. Luego, se puede calcular el
    promedio de notas, la desviación, la nota mayor y la nota menor de la lista.
    """
    def __init__(self):
        super().__init__()
        self.title("Notas")
        self.geometry("280x340")
        self.resizable(False, False)
        self.notas = Notas()

        # Etiquetas y campos de entrada
        self.labels = [tk.Label(self, text=f"Nota {i+1}:") for i in range(5)]
        self.entries = [tk.Entry(self) for _ in range(5)]
        
        for i in range(5):
            self.labels[i].place(x=20, y=20 + i * 30)
            self.entries[i].place(x=105, y=20 + i * 30, width=135)

        # Botones
        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn_calcular.place(x=40, y=170, width=90)
        
        self.btn_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar)
        self.btn_limpiar.place(x=155, y=170, width=90)

        # Etiquetas de resultados
        self.lbl_promedio = tk.Label(self, text="Promedio = ")
        self.lbl_promedio.place(x=20, y=210)
        
        self.lbl_desviacion = tk.Label(self, text="Desviación = ")
        self.lbl_desviacion.place(x=20, y=240)
        
        self.lbl_mayor = tk.Label(self, text="Nota mayor = ")
        self.lbl_mayor.place(x=20, y=270)
        
        self.lbl_menor = tk.Label(self, text="Nota menor = ")
        self.lbl_menor.place(x=20, y=300)

    def calcular(self):
        """
        Método que se ejecuta al presionar el botón "Calcular".
        Obtiene las notas ingresadas, realiza los cálculos y muestra los resultados.
        """
        try:
            self.notas.lista_notas = [float(entry.get()) for entry in self.entries]
            promedio = self.notas.calcular_promedio()
            desviacion = self.notas.calcular_desviacion()
            mayor = self.notas.calcular_mayor()
            menor = self.notas.calcular_menor()

            self.lbl_promedio.config(text=f"Promedio = {promedio:.2f}")
            self.lbl_desviacion.config(text=f"Desviación = {desviacion:.2f}")
            self.lbl_mayor.config(text=f"Nota mayor = {mayor:.2f}")
            self.lbl_menor.config(text=f"Nota menor = {menor:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese solo números válidos")
    
    def limpiar(self):
        """
        Método que se ejecuta al presionar el botón "Limpiar".
        Limpia los campos de texto y restablece las etiquetas de resultados.
        """
        for entry in self.entries:
            entry.delete(0, tk.END)
        self.entries[0].focus()
        self.notas.lista_notas = []
        self.lbl_promedio.config(text="Promedio = ")
        self.lbl_desviacion.config(text="Desviación = ")
        self.lbl_mayor.config(text="Nota mayor = ")
        self.lbl_menor.config(text="Nota menor = ")
