# Ejercicio propuesto No 21 del Capítulo 3. Libro de Lógica de Programación de Efrain Oviedo.

from math import sqrt

class Triangulo:
    
    def __init__(self, lado_a: float, lado_b: float, lado_c: float) -> None:
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c
        
    def perimetro_triangulo(self) -> float:
        """Calcula el perímetro de un triángulo a partir de sus tres lados."""
        return self.lado_a + self.lado_b + self.lado_c
    
    def semiperimetro_triangulo(self) -> float:
        """Calcula el semiperímetro de un triángulo."""
        perimetro = self.perimetro_triangulo()
        return perimetro / 2
    
    def area_triangulo(self) -> float:
        """Calcula el área de un triángulo a partir de su semiperímetro y sus lados."""
        s = self.semiperimetro_triangulo()
        return sqrt(s * (s - self.lado_a) * (s - self.lado_b) * (s - self.lado_c))


def main() -> None:
    """
    Solicita los lados de un triángulo al usuario y muestra en pantalla el perímetro, 
    el semiperímetro y el área de un triángulo.
    """
    a = float(input("Ingrese el primer lado de un triángulo: "))
    b = float(input("Ingrese el segundo lado de un triángulo: "))
    c = float(input("Ingrese el tercer lado de un triángulo: "))

    # Se crea el objeto de tipo Triangulo
    trianqulo = Triangulo(a, b, c)

    # Se muestra en pantalla 
    print(f"Perímetro: {trianqulo.perimetro_triangulo():,.2f}")
    print(f"Semiperímetro: {trianqulo.semiperimetro_triangulo():,.2f}")
    print(f"Área: {trianqulo.area_triangulo():,.2f}")


if __name__ == "__main__":
    main()
