# Ejercicio propuesto No 19 del Capítulo 3. Libro de Lógica de Programación de Efrain Oviedo.

import flet as ft
from equilatero import Equilatero

class EquilateroApp:

    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Triángulo Equilátero"
        self.page.window.width = 750
        self.page.window.height = 450
        self.page.window.resizable = False
        self.page.window.maximizable = False

        # Campo para solicitar el dato al usuario
        self.lado_entrada = ft.TextField(
            label="Lado",
            width=300,
            prefix_icon=ft.CupertinoIcons.TRIANGLE_FILL,
            helper_text="Valor en centímetros",
            input_filter=ft.InputFilter(allow=True, regex_string=r"^\d*\.?\d*$", replacement_string="")
        )

        # Botones
        self.calcular_boton = ft.ElevatedButton(
            width=200,
            height=40,
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.CALCULATE),
                    ft.Text(value="Calcular", size=16)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            ),
            style=ft.ButtonStyle(
                color={
                    ft.ControlState.DEFAULT: ft.Colors.WHITE
                },
                bgcolor={
                    ft.ControlState.DEFAULT: ft.Colors.GREEN_700,
                    ft.ControlState.HOVERED: ft.Colors.GREEN_900,
                }
            ),
            on_click=self.calcular_propiedades
        )
        self.limpiar_boton = ft.ElevatedButton(
            width=200,
            height=40,
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.CLEAR),
                    ft.Text(value="Limpiar", size=16)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            ),
            style=ft.ButtonStyle(
                color={
                    ft.ControlState.DEFAULT: ft.Colors.WHITE
                },
                bgcolor={
                    ft.ControlState.DEFAULT: ft.Colors.BLUE_700,
                    ft.ControlState.HOVERED: ft.Colors.BLUE_900,
                }
            ),
            on_click=self.limpiar_datos
        )

        # Texto plano para mostrar el cálculo
        self.perimetro_texto = ft. Text(
            value="0.00",
            size=16,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_500
        )
        self.altura_texto = ft.Text(
            value="0.00",
            size=16,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_500
        )
        self.area_texto = ft.Text(
            value="0.00",
            size=16,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_500
        )
        self.datos_resumen_texto = ft.Column(
            controls=[
                self.perimetro_texto,
                self.altura_texto,
                self.area_texto
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.END
        )

        # Etiquetas de los cálculos que se realizarán
        self.resumen_texto = ft.Column(
            controls=[
                ft.Text(
                    value="Perímetro (cm): ",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                ),
                ft.Text(
                    value="Altura (cm): ",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                ),
                ft.Text(
                    value="Área (cm²): ",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                )
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.END
        )

        # Fila donde se almacena las etiquetas y los campos calculados
        self.resumen_fila = ft.Row(
            controls=[
                self.resumen_texto,
                self.datos_resumen_texto
            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        )

        # Crear contenedor donde se almacenarán todos los widgets
        self.titulo_contenedor = ft.Container(
            content=ft.Text(
                value="Triángulo Equilátero",
                size=24,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_500
            ),
            padding=20,
            alignment=ft.Alignment(0.0, 0.0)
        )
        self.entrada_contenedor = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value="Ingreso",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLACK
                    ),
                    ft.Divider(),
                    self.lado_entrada,
                    self.calcular_boton,
                    ft.Text(
                        value="*Solo se deben ingresar valores numéricos",
                        size=14,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLACK
                    ),
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            height=300,
            border_radius=10,
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.all(width=1, color=ft.Colors.GREY_300),
            expand=True
        )
        self.salida_contenedor = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value="Resumen",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLACK
                    ),
                    ft.Divider(),
                    self.resumen_fila,
                    self.limpiar_boton
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            height=300,
            border_radius=10,
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.all(width=1, color=ft.Colors.GREY_300),
            expand=True
        )

        # Se agregan los widgets a la página
        self.page.add(
            self.titulo_contenedor,
            ft.Row(
                controls=[
                    self.entrada_contenedor,
                    self.salida_contenedor
                ]
            )
        )

    def calcular_propiedades(self, e):
        lado = self.lado_entrada.value
        if lado == "":
            snack_bar = ft.SnackBar(
                content=ft.Text("El campo no puede estar vacío.")
            )
            self.page.overlay.append(snack_bar)
            snack_bar.open = True
            self.page.update()
        else:
            equilatero = Equilatero(float(lado))
            perimetro = equilatero.perimetro_equilatero()
            altura = equilatero.altura_equilatero()
            area = equilatero.area_equilatero()

            self.perimetro_texto.value = f"{perimetro:.2f}"
            self.altura_texto.value = f"{altura:.2f}"
            self.area_texto.value = f"{area:.2f}"

            self.page.update()
        return e

    def limpiar_datos(self, e):
        self.perimetro_texto.value = "0.00"
        self.area_texto.value = "0.00"
        self.altura_texto.value = "0.00"
        self.lado_entrada.value = ""
        self.page.update()
        return e


def main(page: ft.Page):
    EquilateroApp(page)

ft.app(target=main)
