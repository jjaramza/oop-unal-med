class Empleado:
    """
    Esta clase define objetos de tipo Empleado la cual tiene varios atributos como
    código del empleado, nombres, número de horas trabajadas al mes, valor hora trabajada
    y porcentaje de retención en la fuente.
    """
    def __init__(self, codigo: str, nombre: str, horas_mes: float, valor_hora: float, porcentaje_rete_fuente: float) -> None:
        """
        Constructor de la clase Empleado.

        Args:
            codigo (str): Parámetro que define el código del empleado
            nombre (str): Parámetro que define el nombre del empleado
            horas_mes (float): Parámetro que define el número de horas trabajadas al mes
            valor_hora (float): Parámetro que define el valor hora trabajada
            porcentaje_rete_fuente (float): Parámetro que define el porcentaje de retención en la fuente
        """
        self.codigo = codigo
        self.nombre = nombre
        self.horas_mes = horas_mes
        self.valor_hora = valor_hora
        self.porcentaje_rete_fuente = porcentaje_rete_fuente

    def calcular_salario_bruto(self) -> float:
        """
        Calcula y devuelve el salario bruto de un empleado.

        Returns:
            float: Salario bruto calculado como la multiplicación entre el valor de la hora y las horas trabajadas al mes
        """
        return self.valor_hora * self.horas_mes

    def calcular_salario_neto(self) -> float:
        """
        Calcula y devuelve el salario neto de un empleado.
        Returns:
            float: Salario neto que se calcula restándole el valor de la retención en la fuente al salario bruto
        """
        salario_bruto = self.calcular_salario_bruto()
        return salario_bruto * (1 - self.porcentaje_rete_fuente / 100)
