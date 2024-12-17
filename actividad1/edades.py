# Ejercicio resuelto No 4 del libro de Lógica de Programación de Efrain Oviedo

class Edades:
    """
    A partir de la edad de Juan se calcula la edad de Alberto y Ana.
    Y la edad de la mamá se calcula a partir de los tres hermanos.
    """
    def __init__(self, edad_juan: int):
        """
        Inicializar la edad de Juan.
        """
        self.edad_juan = edad_juan
        
    def calcular_edades(self, edad_juan: int) -> list:
        """
        Calcular las edades de Alberto, Ana y Mama con base en la edad de Juan.
        """
        edad_alberto = (2 * edad_juan) // 3
        edad_ana = (4 * edad_juan) // 3
        edad_mama = edad_juan + edad_alberto + edad_ana
        return [edad_alberto, edad_ana, edad_juan, edad_mama]
        
    def mostrar_edades(self):
        """
        Muestra las edades de Alberto, Ana, Juan y Mamá con un formato específico.
        """
        edades = self.calcular_edades(self.edad_juan)
        
        print("\nLas edades son:")
        for idx, nombre in enumerate(["Alberto", "Ana", "Juan", "Mamá"]):
            print(f"{nombre}: {edades[idx]}")
    

if __name__ == "__main__":
    # Solicita la edad de Juan al usuario
    edad_juan = int(input("Ingrese la edad de Juan: "))
    
    # Crea una instancia de la clase Edades
    salida_edades = Edades(edad_juan)
    
    # Muestra las edades
    salida_edades.mostrar_edades()
