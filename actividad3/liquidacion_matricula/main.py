import tkinter as tk
from tkinter import messagebox, ttk
import re
from liquidacion import Liquidacion

class LiquidacionApp:
    
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Liquidación de Matrícula")
        self.root.geometry("300x350")
        self.root.resizable(False, False)
        
        # Frame principal
        self.frame_principal = tk.Frame(master=self.root, padx=20, pady=20)
        self.frame_principal.pack(expand=True)
        
        # Variables para almacenar los valores de entrada
        self.stringvar_inscripcion = tk.StringVar()
        self.stringvar_nombre = tk.StringVar()
        self.stringvar_patrimonio = tk.StringVar()
        self.stringvar_estrato = tk.StringVar()
        
        # Validaciones en tiempo real
        self.stringvar_inscripcion.trace_add(mode="write", callback=self.validar_inscripcion)
        self.stringvar_nombre.trace_add(mode="write", callback=self.validar_nombre)
        self.stringvar_patrimonio.trace_add(mode="write", callback=self.validar_patrimonio)
        self.stringvar_estrato.trace_add(mode="write", callback=self.validar_estrato)
        
        # Método para crear los campos del formulario
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
            "inscripcion": False,
            "nombre": False,
            "patrimonio": False,
            "estrato": False
        }
        
    def crear_campos_formulario(self) -> None:
        """Campos del formulario con sus etiquetas."""
        # Campo número de inscripción
        tk.Label(master=self.frame_principal, text="Número inscripción:").pack(anchor=tk.W)
        self.entry_inscripcion = tk.Entry(
            master=self.frame_principal,
            textvariable=self.stringvar_inscripcion,
            width=30
        )
        self.entry_inscripcion.focus()
        self.entry_inscripcion.pack()
        self.label_error_inscripcion = tk.Label(
            master=self.frame_principal,
            text="",
            fg="red",
            wraplength=300
        )
        self.label_error_inscripcion.pack(anchor=tk.W)
        
        # Campo Nombre del estudiante
        tk.Label(master=self.frame_principal, text="Nombre estudiante:").pack(anchor=tk.W)
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
        
        # Campo Patrimonio
        tk.Label(master=self.frame_principal, text="Patrimonio ($):").pack(anchor=tk.W)
        self.entry_patrimonio = tk.Entry(
            master=self.frame_principal,
            textvariable=self.stringvar_patrimonio,
            width=30
        )
        self.entry_patrimonio.pack()
        self.label_error_patrimonio = tk.Label(
            master=self.frame_principal,
            text="",
            fg="red",
            wraplength=300
        )
        self.label_error_patrimonio.pack(anchor=tk.W)
        
        # Campo Estrado social
        tk.Label(master=self.frame_principal, text="Estrato social:").pack(anchor=tk.W)
        self.combobox_estrato = ttk.Combobox(
            master=self.frame_principal,
            textvariable=self.stringvar_estrato,
            width=27,
            state="readonly",
            values=["1", "2", "3", "4", "5", "6"]
        )
        self.combobox_estrato.pack()
        
        # Etiqueda vacía
        self.label_vacia = tk.Label(
            master=self.frame_principal,
            text="",
            wraplength=300
        )
        self.label_vacia.pack(anchor=tk.W)
    
    def validar_inscripcion(self, *args) -> None:
        """Valida que el campo del número inscripción no esté vacío."""
        inscripcion = self.stringvar_inscripcion.get()
        if not inscripcion:
            self.label_error_inscripcion.config(text="Campo requerido.")
            self.campos_validos["inscripcion"] = False
        else:
            self.label_error_inscripcion.config(text="")
            self.campos_validos["inscripcion"] = True
        self.actualizar_boton_enviar()
    
    def validar_nombre(self, *args) -> None:
        """Valida que el campo nombre estudiante contenga solo letras y espacios."""
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
    
    def validar_patrimonio(self, *args) -> None:
        """Valida que el campo Patrimonio contenga solo."""
        patrimonio= self.stringvar_patrimonio.get()
        if not patrimonio:
            self.label_error_patrimonio.config(text="Campo requerido.")
            self.campos_validos["patrimonio"] = False
        elif not re.match(pattern=r"^[1-9][0-9]*$", string=patrimonio):
            self.label_error_patrimonio.config(text="Ingrese solo números.")
            self.campos_validos["patrimonio"] = False
        else:
            self.label_error_patrimonio.config(text="")
            self.campos_validos["patrimonio"] = True
        self.actualizar_boton_enviar()
    
    def validar_estrato(self, *args) -> None:
        """Valida que el campo estrato social no esté vacío."""
        estrato = self.combobox_estrato.get()
        if not estrato:
            self.campos_validos["estrato"] = False
        else:
            self.campos_validos["estrato"] = True
        self.actualizar_boton_enviar()
    
    def actualizar_boton_enviar(self) -> None:
        """Actualiza el estado del botón de acuerdo a la validación de los campos."""
        if all(self.campos_validos.values()):
            self.button_enviar.config(state=tk.NORMAL)
        else:
            self.button_enviar.config(state=tk.DISABLED)
    
    def obtener_info_estudiante(self) -> dict:
        """Extraer la información de los campos para calcular la liquidación."""
        inscripcion = self.entry_inscripcion.get().strip()
        nombre = self.entry_nombre.get().strip()
        patrimonio = int(self.entry_patrimonio.get())
        estrato = int(self.combobox_estrato.get())
        
        estudiante = Liquidacion(
            numero_inscripcion=inscripcion,
            nombre_estudiante=nombre,
            patrimonio=patrimonio,
            estrato_social=estrato
        )
        return {
            "inscripcion": inscripcion,
            "nombre": nombre,
            "matricula": estudiante.valor_matricula()
        }
    
    def enviar_formulario(self) -> None:
        """Obtiene los datos para mostrar lo requerido."""
        info_estudiante = self.obtener_info_estudiante()
        mensaje = f"""
        Liquidación de matrícula:
        
        Número inscripción:\t{info_estudiante["inscripcion"]}
        Nombre estudiante:\t{info_estudiante["nombre"]}
        Valor matrícula:\t$ {f'{info_estudiante["matricula"]:,.0f}'.replace(",", ".")}
        """
        messagebox.showinfo(title="Resumen", message=mensaje)
        self.limpiar_campos()
    
    def limpiar_campos(self) -> None:
        """Limpiar todos los campos del formulario."""
        self.stringvar_inscripcion.set("")
        self.stringvar_nombre.set("")
        self.stringvar_patrimonio.set("")
        self.stringvar_estrato.set("")
        
        self.label_error_inscripcion.config(text="")
        self.label_error_nombre.config(text="")
        self.label_error_patrimonio.config(text="")
        
        self.entry_inscripcion.focus()


def main() -> None:
    root = tk.Tk()
    LiquidacionApp(root=root)
    root.mainloop()

main()
