import tkinter as tk
from equilatero import Equilatero

class EquilateroApp:
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Triángulo Equilátero")
        self.root.geometry("400x380")
        self.root.resizable(False, False)
        
        # Frame principal
        self.frame_principal = tk.Frame(master=self.root)
        self.frame_principal.pack(expand=True)
        
        # Título frame
        self.label_titulo = tk.Label(
            master=self.frame_principal,
            text="Triángulo Equilátero",
            font=("Arial", 18, "bold"),
            fg="blue"
        )
        self.label_titulo.grid(column=0, row=0, columnspan=2, pady=10)
        
        # Nombre de etiquetas
        self.label_lado = tk.Label(
            master=self.frame_principal,
            text="Lado (cm):",
            font=("Arial", 14)
        )
        self.label_lado.grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
        self.label_perimetro = tk.Label(
            master=self.frame_principal,
            text="Perímetro (cm):",
            font=("Arial", 14)
        )
        self.label_perimetro.grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)
        self.label_altura = tk.Label(
            master=self.frame_principal,
            text="Altura (cm):",
            font=("Arial", 14)
        )
        self.label_altura.grid(column=0, row=3, padx=10, pady=10, sticky=tk.W)
        self.label_area = tk.Label(
            master=self.frame_principal,
            text="Área (cm²):",
            font=("Arial", 14)
        )
        self.label_area.grid(column=0, row=4, padx=10, pady=10, sticky=tk.W)

        # Campo de entrada
        self.entry_lado = tk.Entry(
            master=self.frame_principal,
            font=("Arial", 14),
            width=5
        )
        self.entry_lado.grid(column=1, row=1, padx=10, pady=10, sticky=tk.E)
        
        # Etiquetas de salida
        self.label_perimetro_resultado = tk.Label(
            master=self.frame_principal,
            text="0.00",
            font=("Arial", 14, "bold")
        )
        self.label_perimetro_resultado.grid(column=1, row=2, padx=10, pady=10, sticky=tk.E)
        self.label_altura_resultado = tk.Label(
            master=self.frame_principal,
            text="0:00",
            font=("Arial", 14, "bold")
        )
        self.label_altura_resultado.grid(column=1, row=3, padx=10, pady=10, sticky=tk.E)
        self.label_area_resultado = tk.Label(
            master=self.frame_principal,
            text="0:00",
            font=("Arial", 14, "bold")
        )
        self.label_area_resultado.grid(column=1, row=4, padx=10, pady=10, sticky=tk.E)
        
        # Botones
        self.button_calcular = tk.Button(
            master=self.frame_principal,
            text="Calcular",
            font=("Arial", 14),
            command=self.calcular_propiedades
        )
        self.button_calcular.grid(column=0, row=5, padx=10, pady=10, sticky=tk.W)
        self.button_limpiar = tk.Button(
            master=self.frame_principal,
            text="Limpiar",
            font=("Arial", 14),
            command=self.limpiar_campos
        )
        self.button_limpiar.grid(column=1, row=5, padx=10, pady=10, sticky=tk.E)
        
        # Etiqueta de advertencias
        self.label_advertencia = tk.Label(
            master=self.frame_principal,
            text="Ingrese solo números positivos.",
            font=("Arial", 12, "bold")
        )
        self.label_advertencia.grid(column=0, row=6, columnspan=2, pady=10)
    
    def calcular_propiedades(self):
        lado = self.entry_lado.get().strip()
        
        if lado == "":
            self.label_advertencia.config(text="El campo no puede estar vacío.", fg="red")
        elif not lado.replace(".", "").isdigit() or lado.count(".") > 1:
            self.label_advertencia.config(text="Ingrese un número válido.", fg="red")
        else:
            equilatero = Equilatero(float(lado))
            perimetro = equilatero.perimetro_equilatero()
            altura = equilatero.altura_equilatero()
            area = equilatero.area_equilatero()
            self.label_perimetro_resultado.config(text=f"{perimetro:.2f}")
            self.label_altura_resultado.config(text=f"{altura:.2f}")
            self.label_area_resultado.config(text=f"{area:.2f}")
            self.label_advertencia.config(text="Cálculos realizados con éxito.", fg="green")
    
    def limpiar_campos(self):
        self.entry_lado.delete(first=0, last=tk.END)
        self.label_perimetro_resultado.config(text="0.00")
        self.label_altura_resultado.config(text="0.00")
        self.label_area_resultado.config(text="0.00")
        self.label_advertencia.config(text="Ingrese solo números positivos.", fg="black")


root = tk.Tk()
EquilateroApp(root=root)
root.mainloop()
