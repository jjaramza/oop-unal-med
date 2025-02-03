from math import sqrt

class Notas:
    """
    Esta clase denominada Notas define una lista de notas numéricas de tipo float.
    """
    def __init__(self):
        """
        Constructor de la clase Notas, instancia una lista de notas de tipo float.
        """
        self.lista_notas: list[float] = []
        
    def calcular_promedio(self) -> float:
        """
        Método que calcula el promedio de notas.
        
        Returns:
            float: El promedio de notas calculado.
        """
        if not self.lista_notas:
            return 0.0
        return sum(self.lista_notas) / len(self.lista_notas)
    
    def calcular_desviacion(self) -> float:
        """
        Método que calcula la desviación estándar de la lista de notas.
        
        Returns:
            float: La desviación estándar de la lista de notas.
        """
        if len(self.lista_notas) < 2:
            return 0.0
        promedio = self.calcular_promedio()
        varianza = sum((x - promedio) ** 2 for x in self.lista_notas) / len(self.lista_notas)
        return sqrt(varianza)
    
    def calcular_menor(self) -> float:
        """
        Método que calcula el valor menor de la lista de notas.
        
        Returns:
            float: El valor menor de la lista de notas.
        """
        if not self.lista_notas:
            return 0.0
        return min(self.lista_notas)
    
    def calcular_mayor(self) -> float:
        """
        Método que calcula el valor mayor de la lista de notas.
        
        Returns:
            float: El valor mayor de la lista de notas.
        """
        if not self.lista_notas:
            return 0.0
        return max(self.lista_notas)
