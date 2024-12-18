# Ejercicio resuelto No 11 del Capítulo 4. Libro de Lógica de Programación de Efrain Oviedo.

class NumeroMayor:
    
    def __init__(self, num1: int, num2: int, num3: int) -> None:
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        
    def numero_mayor(self) -> int:
        """Determina cuál es el número mayor de tres enteros diferentes."""
        mayor = 0
        if self.num1 > self.num2 and self.num1 > self.num3:
            mayor = self.num1
        elif self.num2 > self.num3:
            mayor = self.num2
        else:
            mayor = self.num3
        return mayor
    
    
def main() -> None:
    # Solicitud de datos
    n1 = int(input("Ingrese un número entero: "))
    n2 = int(input("Ingrese otro número entero: "))
    n3 = int(input("Ingrese otro número entero: "))
    
    # Se crea un objeto de la clase NumeroMayor
    mayor = NumeroMayor(num1=n1, num2=n2, num3=n3)
    
    # Se muestra el resultado
    print(f"El valor mayor entre {n1}, {n2}, {n3} es {mayor.numero_mayor()}")
    
    
if __name__ == "__main__":
    main()
