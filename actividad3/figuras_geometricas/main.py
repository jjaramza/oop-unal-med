import tkinter as tk
from tkinter import ttk
from figuras import Circulo, Cuadrado, Rectangulo, Rombo, Trapecio, TrianguloRectangulo

# Constantes de configuración
FONT_TITLE = ("Arial", 16, "bold")
FONT_BUTTON = ("Arial", 12, "bold")
COLOR_TITLE = "blue"

class CreateFrame:
    def __init__(self, frame: tk.Frame, titulo: str) -> None:
        self.frame = frame
        self.titulo = titulo
        self.frame.pack(expand=True)
        
        self.entries = {}  # Diccionario para almacenar las entradas
        
        self._crear_titulo()
        self._agregar_campos()
        self._crear_botones()
        self._crear_resultados()
    
    def _crear_titulo(self):
        ttk.Label(
            master=self.frame,
            text=self.titulo,
            font=FONT_TITLE,
            foreground=COLOR_TITLE
        ).grid(column=0, row=0, columnspan=2, padx=20, pady=20)
    
    def _agregar_campos(self):
        campos = self._obtener_campos_config()
        for texto, col_label, fila_label in campos["Label"]:
            ttk.Label(master=self.frame, text=texto).grid(
                column=col_label, row=fila_label, padx=10, pady=5, sticky=tk.E
            )
        for nombre_variable, col_entry, fila_entry in campos["Entry"]:
            entry = ttk.Entry(master=self.frame, width=15)
            entry.grid(column=col_entry, row=fila_entry, padx=10, pady=5, sticky=tk.W)
            self.entries[nombre_variable] = entry
        list(self.entries.values())[0].focus()
        
    def _crear_botones(self):
        ttk.Button(
            master=self.frame,
            text="Calcular",
            command=self.calcular_propiedades
        ).grid(column=0, row=6, padx=10, pady=20)

        ttk.Button(
            master=self.frame,
            text="Limpiar",
            command=self.limpiar_campos
        ).grid(column=1, row=6, padx=10, pady=20)
        
    def _crear_resultados(self):
        self.text_resultados = tk.Text(
            self.frame,
            width=30,
            height=4,
            state="disabled"
        )
        self.text_resultados.grid(column=0, row=7, columnspan=2, padx=20, pady=20)

    def _obtener_campos_config(self):
        return {
            "Círculo": {
                "Label": [("Radio (cm):", 0, 1)],
                "Entry": [("entry_radio_circulo", 1, 1)]
            },
            "Cuadrado": {
                "Label": [("Lado (cm):", 0, 1)],
                "Entry": [("entry_lado_cuadrado", 1, 1)]
            },
            "Rectángulo": {
                "Label": [
                    ("Base (cm):", 0, 1),
                    ("Altura (cm):", 0, 2)
                ],
                "Entry": [
                    ("entry_base_rectangulo", 1, 1),
                    ("entry_altura_rectangulo", 1, 2)
                ]
            },
            "Rombo": {
                "Label": [
                    ("Diagonal mayor (cm):", 0, 1),
                    ("Diagonal menor (cm):", 0, 2)
                ],
                "Entry": [
                    ("entry_diagmayor_rombo", 1, 1),
                    ("entry_diagmenor_rombo", 1, 2)
                ]
            },
            "Trapecio": {
                "Label": [
                    ("Base mayor (cm):", 0, 1),
                    ("Base menor (cm):", 0, 2),
                    ("Lado 1 (cm):", 0, 3),
                    ("Lado 2 (cm):", 0, 4),
                    ("Altura (cm):", 0, 5)
                ],
                "Entry": [
                    ("entry_base_mayor_trapecio", 1, 1),
                    ("entry_base_menor_trapecio", 1, 2),
                    ("entry_lado1_trapecio", 1, 3),
                    ("entry_lado2_trapecio", 1, 4),
                    ("entry_altura_trapecio", 1, 5)
                ]
            },
            "Triángulo Rectángulo": {
                "Label": [
                    ("Base (cm):", 0, 1),
                    ("Altura (cm):", 0, 2)
                ],
                "Entry": [
                    ("entry_base_triangulo", 1, 1),
                    ("entry_altura_triangulo", 1, 2)
                ]
            }
        }.get(self.titulo, {})
    
    def calcular_propiedades(self):
        self.text_resultados.config(state="normal")
        try:
            lista_args = [float(entry.get()) for entry in self.entries.values()]
            figuras = {
                "Círculo": Circulo,
                "Cuadraro": Cuadrado,
                "Rectángulo": Rectangulo,
                "Rombo": Rombo,
                "Trapecio": Trapecio,
                "Triángulo Rectángulo": TrianguloRectangulo
            }
            figura = figuras[self.titulo](*lista_args)
            area = figura.calcular_area()
            perimetro = figura.calcular_perimetro()
            
            self.text_resultados.delete(1.0, "end")
            self.text_resultados.insert(
                1.0, f"Área = {area:.2f} cm²\nPerímetro = {perimetro:.2f} cm"
            )
            
            if self.titulo == "Triángulo Rectángulo":
                self.text_resultados.insert(
                    tk.END, f"\n{figura.determinar_tipo_triangulo()}"
                )
        except ValueError:
            self.text_resultados.delete(1.0, "end")
            self.text_resultados.insert(1.0, "Por favor, ingrese números válidos.")
        self.text_resultados.config(state="disabled")        
    
    def limpiar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, "end")
        list(self.entries.values())[0].focus()
        self.text_resultados.config(state="normal")
        self.text_resultados.delete(1.0, "end")
        self.text_resultados.config(state="disabled")


class FigurasGeometricasApp:
    def __init__(self, root=tk.Tk) -> None:
        self.root = root
        self.root.title("Figuras Geométricas")
        self.root.minsize(width=350, height=300)
        self.root.resizable(False, False)
        
        self.frame_actual = tk.Frame(master=self.root)
        self.frame_actual.pack(expand=True)
        
        self._crear_menu()
        
        tk.Label(
            master=self.frame_actual,
            text="Figuras\nGeométricas",
            font=("Arial", 20, "bold"),
            fg="blue"
        ).pack()
    
    def _crear_menu(self):
        barra_menu = tk.Menu()
        menu_figuras = tk.Menu(master=barra_menu, tearoff=False)
        
        figuras = ["Círculo", "Cuadrado", "Rectángulo", "Rombo", "Trapecio", "Triángulo Rectángulo"]
        for figura in figuras:
            menu_figuras.add_command(
                label=figura, command=lambda f=figura: self.cambiar_frame(f)
            )

        menu_figuras.add_separator()
        menu_figuras.add_command(label="Salir", command=self.root.destroy)
        
        barra_menu.add_cascade(menu=menu_figuras, label="Figuras")
        self.root.config(menu=barra_menu)

    def cambiar_frame(self, titulo: str):
        if self.frame_actual:
            self.frame_actual.destroy()
        
        self.frame_actual = tk.Frame(master=self.root)
        self.frame_actual.pack(expand=True)
        CreateFrame(self.frame_actual, titulo)

   
def main() -> None:
    root = tk.Tk()
    FigurasGeometricasApp(root=root)
    root.mainloop()

if __name__ == "__main__":
    main()
