import tkinter as tk
from tkinter import Toplevel
from figuras.ventana_cilindro import VentanaCilindro
from figuras.ventana_esfera import VentanaEsfera
from figuras.ventana_piramide import VentanaPiramide

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.geometry("350x160")
        self.resizable(False, False)
        self.center_window()
        self.inicio()
    
    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"350x160+{x}+{y}")
    
    def inicio(self):
        # Botones para seleccionar una figura geométrica
        self.cilindro_btn = tk.Button(self, text="Cilindro", command=self.mostrar_cilindro)
        self.cilindro_btn.place(x=20, y=50, width=80, height=30)

        self.esfera_btn = tk.Button(self, text="Esfera", command=self.mostrar_esfera)
        self.esfera_btn.place(x=125, y=50, width=80, height=30)

        self.piramide_btn = tk.Button(self, text="Pirámide", command=self.mostrar_piramide)
        self.piramide_btn.place(x=225, y=50, width=100, height=30)
    
    def mostrar_esfera(self):
        VentanaEsfera(self)
    
    def mostrar_cilindro(self):
        VentanaCilindro(self)
    
    def mostrar_piramide(self):
        VentanaPiramide(self)
