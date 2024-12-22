import tkinter as tk
from tkinter import messagebox
import re
from equilatero import Equilatero

class EquilateroApp:
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Triángulo Equilátero")
        self.root.geometry("350x200")
        self.root.resizable(False, False)
        
        # Frame principal
        self.frame_principal = tk.Frame(master=self.root, padx=20, pady=20)
        self.frame_principal.pack(expand=True)
        
        # Variable para almacenar el valor de entrada
        self.stringvar_lado = tk.StringVar()
        
        # Validación en tiempo real
        self.stringvar_lado.trace_add(mode="write", callback=self.validar_lado)
        
        # Creación de los widgets
        self.creacion_widgets()
        
        # Botón para calcular
        self.button_calcular = tk.Button(
            master=self.frame_principal,
            text="Calcular",
            command=self.mostrar_resultados,
            width=20,
            state=tk.DISABLED
        )
        self.button_calcular.pack(pady=10)
        
        # Estado validación del campo
        self.campos_validos = {"lado": False}
    
    def creacion_widgets(self) -> None:
        """Campos del formulario con sus etiquetas."""
        # Campo lado de un triángulo equilátero
        tk.Label(master=self.frame_principal, text="Lado (en cm):").pack(anchor=tk.W)
        self.entry_lado = tk.Entry(
            master=self.frame_principal,
            textvariable=self.stringvar_lado,
            width=30
        )
        self.entry_lado.focus()
        self.entry_lado.pack()
        self.label_error_lado = tk.Label(
            master=self.frame_principal,
            text="",
            fg="red",
            wraplength=300
        )
        self.label_error_lado.pack(anchor=tk.W)
    
    def validar_lado(self, *args) -> None:
        """Valida que el campo lado del triángulo contenga solo números."""
        lado = self.stringvar_lado.get()
        if not lado:
            self.label_error_lado.config(text="Campo requerido.")
            self.campos_validos["lado"] = False
        elif not re.match(pattern=r"^[0-9]+(\.[0-9]+)?$", string=lado):
            self.label_error_lado.config(text="Ingrese solo números positivos.")
            self.campos_validos["lado"] = False
        else:
            self.label_error_lado.config(text="")
            self.campos_validos["lado"] = True
        self.actualizar_boton_calcular()
    
    def actualizar_boton_calcular(self) -> None:
        """Actualiza el estado del botón de acuerdo a la validación de los campos."""
        if all(self.campos_validos.values()):
            self.button_calcular.config(state=tk.NORMAL)
        else:
            self.button_calcular.config(state=tk.DISABLED)
    
    def calcular_propiedades(self) -> dict[str, float]:
        """Extraer la información del campo lado para calcular las propiedades."""
        lado = float(self.stringvar_lado.get())
        
        equilatero = Equilatero(lado=lado)
        
        perimetro = equilatero.perimetro_equilatero()
        altura = equilatero.altura_equilatero()
        area = equilatero.area_equilatero()
        
        return {
            "perimetro": perimetro,
            "altura": altura,
            "area": area
        }
    
    def mostrar_resultados(self) -> None:
        """Obtiene los datos para mostrar los resultados."""
        propiedades = self.calcular_propiedades()
        mensaje = f"""
        Propiedades Triángulo Equilátero:
        
        Perímetro (cm):\t{propiedades["perimetro"]:.2f}
        Altura (cm):\t\t{propiedades["altura"]:.2f}
        Área (cm²):\t\t{propiedades["area"]:.2f}
        """
        messagebox.showinfo(title="Resultados", message=mensaje)
        self.limpiar_campos()
    
    def limpiar_campos(self) -> None:
        """Valores por defecto del framde"""
        self.stringvar_lado.set(value="")
        self.label_error_lado.config(text="")
        self.entry_lado.focus()
    

def main() -> None:
    root = tk.Tk()
    EquilateroApp(root=root)
    root.mainloop()

main()
