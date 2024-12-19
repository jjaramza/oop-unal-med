# Ejercicio resuelto No 7 del Capítulo 4. Libro de Lógica de Programación de Efrain Oviedo.

import flet as ft
from comparacion import ComparacionNumero

class ComparacionApp:

    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Comparación de números"
        self.page.window.width = "450"
        self.page.window.height = "400"
        self.page.window.resizable = False
        self.page.window.maximizable = False

        # Campos para solicitar los números enteros
        self.valor_a_entrada = ft.TextField(
            label="Primer número",
            width=180,
            input_filter=ft.InputFilter(regex_string=r"^-?\d*$", allow=True, replacement_string="")
        )
        self.valor_b_entrada = ft.TextField(
            label="Segundo número",
            width=180,
            input_filter=ft.InputFilter(regex_string=r"^-?\d*$", allow=True, replacement_string="")
        )

        # Botones
        self.comparar_boton = ft.ElevatedButton(
            text="Comparar",
            width=150,
            height=40,
            style=ft.ButtonStyle(
                color={
                    ft.ControlState.DEFAULT: ft.Colors.WHITE
                },
                bgcolor={
                    ft.ControlState.DEFAULT: ft.Colors.BLUE_700,
                    ft.ControlState.HOVERED: ft.Colors.BLUE_900
                }
            ),
            on_click=self.comparar_numeros
        )
        self.limpiar_boton = ft.ElevatedButton(
            text="Limpiar",
            width=150,
            height=40,
            style=ft.ButtonStyle(
                color={
                    ft.ControlState.DEFAULT: ft.Colors.WHITE
                },
                bgcolor={
                    ft.ControlState.DEFAULT: ft.Colors.RED_700,
                    ft.ControlState.HOVERED: ft.Colors.RED_900
                }
            ),
            on_click=self.limpiar_campos
        )

        # Etiqueta para mostrar el resultado
        self.resultado_comparacion_texto = ft.Text(
            value="",
            size=20,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLACK
        )

        # Contenedor para almacenar los widgets
        self.contenedor = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value="Comparar Enteros",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_700
                    ),
                    ft.Divider(),
                    ft.Row(
                        controls=[
                            self.valor_a_entrada,
                            self.valor_b_entrada,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    ft.Row(
                        controls=[
                            self.comparar_boton,
                            self.limpiar_boton,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    ft.Divider(),
                    self.resultado_comparacion_texto
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border_radius=10,
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.all(width=1, color=ft.Colors.GREY_300),
            expand=True
        )


        self.page.add(self.contenedor)

    def comparar_numeros(self, e):
        num_a = self.valor_a_entrada.value
        num_b = self.valor_b_entrada.value
        if num_a == "" or num_b == "":
            snack_bar = ft.SnackBar(
                content=ft.Text("Los campos no pueden estar vacíos.")
            )
            self.page.overlay.append(snack_bar)
            snack_bar.open = True
            self.page.update()
        elif num_a == "-" or num_b == "-":
            snack_bar = ft.SnackBar(
                content=ft.Text("Ingrese un número entero válido.")
            )
            self.page.overlay.append(snack_bar)
            snack_bar.open = True
            self.page.update()
        else:
            comparacion = ComparacionNumero(
                valor_a=int(num_a),
                valor_b=int(num_b)
            )
            resultado = comparacion.comparar()
            self.resultado_comparacion_texto.value = f"{num_a} es {resultado.value} que {num_b}"
            self.page.update()
        return e

    def limpiar_campos(self, e):
        self.valor_a_entrada.value = ""
        self.valor_b_entrada.value = ""
        self.resultado_comparacion_texto.value = ""
        self.page.update()
        return e


def main(page: ft.Page):
    ComparacionApp(page)

ft.app(target=main)
