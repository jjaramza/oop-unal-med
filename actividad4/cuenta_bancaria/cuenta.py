class Cuenta:
    """
    Esta clase denominada Cuenta modela una cuenta bancaria con los
    atributos saldo, número de consignaciones, número de retiros, tasa
    anual de interés y comisión mensual.
    
    Attributes:
        _saldo (float): Saldo de una cuenta bancaria.
        _numero_consignaciones (int): Número de consignaciones realizadas en una cuenta bancaria.
        _numero_retiros (int): Número de retiros de una cuenta bancaria.
        _tasa_anual (float): Tasa anual de intereses de una cuenta bancaria.
        _comision_mensual (float): Comisión mensual que se cobra a una cuenta bancaria.
    """
    def __init__(self, saldo: float, tasa_anual: float) -> None:
        """
        Constructor de la clase Cuenta.
        
        Args:
            _saldo (float): Saldo de una cuenta bancaria.
            _tasa_anual (float): Tasa anual de intereses de una cuenta bancaria.
        """
        self._saldo: float = saldo
        self._tasa_anual: float = tasa_anual
        self._numero_consignaciones: int = 0
        self._numero_retiros: int = 0
        self._comision_mensual: float = 0
        
    def consignar(self, cantidad: float) -> None:
        """
        Método que recibe una cantidad de dinero a consignar y actualiza 
        el saldo de la cuenta.
        
        Args:
            cantidad (float): Cantidad de dinero a consignar en la cuenta.
        """
        # Se actualiza el saldo con la cantidad consignada
        self._saldo += cantidad
        
        # Se actualizada el número de consignaciones realizadas en la cuenta
        self._numero_consignaciones += 1
        
    def retirar(self, cantidad: float) -> None:
        """
        Método que recibe una cantidad de dinero a retirar y actualiza el
        saldo de la cuenta.
        
        Args:
            cantidad (float): Cantidad de dinero a retirar de la cuenta.
        """
        nuevo_saldo: float = self._saldo - cantidad
        
        # Si la cantidad a retirar no supera el saldo, el retiro no se puede realizar
        if nuevo_saldo >= 0:
            self._saldo -= cantidad
            self._numero_retiros += 1
        else:
            print("\nLa cantidad a retirar excede el salado actual.\n")
            
    def calcular_interes(self) -> None:
        """
        Método que calcula interés mensual de la cuenta a partir de la tasa
        anual aplicada.
        """
        # Convierte la tasa anual en mensual
        tasa_mensual: float = self._tasa_anual / 12
        interes_mensual: float = self._saldo * tasa_mensual
        
        # Actualiza el saldo aplicando el interés mensual
        self._saldo += interes_mensual
        
    def extracto_mensual(self) -> None:
        """
        Método que genera un extracto aplicando al saldo actual una
        comisión y calculando sus intereses
        """
        self._saldo -= self._comision_mensual
        self.calcular_interes()
