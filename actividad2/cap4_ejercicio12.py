# Ejercicio resuelto No 12 del Capítulo 4. Libro de Lógica de Programación de Efrain Oviedo.

class Salario:
    
    def __init__(self,
                 nombre_trabajador: str,
                 horas_trabajadas: float,
                 valor_hora_trabajo: float) -> None:
        self.nombre = nombre_trabajador
        self.horas = horas_trabajadas
        self.valor_hora = valor_hora_trabajo
        
    def calculo_salario(self) -> float:
        """Se calcula el salario con base en las horas normales y extras."""
        hora_extra: int
        hora_ext_exc: int
        salario: float
        if self.horas > 40:
            hora_extra = self.horas - 40
            if hora_extra > 8:
                hora_ext_exc = hora_extra - 8
                salario = 40 * self.valor_hora + 16 * self.valor_hora + hora_ext_exc * 3 * self.valor_hora
            else:
                salario = 40 * self.valor_hora + hora_extra * 2 * self.valor_hora
        else:
            salario = self.horas * self.valor_hora
        return salario
    
    def mostrar_liquidacion(self) -> str:
        """Muestra el salario devengado de un trabajador."""
        salario = f"{'{:,.0f}'.format(self.calculo_salario())}"
        return f"El trabajador {self.nombre.upper()} devengó: ${salario.replace(",", ".")}"
    
    
def main() -> None:
    # Solicitud de datos
    nombre = input("Ingrese el nombre del trabajador: ")
    horas = float(input("Ingrese el número de horas trabajadas en la semana: "))
    valor_hora = float(input("Ingrese el valor de la hora trabajada: "))
    
    # Se crea el objeto de tipo Salario
    salario = Salario(nombre_trabajador=nombre,
                      horas_trabajadas=horas,
                      valor_hora_trabajo=valor_hora)
    
    # Se muestra la información
    print(salario.mostrar_liquidacion())
    

if __name__ == "__main__":
    main()
