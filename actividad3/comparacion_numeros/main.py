import tkinter as tk
from comparacion import ComparacionNumero

class ComparacionApp:
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Comparación de números")
        self.root.geometry("450x320")
        self.root.resizable(False, False)
        
        # Frame principal
        self.frame_principal = tk.Frame(master=self.root)
        self.frame_principal.pack(expand=True, pady=20)
        
        # Título
        self.label_titulo = tk.Label(
            master=self.frame_principal,
            text="Comparación de Enteros",
            font=("Arial", 18, "bold")
        )
        self.label_titulo.grid(column=0, row=0, columnspan=2, pady=10)
        
        # Etiquetas
        self.label_numero_a = tk.Label(
            master=self.frame_principal,
            text="Número a:",
            font=("Arial", 14)
        )
        self.label_numero_a.grid(column=0, row=1, pady=10)
        self.label_numero_b = tk.Label(
            master=self.frame_principal,
            text="Número b:",
            font=("Arial", 14)
        )
        self.label_numero_b.grid(column=0, row=2, pady=10)
        
        # Campos de entrada
        self.entry_numero_a = tk.Entry(
            master=self.frame_principal,
            font=("Arial", 14),
            width=10,
        )
        self.entry_numero_a.grid(column=1, row=1, pady=10)
        self.entry_numero_b = tk.Entry(
            master=self.frame_principal,
            font=("Arial", 14),
            width=10,
        )
        self.entry_numero_b.grid(column=1, row=2, pady=10)
        
        # Botones
        self.button_aceptar = tk.Button(
            master=self.frame_principal,
            font=("Arial", 14),
            text="Aceptar",
            command=self.mostrar_informacion
        )
        self.button_aceptar.grid(column=0, row=3, pady=10)
        self.button_limpiar = tk.Button(
            master=self.frame_principal,
            font=("Arial", 14),
            text="Limpiar",
            command=self.limpiar_campos
        )
        self.button_limpiar.grid(column=1, row=3, pady=10)
        
        # Mensaje para mostrar el resultado o advertencias
        self.label_respuesta = tk.Label(
            master=self.frame_principal,
            text="",
            font=("Arial", 15, "bold")
        )
        self.label_respuesta.grid(column=0, row=4, columnspan=2, pady=10)
    
    def mostrar_informacion(self):
        num_a = self.entry_numero_a.get().strip()
        num_b = self.entry_numero_b.get().strip()
        
        if not num_a or not num_b:
            self.label_respuesta.config(
                text="Los campos no pueden\nestar vacíos.",
                fg="red"
            )
        elif not num_a.replace("-", "").isdigit() or not num_b.replace("-", "").isdigit():
            self.label_respuesta.config(
                text="Por favor, ingrese\nnúmeros enteros.",
                fg="red"
            )
        else:
            comparacion = ComparacionNumero(valor_a=num_a, valor_b=num_b)
            
            self.label_respuesta.config(
                text=f"{num_a} es {comparacion.comparar().value} que {num_b}",
                fg="blue"
            )
    
    def limpiar_campos(self):
        self.entry_numero_a.delete(first=0,last=tk.END)
        self.entry_numero_b.delete(first=0, last=tk.END)
        self.label_respuesta.config(text="")
        self.entry_numero_a.focus()
        

root = tk.Tk()
ComparacionApp(root=root)
root.mainloop()
