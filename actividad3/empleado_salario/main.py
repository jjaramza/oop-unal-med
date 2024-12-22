import tkinter as tk
from tkinter import messagebox
import re
from empleado import Empleado

class NominaApp:
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Nómina empleado")
        self.root.geometry("300x450")
        self.root.resizable(False, False)
        
        # Frame principal
        self.frame_principal = tk.Frame(master=self.root, padx=20, pady=20)
        self.frame_principal.pack(expand=True)
        
        # Variables para almacenar los valores de entrada
        self.stringvar_codigo = tk.StringVar()
        self.stringvar_nombre = tk.StringVar()
        self.stringvar_horas = tk.StringVar()
        self.stringvar_valor = tk.StringVar()
        self.stringvar_retefuente = tk.StringVar()
        
        # Validaciones en tiempo real
        self.stringvar_codigo.trace_add(mode="write", callback=self.validar_codigo)
        self.stringvar_nombre.trace_add(mode="write", callback=self.validar_nombre)
        self.stringvar_horas.trace_add(mode="write", callback=self.validar_horas_trabajadas)
        self.stringvar_valor.trace_add(mode="write", callback=self.validar_valor_hora)
        self.stringvar_retefuente.trace_add(mode="write", callback=self.validar_rete_fuente)
        
        # Método para crear los campos del formulario
        self.crear_campos_formulario()
        
        # Botón para enviar
        self.button_enviar = tk.Button(
            master=self.frame_principal,
            text="Aceptar",
            command=self.enviar_formulario,
            width=20,
            state=tk.DISABLED
        )
        self.button_enviar.pack(pady=10)
        
        # Estado de validación de los campos
        self.campos_validos = {
            "codigo": False,
            "nombre": False,
            "horas": False,
            "valor": False,
            "retefuente": False
        }
        
    def crear_campos_formulario(self):
        """Campos del formulario con sus etiquetas."""
        # Campo Código empleado
        tk.Label(master=self.frame_principal, text="Código empleado:").pack(anchor=tk.W)
        self.entry_codigo = tk.Entry(
            master=self.frame_principal,
            textvariable=self.stringvar_codigo,
            width=30
        )
        self.entry_codigo.focus()
        self.entry_codigo.pack()
        self.label_error_codigo = tk.Label(
            master=self.frame_principal,
            text="",
            fg="red",
            wraplength=300
        )
        self.label_error_codigo.pack(anchor=tk.W)
        
        # Campo Nombre empleado
        tk.Label(master=self.frame_principal, text="Nombre empleado:").pack(anchor=tk.W)
        self.entry_nombre = tk.Entry(
            master=self.frame_principal,
            textvariable=self.stringvar_nombre,
            width=30
        )
        self.entry_nombre.pack()
        self.label_error_nombre = tk.Label(
            master=self.frame_principal,
            text="",
            fg="red",
            wraplength=300
        )
        self.label_error_nombre.pack(anchor=tk.W)
        
        # Campo Horas trabajadas
        tk.Label(master=self.frame_principal, text="Horas trabajadas (h):").pack(anchor=tk.W)
        self.entry_horas = tk.Entry(
            master=self.frame_principal,
            textvariable=self.stringvar_horas,
            width=30
        )
        self.entry_horas.pack()
        self.label_error_horas = tk.Label(
            master=self.frame_principal,
            text="",
            fg="red",
            wraplength=300
        )
        self.label_error_horas.pack(anchor=tk.W)
        
        # Campo Valor hora
        tk.Label(master=self.frame_principal, text="Valor hora ($):").pack(anchor=tk.W)
        self.entry_valor = tk.Entry(
            master=self.frame_principal,
            textvariable=self.stringvar_valor,
            width=30
        )
        self.entry_valor.pack()
        self.label_error_valor = tk.Label(
            master=self.frame_principal,
            text="",
            fg="red",
            wraplength=300
        )
        self.label_error_valor.pack(anchor=tk.W)
        
        # Campo Porcentaje Retención en la Fuente
        tk.Label(master=self.frame_principal, text="Retención en la Fuente (%):").pack(anchor=tk.W)
        self.entry_retefuente = tk.Entry(
            master=self.frame_principal,
            textvariable=self.stringvar_retefuente,
            width=30
        )
        self.entry_retefuente.pack()
        self.label_error_retefuente = tk.Label(
            master=self.frame_principal,
            text="",
            fg="red",
            wraplength=300
        )
        self.label_error_retefuente.pack(anchor=tk.W)
    
    def validar_codigo(self, *args):
        """Valida que el campo del código empleado no esté vacío."""
        codigo = self.stringvar_codigo.get()
        if not codigo:
            self.label_error_codigo.config(text="Campo requerido.")
            self.campos_validos["codigo"] = False
        else:
            self.label_error_codigo.config(text="")
            self.campos_validos["codigo"] = True
            self.actualizar_boton_enviar()
    
    def validar_nombre(self, *args):
        """Valida que el campo nombre empleado contenga solo letras y espacios."""
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
    
    def validar_horas_trabajadas(self, *args):
        """Valida que el campo horas trabajadas contenga solo números reales."""
        horas = self.stringvar_horas.get()
        if not horas:
            self.label_error_horas.config(text="Campo requerido.")
            self.campos_validos["horas"] = False
        elif not re.match(pattern=r"^[0-9]+(\.[0-9]+)?$", string=horas):
            self.label_error_horas.config(text="Ingrese solo números.")
            self.campos_validos["horas"] = False
        else:
            self.label_error_horas.config(text="")
            self.campos_validos["horas"] = True
            self.actualizar_boton_enviar()
    
    def validar_valor_hora(self, *args):
        """Valida que el campo valor hora solo contenga números reales."""
        valor = self.stringvar_valor.get()
        if not valor:
            self.label_error_valor.config(text="Campo requerido.")
            self.campos_validos["valor"] = False
        elif not re.match(pattern=r"^[0-9]+(\.[0-9]+)?$", string=valor):
            self.label_error_valor.config(text="Ingrese solo números.")
            self.campos_validos["valor"] = False
        else:
            self.label_error_valor.config(text="")
            self.campos_validos["valor"] = True
            self.actualizar_boton_enviar()
    
    def validar_rete_fuente(self, *args):
        """Valida que el campo rete fuente contenga solo números reales."""
        rete_fuente = self.stringvar_retefuente.get()
        if not rete_fuente:
            self.label_error_retefuente.config(text="Campo requerido.")
            self.campos_validos["retefuente"] = False
        elif not re.match(pattern=r"^[0-9]+(\.[0-9]+)?$", string=rete_fuente):
            self.label_error_retefuente.config(text="Ingrese solo números.")
            self.campos_validos["retefuente"] = False
        else:
            self.label_error_retefuente.config(text="")
            self.campos_validos["retefuente"] = True
            self.actualizar_boton_enviar()
    
    def actualizar_boton_enviar(self):
        """Actualiza el estado del botón de acuerdo a la validación de los campos."""
        if all(self.campos_validos.values()):
            self.button_enviar.config(state=tk.NORMAL)
        else:
            self.button_enviar.config(state=tk.DISABLED)
    
    def obtener_info_salario(self):
        """Extraer la información de los campos para calcular el salario."""
        codigo = self.entry_codigo.get().strip()
        nombre = self.entry_nombre.get().strip()
        horas = float(self.entry_horas.get().strip())
        valor = float(self.entry_valor.get().strip())
        rete_fuente = float(self.entry_retefuente.get().strip())
        
        empleado = Empleado(
            codigo=codigo,
            nombre=nombre,
            horas_mes=horas,
            valor_hora=valor,
            porcentaje_rete_fuente=rete_fuente
        )
        
        salario_bruto = empleado.calcular_salario_bruto()
        salario_neto = empleado.calcular_salario_neto()
        
        return {
            "codigo": codigo,
            "nombre": nombre,
            "salario_bruto": salario_bruto,
            "salario_neto": salario_neto
        }
    
    def enviar_formulario(self):
        """Obtiene los datos para mostrar lo requerido."""
        info_empleado = self.obtener_info_salario()
        mensaje = f"""
        Resumen Colilla de Pago:
        
        Código empleado:\t{info_empleado["codigo"]}
        Nombre empleado:\t{info_empleado["nombre"]}
        Salario bruto:\t\t$ {f'{info_empleado["salario_bruto"]:,.0f}'.replace(",", ".")}
        Salario neto:\t\t$ {f'{info_empleado["salario_neto"]:,.0f}'.replace(",", ".")}
        """
        messagebox.showinfo("Resumen", mensaje)
        self.limpiar_campos()
        
    def limpiar_campos(self):
        """Limpiar todos los campos del formulario."""
        self.stringvar_codigo.set("")
        self.stringvar_nombre.set("")
        self.stringvar_horas.set("")
        self.stringvar_valor.set("")
        self.stringvar_retefuente.set("")
        
        self.label_error_codigo.config(text="")
        self.label_error_nombre.config(text="")
        self.label_error_horas.config(text="")
        self.label_error_valor.config(text="")
        self.label_error_retefuente.config(text="")
        
        self.entry_codigo.focus()
        

def main():
    root = tk.Tk()
    NominaApp(root=root)
    root.mainloop()

main()
