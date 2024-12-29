class SalarioMensual:
    """
    La clase SalarioMensual permite calcular el salario mensual de un empleado,
    y en función de lo que gana se mostrará su nombre y el salario.
    
    Attributes:
        nombre_empleado (str): Nombre del empleado
        salario_hora (float): Salario básico por hora
        horas_mes (float): Horas trabajadas en el mes
    """
    def __init__(self, nombre_empleado: str, salario_hora: float, horas_mes: float) -> None:
        self.nombre_empleado = nombre_empleado
        self.salario_hora = salario_hora
        self.horas_mes = horas_mes
        
    def calcular_salario(self) -> float:
        """
        Calcular el salario mensual con base en las horas trabajadas.
        
        Returns:
            float: Salario mensual
        """
        return self.salario_hora * self.horas_mes
    
    def mostrar_info_empleado(self) -> str:
        """
        Muestra la información del empleado como el nombre y el salario,
        este último solo se visualiza si es mayor a $450.000.
        
        Returns:
            str: Nombre de empleado + salario mensual
        """
        salario_mes = self.calcular_salario()
        
        if salario_mes > 450000:
            salario_str = "{:,.0f}".format(salario_mes).replace(",", ".")
            return f"Nombre empleado: {self.nombre_empleado}\nSalario mensual: ${salario_str}"
        else:
            return f"Nombre empleado: {self.nombre_empleado}"
