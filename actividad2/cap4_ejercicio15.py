# Ejercicio resuelto No 15 del Capítulo 4. Libro de Lógica de Programación de Efrain Oviedo.

class Esfera:
    
    def __init__(self, pesoA: float, pesoB: float, pesoC: float, pesoD: float) -> None:
        self.pesoA = pesoA
        self.pesoB = pesoB
        self.pesoC = pesoC
        self.pesoD = pesoD
        
    def determinar_esfera_diferente(self) -> str:
        """
        A partir de los pesos de cuatro esferas, donde tres de ellas tienen igual peso,
        se determinará cuál es la diferente (ya sea si tiene mayor o menor peso).
        """
        mensaje: str
        if self.pesoA == self.pesoB and self.pesoA == self.pesoC:
            if self.pesoD > self.pesoA:
                mensaje = "La esfera D es la diferente y es de mayor peso."
            else:
                mensaje = "La esfera D es la diferente y es de menor peso."
        elif self.pesoA == self.pesoB and self.pesoA == self.pesoD:
            if self.pesoC > self.pesoA:
                mensaje = "La esfera C es la diferente y es de mayor peso."
            else:
                mensaje = "La esfera C es la diferente y es de menor peso."
        elif self.pesoA == self.pesoC and self.pesoA == self.pesoD:
            if self.pesoB > self.pesoA:
                mensaje = "La esfera B es la diferente y es de mayor peso."
            else:
                mensaje = "La esfera B es la diferente y es de menor peso."
        else:
            if self.pesoA > self.pesoB:
                mensaje = "La esfera A es la diferente y es de mayor peso."
            else:
                mensaje = "La esfera A es la diferente y es de menor peso."
        return mensaje
    
    
def main() -> None:
    # Solicitud de pesos
    esferaA = float(input("Ingrese el peso de la esfera A: "))
    esferaB = float(input("Ingrese el peso de la esfera B: "))
    esferaC = float(input("Ingrese el peso de la esfera C: "))
    esferaD = float(input("Ingrese el peso de la esfera D: "))
    
    # Creación de objeto
    esfera = Esfera(pesoA=esferaA, pesoB=esferaB, pesoC=esferaC, pesoD=esferaD)
    
    # Mostrar información
    print(esfera.determinar_esfera_diferente())


if __name__ == "__main__":
    main()
