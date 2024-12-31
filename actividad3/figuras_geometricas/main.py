import tkinter as tk
from circulo import Circulo
from cuadrado import Cuadrado
from rectangulo import Rectangulo
from rombo import Rombo
from trapecio import Trapecio
from triangulo_rectangulo import TrianguloRectangulo

class CreateFrame:
    def __init__(self, frame: tk.Frame, titulo: str) -> None:
        self.frame = frame
        self.titulo = titulo
        self.frame.pack(expand=True)
        
        # Título del frame
        self.label_titulo = tk.Label(
            master=self.frame,
            text=self.titulo,
            font=("Arial", 16, "bold"),
            fg="blue"
        )
        self.label_titulo.grid(column=0, row=0, columnspan=2, padx=20, pady=20)
        
        # Agregar los campos del formulario
        self.agregar_campos()
        
        # Botón para calcular
        self.button_calcular = tk.Button(
            master=self.frame,
            text="Calcular",
            width=10,
            font=("Arial", 12, "bold"),
            command=self.calcular_propiedades
        )
        self.button_calcular.grid(column=0, row=6, padx=10, pady=20)
        
        # Botón para limpiar campos
        self.button_limpiar = tk.Button(
            master=self.frame,
            text="Limpiar",
            width=10,
            font=("Arial", 12, "bold"),
            command=self.limpiar_campos
        )
        self.button_limpiar.grid(column=1, row=6, padx=10, pady=20)
        
        # Campo de Texo para mostrar los resultados
        self.text_resultados = tk.Text(
            self.frame,
            width=30,
            height=4,
            state="disabled"
        )
        self.text_resultados.grid(column=0, row=7, columnspan=2, padx=20, pady=20)
    
    def agregar_campos(self):
        if self.titulo == "Círculo":
            # Campo Radio
            tk.Label(master=self.frame, text="Radio (cm):").grid(column=0, row=1, padx=10, pady=5, sticky=tk.E)
            self.entry_circulo = tk.Entry(master=self.frame, width=15)
            self.entry_circulo.focus()
            self.entry_circulo.grid(column=1, row=1, padx=10, pady=5, sticky=tk.W)
        elif self.titulo == "Cuadrado":
            # Campo Longitud lado
            tk.Label(master=self.frame, text="Lado (cm):").grid(column=0, row=1, padx=10, pady=5, sticky=tk.E)
            self.entry_cuadrado = tk.Entry(master=self.frame, width=15)
            self.entry_cuadrado.focus()
            self.entry_cuadrado.grid(column=1, row=1, padx=10, pady=5, sticky=tk.W)
        elif self.titulo == "Rectángulo":
            # Campo Base
            tk.Label(master=self.frame, text="Base (cm):").grid(column=0, row=1, padx=10, pady=5, sticky=tk.E)
            self.entry_rect_base = tk.Entry(master=self.frame, width=15)
            self.entry_rect_base.focus()
            self.entry_rect_base.grid(column=1, row=1, padx=10, pady=5, sticky=tk.W)
            
            # Campo Altura
            tk.Label(master=self.frame, text="Altura (cm):").grid(column=0, row=2, padx=10, pady=5, sticky=tk.E)
            self.entry_rect_altura = tk.Entry(master=self.frame, width=15)
            self.entry_rect_altura.grid(column=1, row=2, padx=10,pady=5, sticky=tk.W)
        elif self.titulo == "Rombo":
            # Campo Longitud diagonal mayor
            tk.Label(master=self.frame, text="Diagonal mayor (cm):").grid(column=0, row=1, padx=10, pady=5, sticky=tk.E)
            self.entry_rombo_dgmayor = tk.Entry(master=self.frame, width=15)
            self.entry_rombo_dgmayor.focus()
            self.entry_rombo_dgmayor.grid(column=1, row=1, padx=10, pady=5, sticky=tk.W)
            
            # Campo Longitud diagonal mayor
            tk.Label(master=self.frame, text="Diagonal menor (cm):").grid(column=0, row=2, padx=10, pady=5, sticky=tk.E)
            self.entry_rombo_dgmenor = tk.Entry(master=self.frame, width=15)
            self.entry_rombo_dgmenor.grid(column=1, row=2, padx=10, pady=5, sticky=tk.W)
        elif self.titulo == "Trapecio":
            # Campo Longitud lado 1
            tk.Label(master=self.frame, text="Lado 1 (cm):").grid(column=0, row=1, padx=10, pady=5, sticky=tk.E)
            self.entry_trap_lg1 = tk.Entry(master=self.frame, width=15)
            self.entry_trap_lg1.focus()
            self.entry_trap_lg1.grid(column=1, row=1, padx=10, pady=5, sticky=tk.W)
            
            # Campo Longitud lado 2
            tk.Label(master=self.frame, text="Lado 2 (cm):").grid(column=0, row=2, padx=10, pady=5, sticky=tk.E)
            self.entry_trap_lg2 = tk.Entry(master=self.frame, width=15)
            self.entry_trap_lg2.grid(column=1, row=2, padx=10, pady=5, sticky=tk.W)
            
            # Campo Longitud Base Mayor
            tk.Label(master=self.frame, text="Base mayor (cm):").grid(column=0, row=3, padx=10, pady=5, sticky=tk.E)
            self.entry_trap_basemayor = tk.Entry(master=self.frame, width=15)
            self.entry_trap_basemayor.grid(column=1, row=3, padx=10, pady=5, sticky=tk.W)
            
            # Campo Longitud Base Menor
            tk.Label(master=self.frame, text="Base menor (cm):").grid(column=0, row=4, padx=10, pady=5, sticky=tk.E)
            self.entry_trap_basemenor = tk.Entry(master=self.frame, width=15)
            self.entry_trap_basemenor.grid(column=1, row=4, padx=10, pady=5, sticky=tk.W)
            
            # Campo Longitud altura
            tk.Label(master=self.frame, text="Altura (cm):").grid(column=0, row=5, padx=10, pady=5, sticky=tk.E)
            self.entry_trap_altura = tk.Entry(master=self.frame, width=15)
            self.entry_trap_altura.grid(column=1, row=5, padx=10, pady=5, sticky=tk.W)
        elif self.titulo == "Triángulo Rectángulo":
            # Campo Base
            tk.Label(master=self.frame, text="Base (cm):").grid(column=0, row=1, padx=10, pady=5, sticky=tk.E)
            self.entry_trirect_base = tk.Entry(master=self.frame, width=15)
            self.entry_trirect_base.focus()
            self.entry_trirect_base.grid(column=1, row=1, padx=10, pady=5, sticky=tk.W)
            
            # Campo Altura
            tk.Label(master=self.frame, text="Altura (cm):").grid(column=0, row=2, padx=10, pady=5, sticky=tk.E)
            self.entry_trirect_altura = tk.Entry(master=self.frame, width=15)
            self.entry_trirect_altura.grid(column=1, row=2, padx=10,pady=5, sticky=tk.W)

    def calcular_propiedades(self):
        self.text_resultados.config(state="normal")
        try:
            self.text_resultados.delete(1.0, "end")
            if self.titulo == "Círculo":
                circulo = Circulo(radio=float(self.entry_circulo.get()))
                area = circulo.calcular_area()
                perimetro = circulo.calcular_perimetro()
            elif self.titulo == "Cuadrado":
                cuadrado = Cuadrado(lado=float(self.entry_cuadrado.get()))
                area = cuadrado.calcular_area()
                perimetro = cuadrado.calcular_perimetro()
            elif self.titulo == "Rectángulo":
                rectangulo = Rectangulo(
                    base=float(self.entry_rect_base.get()),
                    altura=float(self.entry_rect_altura.get())
                )
                area = rectangulo.calcular_area()
                perimetro = rectangulo.calcular_perimetro()
            elif self.titulo == "Rombo":
                rombo = Rombo(
                    diagonal_mayor=float(self.entry_rombo_dgmayor.get()),
                    diagonal_menor=float(self.entry_rombo_dgmenor.get())
                )
                area = rombo.calcular_area()
                perimetro = rombo.calcular_perimetro()
            elif self.titulo == "Trapecio":
                trapecio = Trapecio(
                    base_mayor=float(self.entry_trap_basemayor.get()),
                    base_menor=float(self.entry_trap_basemenor.get()),
                    lado_1=float(self.entry_trap_lg1.get()),
                    lado_2=float(self.entry_trap_lg2.get()),
                    altura=float(self.entry_trap_altura.get())
                )
                area = trapecio.calcular_area()
                perimetro = trapecio.calcular_perimetro()
            elif self.titulo == "Triángulo Rectángulo":
                tri_rect = TrianguloRectangulo(
                    base=float(self.entry_trirect_base.get()),
                    altura=float(self.entry_trirect_altura.get())
                )
                area = tri_rect.calcular_area()
                perimetro = tri_rect.calcular_perimetro()
                self.text_resultados.insert(
                    tk.END,
                    f"\n{tri_rect.determinar_tipo_triangulo()}"
                )
            self.text_resultados.insert(
                1.0,
                f"Área = {area:.2f} cm²\nPerímetro = {perimetro:.2f} cm"
            )
        except:
            self.text_resultados.delete(1.0, "end")
            self.text_resultados.insert(1.0, "Por favor, ingrese solo\nnúmeros positivos.")
        self.text_resultados.config(state="disabled")
    
    def limpiar_campos(self):
        pass


class FigurasGeometricasApp:
    def __init__(self, root=tk.Tk) -> None:
        self.root = root
        self.root.title("Figuras Geométricas")
        self.root.minsize(width=350, height=300)
        self.root.resizable(False, False)
        
        # Contenedor para los Frames
        self.frame = tk.Frame(master=self.root)
        self.frame.pack(expand=True)
        
        # Contenedor actual
        self.frame_actual = tk.Frame(master=self.frame)
        self.frame_actual.pack(expand=True)
        
        # Título inicial
        tk.Label(
            master=self.frame_actual,
            text="Figuras\nGeométricas",
            font=("Arial", 20, "bold"),
            fg="blue"
        ).pack()
        
        # Creación del Menú
        self.barra_menu = tk.Menu()
        self.menu_figuras = tk.Menu(master=self.barra_menu, tearoff=False)
          
        # Agregar comandos al Menú Figuras
        self.menu_figuras.add_command(
            label="Círculo", command=lambda: self.cambiar_frame("Círculo")
        )
        self.menu_figuras.add_command(
            label="Cuadrado", command=lambda: self.cambiar_frame("Cuadrado")
        )
        self.menu_figuras.add_command(
            label="Rectángulo", command=lambda: self.cambiar_frame("Rectángulo")
        )
        self.menu_figuras.add_command(
            label="Rombo", command=lambda: self.cambiar_frame("Rombo")
        )
        self.menu_figuras.add_command(
            label="Trapecio", command=lambda: self.cambiar_frame("Trapecio")
        )
        self.menu_figuras.add_command(
            label="Triángulo Rectángulo", command=lambda: self.cambiar_frame("Triángulo Rectángulo")
        )
        self.menu_figuras.add_separator()
        self.menu_figuras.add_command(
            label="Salir", command=self.root.destroy
        )
        
        # Agregar el Menú a la ventana
        self.barra_menu.add_cascade(menu=self.menu_figuras, label="Figuras")
        self.root.config(menu=self.barra_menu)
        
    def cambiar_frame(self, titulo: str):
        # Destruir el frame actual en caso de existir
        if self.frame_actual:
            self.frame_actual.destroy()
        
        # Crear un nuevo frame y actualizar la referencia
        self.frame_actual = tk.Frame(master=self.frame)
        self.frame_actual.pack(expand=True)
        
        # Crear el contenido del nuevo frame
        CreateFrame(self.frame_actual, titulo)

   
def main() -> None:
    root = tk.Tk()
    FigurasGeometricasApp(root=root)
    root.mainloop()

main()
