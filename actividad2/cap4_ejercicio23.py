# Ejercicio propuesto No 23 del Capítulo 4. Libro de Lógica de Programación de Efrain Oviedo.

from math import sqrt

class EcuacionGrado2:
    
    def __init__(self, numA: float, numB: float, numC: float) -> None:
        self.numA = numA
        self.numB = numB
        self.numC = numC
        
    def calcular_determinante(self) -> float:
        """Calcular el determinante de una ecuación de segundo grado."""
        return self.numB ** 2 - 4 * self.numA * self.numC
    
    def soluciones_ecuacion(self) -> list[complex]:
        """Encontrar las posibilidades soluciones de una ecuación de segundo grado."""
        determinante = self.calcular_determinante()
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
        """Muestra las soluciones de la ecuación."""
        determinante = self.calcular_determinante()
        soluciones = self.soluciones_ecuacion()
        
        if determinante >= 0:
            return f"Las posibles soluciones son: {soluciones[0]:.2f} y {soluciones[1]:.2f}"
        else:
            return (
                f"Las posibles soluciones son: "
                f"({soluciones[0].real:.2f} + {soluciones[0].imag:.2f}j) y "
                f"({soluciones[1].real:.2f} - {abs(soluciones[1].imag):.2f}j)"
            )
        

def main() -> None:
    # Solicitud de números
    a = float(input("Ingrese el primer coeficiente: "))
    b = float(input("Ingrese el segundo coeficiente: "))
    c = float(input("Ingrese el tercer coeficiente: "))
    
    # Creación del objeto
    sol_ecuacion = EcuacionGrado2(numA=a, numB=b, numC=c)
    
    # Mostrar las soluciones
    print(sol_ecuacion.mostrar_soluciones())
    

if __name__ == "__main__":
    main()
