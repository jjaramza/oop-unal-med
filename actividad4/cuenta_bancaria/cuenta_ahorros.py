from cuenta import Cuenta

class CuentaAhorros(Cuenta):
    """
    Esta clase denominada CuentaAhorros modela una cuenta de ahorros
    que es una subclase de Cuenta. Tiene un nuevo atributo: activa.
    
    Attributes:
        __activa (bool): Identifica si una cuenta está activa. Lo está si su saldo es superior a 10000.
    """
    def __init__(self, saldo: float, tasa_anual: float) -> None:
        """
        Constructor de la clase CuentaAhorros.
        
        Args:
            _saldo (float): Saldo de la cuenta de ahorros.
            _tasa_anual (float): Tasa anual de interés de la cuenta de ahorros.
        """
        # Invoca al constructor de la clase padre
        super().__init__(saldo, tasa_anual)
        # Si el saldo es menor a 10000, la cuenta no se activa
        self.__activa: bool
        if self._saldo < 10000:
            self.__activa = False
        else:
            self.__activa = True
    
    def retirar(self, cantidad: float) -> None:
        """
        Método que recibe una cantidad de dinero a retirar y actualiza el
        saldo de la cuenta.
        
        Args:
            cantidad (float): Cantidad a retirar de una cuenta de ahorros.
        """
        # Si la cuenta está activa, se puede retirar dinero
        if self.__activa:
            # Invoca al método retirar de la clase padre
            super().retirar(cantidad)
            
    def consignar(self, cantidad: float) -> None:
        """
        Método que recibe una cantidad de dinero a consignar y actualiza 
        el saldo de la cuenta.
        
        Args:
            cantidad (float): Cantidad a consignar en una cuenta de ahorros.
        """
        # Si la cuenta está activa, se puede consignar dinero
        if self.__activa:
            # Invoca al método consignar de la clase padre
            super().consignar(cantidad)
            
    def extracto_mensual(self) -> None:
        """
        Método que genera un extracto mensual de una cuenta de ahorros
        """
        # Si la cantidad de retiros es superior a cuatro, se genera una comisión mensual
        if self._numero_retiros > 4:
            self._comision_mensual += (self._numero_retiros - 4) * 1000
        
        super().extracto_mensual() # Invoca el método de la clase padre
        
        # Si el saldo actualizado de la cuenta es menor a 10000, la cuenta no se activa
        if self._saldo < 10000:
            self.__activa = False
            
    def imprimir(self) -> None:
        """
        Método que muestra en pantalla los datos de una cuenta de ahorros
        """
        print(f"\nSaldo = $ {self._saldo:.2f}")
        print(f"Comisión mensual = $ {self._comision_mensual:.2f}")
        print(f"Número de transacciones = {self._numero_consignaciones + self._numero_retiros}\n")
