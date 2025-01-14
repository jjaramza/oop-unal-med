import tkinter as tk
from tkinter import messagebox
import re
from ecuacion import EcuacionGrado2

class EcuacionApp:
    
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Ecuación de Grado 2")
        self.root.geometry("300x350")
        self.root.resizable(False, False)
        
        # Frame principal
        self.frame_principal = tk.Frame(master=self.root, padx=20, pady=20)
        self.frame_principal.pack(expand=True)
        
        # Variables para almacenar los valores de entrada
        self.stringvar_coef_cuadratico = tk.StringVar()
        self.stringvar_coef_lineal = tk.StringVar()
        self.stringvar_independiente = tk.StringVar()
        
        # Validaciones en tiempo real
        self.stringvar_coef_cuadratico.trace_add(
            mode="write",
            callback=self.validar_coef_cuadratico
        )
        self.stringvar_coef_lineal.trace_add(
            mode="write",
            callback=self.validar_coef_lineal
        )
        self.stringvar_independiente.trace_add(
            mode="write",
            callback=self.validar_independiente
        )
        
        # Método para crear campos del formulario
        self.crear_campos_formulario()
        
        # Botón para enviar
        self.button_calcular = tk.Button(
            master=self.frame_principal,
            text="Calcular",
            command=self.enviar_formulario,
            height=2,
            width=20,
            state=tk.DISABLED
        )
        self.button_calcular.pack(pady=10)
        
        # Estado de validación de los campos
        self.campos_validos = {
            "cuadratico": False,
            "lineal": False,
            "independiente": False
        }
    
    def crear_campos_formulario(self) -> None:
        """Campos del formulario con sus etiquetas."""
        # Campo Coeficiente Cuadrático
        tk.Label(master=self.frame_principal, text="Coeficiente cuadrático:").pack(anchor=tk.W)
        self.entry_cuadratico = tk.Entry(
            master=self.frame_principal,
            textvariable=self.stringvar_coef_cuadratico,
            width=30
        )
        self.entry_cuadratico.focus()
        self.entry_cuadratico.pack()
        self.label_error_cuadratico = tk.Label(
            master=self.frame_principal,
            text="",
            fg="red",
            wraplength=300
        )
        self.label_error_cuadratico.pack(anchor=tk.W)
        
        # Campo Coeficiente lineal
        tk.Label(master=self.frame_principal, text="Coeficiente lineal:").pack(anchor=tk.W)
        self.entry_lineal = tk.Entry(
            master=self.frame_principal,
            textvariable=self.stringvar_coef_lineal,
            width=30
        )
        self.entry_lineal.pack()
        self.label_error_lineal = tk.Label(
            master=self.frame_principal,
            text="",
            fg="red",
            wraplength=300
        )
        self.label_error_lineal.pack(anchor=tk.W)
        
        # Campo Término independiente
        tk.Label(master=self.frame_principal, text="Término independiente:").pack(anchor=tk.W)
        self.entry_independiente = tk.Entry(
            master=self.frame_principal,
            textvariable=self.stringvar_independiente,
            width=30
        )
        self.entry_independiente.pack()
        self.label_error_independiente = tk.Label(
            master=self.frame_principal,
            text="",
            fg="red",
            wraplength=300
        )
        self.label_error_independiente.pack(anchor=tk.W)
    
    def validar_coef_cuadratico(self, *args) -> None:
        """Valida que el campo coeficiente cuadrático solo tenga números."""
        cuadratico = self.stringvar_coef_cuadratico.get()
        patron = r"^-?(([1-9][0-9]*)(\.[0-9]+)?|0\.0*[1-9]+[0-9]*)$"
        if not cuadratico:
            self.label_error_cuadratico.config(text="Campo requerido.")
            self.campos_validos["cuadratico"] = False
        elif not re.match(pattern=patron, string=cuadratico):
            self.label_error_cuadratico.config(text="Ingrese solo números.")
            self.campos_validos["cuadratico"] = False
        else:
            self.label_error_cuadratico.config(text="")
            self.campos_validos["cuadratico"] = True
        self.actualizar_boton_enviar()
    
    def validar_coef_lineal(self, *args) -> None:
        """Valida que el campo coeficiente lineal solo tenga números."""
        lineal = self.stringvar_coef_lineal.get()
        if not lineal:
            self.label_error_lineal.config(text="Campo requerido.")
            self.campos_validos["lineal"] = False
        elif not re.match(pattern=r"^[-]?[0-9]+(\.[0-9]+)?$", string=lineal):
            self.label_error_lineal.config(text="Ingrese solo números.")
            self.campos_validos["lineal"] = False
        else:
            self.label_error_lineal.config(text="")
            self.campos_validos["lineal"] = True
        self.actualizar_boton_enviar()
    
    def validar_independiente(self, *args) -> None:
        """Valida que el campo término independiente solo tenga números."""
        independiente = self.stringvar_independiente.get()
        if not independiente:
            self.label_error_independiente.config(text="Campo requerido.")
            self.campos_validos["independiente"] = False
        elif not re.match(pattern=r"^[-]?[0-9]+(\.[0-9]+)?$", string=independiente):
            self.label_error_independiente.config(text="Ingrese solo números.")
            self.campos_validos["independiente"] = False
        else:
            self.label_error_independiente.config(text="")
            self.campos_validos["independiente"] = True
        self.actualizar_boton_enviar()
    
    def actualizar_boton_enviar(self) -> None:
        """Actualiza el estado del botón de acuerdo a la validación de los campos."""
        if all(self.campos_validos.values()):
            self.button_calcular.config(state=tk.NORMAL)
        else:
            self.button_calcular.config(state=tk.DISABLED)
    
    def enviar_formulario(self) -> None:
        """Obtiene los datos para mostrar lo requerido."""
        cuadratico = float(self.stringvar_coef_cuadratico.get())
        lineal = float(self.stringvar_coef_lineal.get())
        independiente = float(self.stringvar_independiente.get())
        
        ecuacion = EcuacionGrado2(
            numA=cuadratico,
            numB=lineal,
            numC=independiente
        )
        mensaje = ecuacion.mostrar_soluciones()
        messagebox.showinfo(title="Resumen", message=mensaje)
        self.limpiar_campos()
        
    def limpiar_campos(self) -> None:
        """Limpiar todos los campos del formulario."""
        self.stringvar_coef_cuadratico.set(value="")
        self.stringvar_coef_lineal.set(value="")
        self.stringvar_independiente.set(value="")
        
        self.label_error_cuadratico.config(text="")
        self.label_error_lineal.config(text="")
        self.label_error_independiente.config(text="")
        
        self.entry_cuadratico.focus()


def main() -> None:
    root = tk.Tk()
    EcuacionApp(root=root)
    root.mainloop()

main()
