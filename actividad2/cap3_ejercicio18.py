# Ejercicio propuesto No 18 del Capítulo 3. Libro de Lógica de Programación de Efrain Oviedo.

class Empleado:
    
    VALOR_HORA = 10000 # Constante de clase: valor hora trabajada.
    RETE_FUENTE = 10 # Constante de clase: porcentaje de retención en la fuente.
    
    def __init__ (self, codigo_empleado: str, nombre_empleado: str, horas_trabajadas_mes: float) -> None:
        self.codigo_empleado = codigo_empleado
        self.nombre_empleado = nombre_empleado
        self.horas_trabajadas_mes = horas_trabajadas_mes
        
    def calcular_salario_bruto(self) -> float:
        """Calcula el salario bruto con base en el valor hora y las horas trabajadas."""
        return self.horas_trabajadas_mes * self.VALOR_HORA
    
    def calcular_salario_neto(self) -> float:
        """
        Calcula el salario neto con base en el salario bruto
        y el porcentaje de retención en la fuente.
        """
        salario_bruto = self.calcular_salario_bruto()
        return salario_bruto * (1 - self.RETE_FUENTE / 100)


def main() -> None:
    """
    Solicitar los datos de un empleado al usuario.
    """
    codigo = input("Ingrese el código del empleado: ")
    nombre = input("Ingrese el nombre completo del empleado: ")
    horas = float(input("Ingrese las horas trabajadas al mes: "))

    empleado = Empleado(codigo_empleado=codigo, nombre_empleado=nombre, horas_trabajadas_mes=horas)
    
    print(
        f"Empleado: {empleado.codigo_empleado} - {empleado.nombre_empleado.upper()}\n"
        f"Salario bruto: {empleado.calcular_salario_bruto():,.2f}\n"
        f"Salario neto: {empleado.calcular_salario_neto():,.2f}"
    )


if __name__ == "__main__":
    main()
