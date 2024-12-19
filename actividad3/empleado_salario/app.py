# Ejercicio propuesto No 18 del Capítulo 3. Libro de Lógica de Programación de Efrain Oviedo.

import flet as ft
from empleado import Empleado

class EmpleadoApp:

    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Empleado"
        self.page.window.width = 850
        self.page.window.height = 620
        self.page.window.resizable = False
        self.page.window.maximizable = False

        # Crear campos de entrada de tipo TextField
        self.codigo_entrada = ft.TextField(
            label="Código empleado",
            width=300,
            prefix_icon=ft.Icons.LOCK_PERSON,
            helper_text="Código sin espacios ni puntos"
        )
        self.nombre_entrada = ft.TextField(
            label="Nombre empleado",
            width=400,
            prefix_icon=ft.Icons.PERSON,
            helper_text="Nombre completo"
        )
        self.horas_mes_entrada = ft.TextField(
            label="Horas trabajadas",
            width=230,
            prefix_icon=ft.Icons.ACCESS_TIME,
            helper_text="Horas trabajadas en el mes",
            input_filter=ft.InputFilter(allow=True, regex_string=r"^\d*\.?\d*$", replacement_string="")
        )
        self.valor_hora_entrada = ft.TextField(
            label="Valor hora",
            width=230,
            prefix_icon=ft.Icons.ATTACH_MONEY,
            helper_text="Valor sin espacios ni puntos",
            input_filter=ft.InputFilter(allow=True, regex_string=r"^\d*\.?\d*$", replacement_string="")
        )
        self.rete_fuente_entrada = ft.TextField(
            label="Retención en la fuente",
            width=230,
            prefix_icon=ft.Icons.PERCENT,
            helper_text="Porcentaje de la rete fuente",
            input_filter=ft.InputFilter(allow=True, regex_string=r"^\d*\.?\d*$", replacement_string="")
        )

        # Botones de tipo ElevateButton
        self.aceptar_boton = ft.ElevatedButton(
            width=200,
            height=40,
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.SEND),
                    ft.Text(value="Aceptar", size=16)
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
            on_click=self.agregar_fila
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
                    ft.ControlState.DEFAULT: ft.Colors.RED_700,
                    ft.ControlState.HOVERED: ft.Colors.RED_900,
                }
            ),
            on_click=self.limpiar_campos
        )

        # Crear tabla para mostrar la información del empleado
        self.info_tabla = ft.DataTable(
            border=ft.border.all(width=1, color=ft.Colors.GREY_700),
            vertical_lines=ft.BorderSide(width=1),
            horizontal_lines=ft.BorderSide(width=1),
            border_radius=10,
            columns=[
                ft.DataColumn(ft.Text(value="Código empleado", weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(value="Nombre empleado", weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(value="Salario bruto", weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(value="Salario neto", weight=ft.FontWeight.BOLD))
            ],
            rows=[]
        )

        # Crear contenedor donde se almacenarán todos los widgets
        self.container_entrada = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value="Datos Empleado",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_500
                    ),
                    ft.Row(
                        controls=[self.codigo_entrada, self.nombre_entrada],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10
                    ),
                    ft.Row(
                        controls=[self.horas_mes_entrada, self.valor_hora_entrada, self.rete_fuente_entrada],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10
                    ),
                    ft.Row(
                        controls=[self.aceptar_boton, self.limpiar_boton],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10
                    ),
                    ft.Divider(),
                    ft.Text(
                        value="Información Salario",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_500
                    ),
                    self.info_tabla
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

        # Agregar los controles a la página
        self.page.add(self.container_entrada)


    def agregar_fila(self, e):
        codigo = self.codigo_entrada.value
        nombre = self.nombre_entrada.value
        horas = self.horas_mes_entrada.value
        valor = self.valor_hora_entrada.value
        porcentaje = self.rete_fuente_entrada.value

        if codigo == "" or nombre == "" or horas == "" or valor == "" or porcentaje == "":
            snack_bar = ft.SnackBar(
                content=ft.Text("Todos los campos deben diligenciarse correctamente.")
            )
            self.page.overlay.append(snack_bar)
            snack_bar.open = True
            self.page.update()
        elif horas == "." or valor == "." or porcentaje == ".":
            snack_bar = ft.SnackBar(
                content=ft.Text("Debe ingresar valores numéricos válidos.")
            )
            self.page.overlay.append(snack_bar)
            snack_bar.open = True
            self.page.update()
        elif not self.info_tabla.rows == []:
            snack_bar = ft.SnackBar(
                content=ft.Text("Debes limpiar los campos para realizar una nueva consulta.")
            )
            self.page.overlay.append(snack_bar)
            snack_bar.open = True
            self.page.update()
        else:
            empleado = Empleado(codigo, nombre, float(horas), float(valor), float(porcentaje))
            salario_bruto = f"$ {round(empleado.calcular_salario_bruto(), 0):,.0f}".replace(",", ".")
            salario_neto = f"$ {round(empleado.calcular_salario_neto(), 0):,.0f}".replace(",", ".")

            nueva_fila = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(value=codigo, color=ft.Colors.BLACK)),
                    ft.DataCell(ft.Text(value=nombre, color=ft.Colors.BLACK)),
                    ft.DataCell(ft.Text(value=salario_bruto, color=ft.Colors.BLACK)),
                    ft.DataCell(ft.Text(value=salario_neto, color=ft.Colors.BLACK))
                ]
            )
            self.info_tabla.rows.append(nueva_fila)

            self.page.update()
        return e

    def limpiar_campos(self, e):
        self.codigo_entrada.value = ""
        self.nombre_entrada.value = ""
        self.horas_mes_entrada.value = ""
        self.valor_hora_entrada.value = ""
        self.rete_fuente_entrada.value = ""
        self.info_tabla.rows = []
        self.page.update()
        return e


def main(page: ft.Page):
    EmpleadoApp(page)

ft.app(target=main)
