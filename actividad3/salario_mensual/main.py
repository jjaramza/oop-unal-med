import tkinter as tk
from tkinter import messagebox
import re
from salario import SalarioMensual

class SalarioApp:
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Salario mensual")
        self.root.geometry("300x350")
        self.root.resizable(False, False)
        
        # Frame principal
        self.frame_principal = tk.Frame(master=self.root, padx=20, pady=20)
        self.frame_principal.pack(expand=True)
        
        # Variables para almacenar los valores de entrada
        self.stringvar_nombre = tk.StringVar()
        self.stringvar_salario_hora = tk.StringVar()
        self.stringvar_horas_mes = tk.StringVar()
        
        # Validaciones en tiempo real
        self.stringvar_nombre.trace_add(mode="write", callback=self.validar_nombre)
        self.stringvar_salario_hora.trace_add(mode="write", callback=self.validar_salario_hora)
        self.stringvar_horas_mes.trace_add(mode="write", callback=self.validar_horas_mes)
        
        # Método para crear campos del formulario
        self.crear_campos_formulario()
        
        # Botón para enviar
        self.button_enviar = tk.Button(
            master=self.frame_principal,
            text="Aceptar",
            command=self.enviar_formulario,
            height=2,
            width=20,
            state=tk.DISABLED
        )
        self.button_enviar.pack(pady=10)
        
        # Estado de validación de los campos
        self.campos_validos = {
            "nombre": False,
            "salario": False,
            "horas": False
        }
    
    def crear_campos_formulario(self) -> None:
        """Campos del formulario con sus etiquetas."""
        # Campo nombre
        tk.Label(master=self.frame_principal, text="Nombre empleado:").pack(anchor=tk.W)
        self.entry_nombre = tk.Entry(
            master=self.frame_principal,
            textvariable=self.stringvar_nombre,
            width=30
        )
        self.entry_nombre.focus()
        self.entry_nombre.pack()
        self.label_error_nombre = tk.Label(
            master=self.frame_principal,
            text="",
            fg="red",
            wraplength=300
        )
        self.label_error_nombre.pack(anchor=tk.W)
        
        # Campo salario básico por hora
        tk.Label(master=self.frame_principal, text="Salario básico por hora:").pack(anchor=tk.W)
        self.entry_salario_hora = tk.Entry(
            master=self.frame_principal,
            textvariable=self.stringvar_salario_hora,
            width=30
        )
        self.entry_salario_hora.pack()
        self.label_error_salario_hora = tk.Label(
            master=self.frame_principal,
            text="",
            fg="red",
            wraplength=300
        )
        self.label_error_salario_hora.pack(anchor=tk.W)
        
        # Campo horas trabajadas en el mes
        tk.Label(master=self.frame_principal, text="Horas trabajadas en el mes:").pack(anchor=tk.W)
        self.entry_horas_mes = tk.Entry(
            master=self.frame_principal,
            textvariable=self.stringvar_horas_mes,
            width=30
        )
        self.entry_horas_mes.pack()
        self.label_error_horas_mes = tk.Label(
            master=self.frame_principal,
            text="",
            fg="red",
            wraplength=300
        )
        self.label_error_horas_mes.pack(anchor=tk.W)
    
    def validar_nombre(self, *args) -> None:
        """Valida que el campo nombre contenga solo letras y espacios."""
        nombre = self.stringvar_nombre.get()
        if not nombre:
            self.label_error_nombre.config(text="Campo requerido.")
            self.campos_validos["nombre"] = False
        elif not re.match(pattern=r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", string=nombre):
            self.label_error_nombre.config(text="Ingrese solo letras.")
            self.campos_validos["nombre"] = False
        else:
            self.label_error_nombre.config(text="")
            self.campos_validos["nombre"] = True
        self.actualizar_boton_enviar()
    
    def validar_salario_hora(self, *args) -> None:
        """Valida que el campo salario básico por hora solo contenga números."""
        salario = self.stringvar_salario_hora.get()
        if not salario:
            self.label_error_salario_hora.config(text="Campo requerido.")
            self.campos_validos["salario"] = False
        elif not re.match(pattern=r"^[0-9]+(\.[0-9]+)?$", string=salario):
            self.label_error_salario_hora.config(text="Ingrese solo números.")
            self.campos_validos["salario"] = False
        else:
            self.label_error_salario_hora.config(text="")
            self.campos_validos["salario"] = True
        self.actualizar_boton_enviar()
    
    def validar_horas_mes(self, *args) -> None:
        """Valida que el campo horas del mes solo contenga números."""
        horas = self.stringvar_horas_mes.get()
        if not horas:
            self.label_error_horas_mes.config(text="Campo requerido.")
            self.campos_validos["horas"] = False
        elif not re.match(pattern=r"^[0-9]+(\.[0-9]+)?$", string=horas):
            self.label_error_horas_mes.config(text="Ingrese solo números.")
            self.campos_validos["horas"] = False
        else:
            self.label_error_horas_mes.config(text="")
            self.campos_validos["horas"] = True
        self.actualizar_boton_enviar()
    
    def actualizar_boton_enviar(self) -> None:
        """Actualiza el estado del botón de acuerdo a la validación de los campos."""
        if all(self.campos_validos.values()):
            self.button_enviar.config(state=tk.NORMAL)
        else:
            self.button_enviar.config(state=tk.DISABLED)
    
    def enviar_formulario(self) -> None:
        """Obtiene los datos para mostrar lo requerido."""
        nombre = self.stringvar_nombre.get().strip()
        salario_hora = float(self.stringvar_salario_hora.get())
        horas_mes = float(self.stringvar_horas_mes.get())
        
        salario_mensual = SalarioMensual(
            nombre_empleado=nombre,
            salario_hora=salario_hora,
            horas_mes=horas_mes
            )
        mensaje = salario_mensual.mostrar_info_empleado()
        messagebox.showinfo(title="Resume", message=mensaje)
        self.limpiar_campos()
        
    def limpiar_campos(self) -> None:
        """Limpiar todos los campos del formulario."""
        self.stringvar_nombre.set(value="")
        self.stringvar_salario_hora.set(value="")
        self.stringvar_horas_mes.set(value="")
        
        self.label_error_nombre.config(text="")
        self.label_error_salario_hora.config(text="")
        self.label_error_horas_mes.config(text="")
        
        self.entry_nombre.focus()


def main() -> None:
    root = tk.Tk()
    SalarioApp(root=root)
    root.mainloop()

main()
