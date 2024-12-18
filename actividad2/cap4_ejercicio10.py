# Ejercicio resuelto No 10 del Capítulo 4. Libro de Lógica de Programación de Efrain Oviedo.

class Liquidacion:
    
    def __init__(self,
                 numero_inscripcion: str,
                 nombre_estudiante: str,
                 patrimonio: float,
                 estrato_social: int) -> None:
        self.numero_inscripcion = numero_inscripcion
        self.nombre_estudiante = nombre_estudiante
        self.patrimonio = patrimonio
        self.estrato_social = estrato_social
        
    def valor_matricula(self) -> float:
        """
        Se calcula el valor de la matrícula con base
        en el patrimonio y el estrato social del estudiante.
        """
        valor_matricula = 50000
        if (self.patrimonio > 2000000) and (self.estrato_social > 3):
            valor_matricula += self.patrimonio * 0.03
        return valor_matricula
    
    def mostrar_liquidacion(self) -> str:
        """Muestra la liquidación de matrícula del estudiante."""
        valor_matricula = self.valor_matricula()
        return (f"El estudiante con número de inscripción {self.numero_inscripcion} "
                f"y nombre {self.nombre_estudiante.upper()} "
                f"debe pagar ${('{:,.0f}'.format(valor_matricula)).replace(',', '.')}")
        
        
def main() -> None:
    # Solicitud de datos al usuario
    inscripcion = input("Ingrese el número de inscripción: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    patrimonio = float(input("Ingrese el patrimonio del estudiante: "))
    estrato = int(input("Ingrese el estrato social del estudiante: "))
    
    # Se crea un objeto de tipo Liquidacion
    estudiante = Liquidacion(numero_inscripcion=inscripcion,
                             nombre_estudiante=nombre,
                             patrimonio=patrimonio,
                             estrato_social=estrato)
    
    print(estudiante.mostrar_liquidacion())
    
    
if __name__ == "__main__":
    main()
