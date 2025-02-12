import tkinter as tk
from tkinter import messagebox
from figuras.cilindro import Cilindro

class VentanaCilindro(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cilindro")
        self.geometry("280x210")
        self.resizable(False, False)
        self.center_window()
        self.init_ui()
        
    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"280x210+{x}+{y}")
    
    def init_ui(self):
        # Etiquetas y campos de entrada
        tk.Label(self, text="Radio (cm):").place(x=20, y=20)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=100, y=20, width=135, height=23)
        
        tk.Label(self, text="Altura (cm):").place(x=20, y=50)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=100, y=50, width=135, height=23)
        
        # Botón Calcular
        self.boton_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.boton_calcular.place(x=100, y=80, width=135, height=23)
        
        # Etiquetas de resultados
        self.label_volumen = tk.Label(self, text="Volumen (cm3):")
        self.label_volumen.place(x=20, y=110)
        
        self.label_superficie = tk.Label(self, text="Superficie (cm2):")
        self.label_superficie.place(x=20, y=140)
    
    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            altura = float(self.campo_altura.get())
            cilindro = Cilindro(radio, altura)
            
            volumen = cilindro.calcular_volumen()
            superficie = cilindro.calcular_superficie()
            
            self.label_volumen.config(text=f"Volumen (cm3): {volumen:.2f}")
            self.label_superficie.config(text=f"Superficie (cm2): {superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")
