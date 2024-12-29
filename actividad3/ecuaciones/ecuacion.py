from math import sqrt

class EcuacionGrado2:
    """
    La clase EcuacionGrado2 permite obtener las posibles soluciones
    de una ecuación de segundo grado Ax² + Bx + C,
    considerando soluciones reales y complejas.
    
    Attributes:
        numA (float): El coeficiente cuadrático (A ≠ 0)
        numB (float): El coeficiente lineal
        numC (float): El término independiente
    """
    def __init__(self, numA: float, numB: float, numC: float) -> None:
        self.numA = numA
        self.numB = numB
        self.numC = numC
        
    @property
    def determinante(self) -> float:
        """
        Calcular el determinante de una ecuación de segundo grado.
        
        Returns:
            float: El determinante de la ecuación de segundo grado.
        """
        return self.numB ** 2 - 4 * self.numA * self.numC
    
    def soluciones_ecuacion(self) -> list[float | complex]:
        """
        Encontrar las posibilidades soluciones de una ecuación de segundo grado.
        
        Returns:
            list[float | complex]: Una lista con las soluciones reales o complejas.
        """
        determinante = self.determinante
        if determinante >= 0:
            x1 = (-self.numB + sqrt(determinante)) / (2 * self.numA)
            x2 = (-self.numB - sqrt(determinante)) / (2 * self.numA)
        else:
            parte_real = -self.numB / (2 * self.numA)
            parte_imaginaria = sqrt(-determinante) / (2 * self.numA)
            x1 = complex(parte_real, parte_imaginaria)
            x2 = complex(parte_real, -parte_imaginaria)
        return [x1, x2]
    
    def mostrar_soluciones(self) -> str:
        """
        Muestra las soluciones de la ecuación.
        
        Returns:
            str: Texto con las soluciones de la ecuación de segundo grado
        """
        soluciones = self.soluciones_ecuacion()
        
        if self.determinante >= 0:
            return f"Soluciones reales:\n\n{soluciones[0]:.2f} y {soluciones[1]:.2f}"
        else:
            return (
                f"Soluciones complejas:\n\n"
                f"({soluciones[0].real:.2f} + {soluciones[0].imag:.2f}i) y "
                f"({soluciones[1].real:.2f} - {abs(soluciones[1].imag):.2f}i)"
            )
