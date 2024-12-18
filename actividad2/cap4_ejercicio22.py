# Ejercicio propuesto No 22 del Capítulo 4. Libro de Lógica de Programación de Efrain Oviedo.

class SalarioMensual:
    
    def __init__(self, nombre_empleado: str, salario_hora: float, horas_mes: float) -> None:
        self.nombre_empleado = nombre_empleado
        self.salario_hora = salario_hora
        self.horas_mes = horas_mes
        
    def calcular_salario(self) -> float:
        """Calcular el salario mensual con base en las horas trabajadas."""
        return self.salario_hora * self.horas_mes
    
    def mostrar_info_empleado(self) -> str:
        """
        Muestra la información del empleado como el nombre y el salario,
        este último solo se visualiza si es mayor a $450.000.
        """
        salario_mes = self.calcular_salario()
        
        if salario_mes > 450000:
            salario_str = "{:,.0f}".format(salario_mes).replace(",", ".")
            return f"Nombre empleado: {self.nombre_empleado}\nSalario mensual: ${salario_str}"
        else:
            return f"Nombre empleado: {self.nombre_empleado}"
    
def main() -> None:
    # Solicitud de datos
    nombre = input("Ingrese el nombre del empleado: ")
    salario_hora = float(input("Ingrese el salario básico por hora: "))
    horas = float(input("Ingrese el número de horas trabajadas en el mes: "))
    
    # Se crea el objeto de tipo SalarioMensual
    salario = SalarioMensual(nombre_empleado=nombre, salario_hora=salario_hora, horas_mes=horas)
    
    # Mostrar información
    print(salario.mostrar_info_empleado())


if __name__ == "__main__":
    main()
