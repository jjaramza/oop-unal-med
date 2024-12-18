# Ejercicio propuesto No 19 del Capítulo 3. Libro de Lógica de Programación de Efrain Oviedo.

from math import sqrt, pow

class Equilatero:
    
    RAIZ_DE_TRES = sqrt(3) # Constante de clase: cálculo de la raíz cuadrada de 3.
    
    def __init__(self, lado: float) -> None:
        self.lado = lado
        
    def perimetro_triangulo(self) -> float:
        """Calcula el perímetro de un triángulo equilátero a partir de un lado."""
        return 3 * self.lado
    
    def altura_triangulo(self) -> float:
        """Calcula la altura de un triángulo equilátero a partir de un lado."""
        return (self.RAIZ_DE_TRES / 2) * self.lado
    
    def area_triangulo(self) -> float:
        """Calcula el área de un triángulo equilátero a partir de un lado."""
        return (self.RAIZ_DE_TRES / 4) * pow(self.lado, 2)


def main() -> None:
    """
    Solicita un lado al usuario y muestra en pantalla el perímetro, 
    la altura y el área de un triángulo equilátero.
    """
    lado = float(input("Ingrese un lado de un triángulo equilátero: "))

    # Se crea el objeto de tipo Equilatero
    equilatero = Equilatero(lado=lado)

    # Se muestra en pantalla 
    print(f"Perímetro: {equilatero.perimetro_triangulo():,.2f}")
    print(f"Altura: {equilatero.altura_triangulo():,.2f}")
    print(f"Área: {equilatero.area_triangulo():,.2f}")


if __name__ == "__main__":
    main()
