# Ejercicio propuesto No 24 del Capítulo 4. Libro de Lógica de Programación de Efrain Oviedo.

class Esfera:
    
    def __init__(self, pesoA: float, pesoB: float, pesoC: float) -> None:
        self.pesoA = pesoA
        self.pesoB = pesoB
        self.pesoC = pesoC
        
    def esfera_mayor_peso(self) -> str:
        """
        A partir de los pesos de tres esferas diferentes, se determinará cuál tiene mayor peso.
        """
        if self.pesoA > self.pesoB and self.pesoA > self.pesoC:
            return f"La esfera A tiene mayor peso ({self.pesoA})"
        elif self.pesoB > self.pesoC:
            return f"La esfera B tiene mayor peso ({self.pesoB})"
        else:
            return f"La esfera C tiene mayor peso ({self.pesoC})"
    
def main() -> None:
    # Solicitud de pesos
    esferaA = float(input("Ingrese el peso de la esfera A: "))
    esferaB = float(input("Ingrese el peso de la esfera B: "))
    esferaC = float(input("Ingrese el peso de la esfera C: "))
    
    # Creación de objeto
    esfera = Esfera(pesoA=esferaA, pesoB=esferaB, pesoC=esferaC)
    
    # Mostrar información
    print(esfera.esfera_mayor_peso())


if __name__ == "__main__":
    main()
