import tkinter as tk
from tkinter import messagebox
import re
from comparacion import ComparacionNumero

class ComparacionApp:
    
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Comparación de números")
        self.root.geometry("350x250")
        self.root.resizable(False, False)
        
        # Frame principal
        self.frame_principal = tk.Frame(master=self.root, padx=20, pady=20)
        self.frame_principal.pack(expand=True)
        
        # Variables para almacenas los valores de entrada
        self.stringvar_numero_a = tk.StringVar()
        self.stringvar_numero_b = tk.StringVar()
        
        # Validación en tiempo real
        self.stringvar_numero_a.trace_add(mode="write", callback=self.validar_numero_a)
        self.stringvar_numero_b.trace_add(mode="write", callback=self.validar_numero_b)
        
        # Creación de los campos
        self.crear_campos_formulario()
        
        # Botón para comparar
        self.button_comparar = tk.Button(
            master=self.frame_principal,
            text="Comparar",
            command=self.comparar_numeros,
            width=15,
            state=tk.DISABLED
        )
        self.button_comparar.pack()
        
        # Estado de validación de los campos
        self.campos_validos = {"numero_a": False, "numero_b": False}
    
    def crear_campos_formulario(self) -> None:
        """Creación de etiquetas y campos de entrada."""
        # Campo del primer número
        tk.Label(master=self.frame_principal, text="Primer número:").pack(anchor=tk.W)
        self.entry_numero_a = tk.Entry(
            master=self.frame_principal,
            textvariable=self.stringvar_numero_a,
            width=30
        )
        self.entry_numero_a.focus()
        self.entry_numero_a.pack()
        self.label_error_numero_a = tk.Label(
            master=self.frame_principal,
            text="",
            fg="red",
            wraplength=300
        )
        self.label_error_numero_a.pack(anchor=tk.W)
        
        # Campo del segundo número
        tk.Label(master=self.frame_principal, text="Segundo número:").pack(anchor=tk.W)
        self.entry_numero_b = tk.Entry(
            master=self.frame_principal,
            textvariable=self.stringvar_numero_b,
            width=30
        )
        self.entry_numero_b.pack()
        self.label_error_numero_b = tk.Label(
            master=self.frame_principal,
            text="",
            fg="red",
            wraplength=300
        )
        self.label_error_numero_b.pack(anchor=tk.W)
        
    def validar_numero_a(self, *args) -> None:
        """Validación del campo del primero número."""
        numero = self.stringvar_numero_a.get()
        if not numero:
            self.label_error_numero_a.config(text="Campo requerido.")
            self.campos_validos["numero_a"] = False
        elif not re.match(pattern=r"^[-]?[0-9]+(\.[0-9]+)?$", string=numero):
            self.label_error_numero_a.config(text="Ingrese un número válido.")
            self.campos_validos["numero_a"] = False
        else:
            self.label_error_numero_a.config(text="")
            self.campos_validos["numero_a"] = True
        self.actualizar_boton_comparar()
    
    def validar_numero_b(self, *args) -> None:
        """Validación del campo del segundo número."""
        numero = self.stringvar_numero_b.get()
        if not numero:
            self.label_error_numero_b.config(text="Campo requerido.")
            self.campos_validos["numero_b"] = False
        elif not re.match(pattern=r"^[-]?[0-9]+(\.[0-9]+)?$", string=numero):
            self.label_error_numero_b.config(text="Ingrese un número válido.")
            self.campos_validos["numero_b"] = False
        else:
            self.label_error_numero_b.config(text="")
            self.campos_validos["numero_b"] = True
        self.actualizar_boton_comparar()
    
    def actualizar_boton_comparar(self):
        """Habilitar o deshabilitar el boton"""
        if all(self.campos_validos.values()):
            self.button_comparar.config(state=tk.NORMAL)
        else:
            self.button_comparar.config(state=tk.DISABLED)
    
    def comparar_numeros(self) -> None:
        """Se realiza la comparación y se muestra en una ventana."""
        numero_a = self.stringvar_numero_a.get()
        numero_b = self.stringvar_numero_b.get()
        
        comparacion = ComparacionNumero(valor_a=float(numero_a), valor_b=float(numero_b))
        
        mensaje = f"""
        {numero_a} es {comparacion.comparar().value} que {numero_b}
        """
        messagebox.showinfo(title="Comparación", message=mensaje)
        self.limpiar_campos()
    
    def limpiar_campos(self) -> None:
        """Limpia los campos, se retorna a sus valores por defecto."""
        self.stringvar_numero_a.set(value="")
        self.stringvar_numero_b.set(value="")
        
        self.label_error_numero_a.config(text="")
        self.label_error_numero_b.config(text="")
        
        self.entry_numero_a.focus()


def main() -> None:
    root = tk.Tk()
    ComparacionApp(root=root)
    root.mainloop()

main()
