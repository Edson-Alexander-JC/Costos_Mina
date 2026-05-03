class DataMantenimiento:
    def __init__(self,
        tarifa_mantenimiento:float,
        mano_obra_percent:float,
        repuestos_percent:float,
    ):
        self.tarifa_mantenimiento:float = tarifa_mantenimiento
        self.mano_obra_percent:float = mano_obra_percent
        self.repuestos_percent:float = repuestos_percent