class Liquidacion:
    """
    Esta clase define objetos de tipo Liquidación, la cuál tiene
    como principal objetivo obtener la liquidación de matrícula
    de un estudiante con base en unos parámetros.
    
    Attributes:
        numero_inscripcion (str): Número de inscripción del estudiante
        nombre_estudiante (str): Nombre completo del estudiante
        patrimonio (float): Patrimonio del estudiante
        estrato_social (int): Estrato social del estudiante
    """
    def __init__(self,
                 numero_inscripcion: str,
                 nombre_estudiante: str,
                 patrimonio: int,
                 estrato_social: int) -> None:
        self.numero_inscripcion = numero_inscripcion
        self.nombre_estudiante = nombre_estudiante
        self.patrimonio = patrimonio
        self.estrato_social = estrato_social
        
    def valor_matricula(self) -> int:
        """
        Se calcula el valor de la matrícula con base
        en el patrimonio y el estrato social del estudiante.
        
        Returns:
            float: El valor del pago de la matrícula
        """
        valor_matricula = 50000
        if (self.patrimonio > 2000000) and (self.estrato_social > 3):
            valor_matricula += self.patrimonio * 0.03
        return int(round(valor_matricula, 0))
        