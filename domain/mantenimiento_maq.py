class MantenimientoDomain:
    def __init__(self,
        data:DataMaquinaria,
        tarifa_mantenimiento:float,
        mano_obra_percent:float,
        repuestos_percent:float,
    ):
        self.MY_MAQUINA = data
        self.tarifa_mantenimiento:float = tarifa_mantenimiento
        self.mano_obra_percent:float = mano_obra_percent
        self.repuestos_percent:float = repuestos_percent

    def calc_tarifa_mantenimiento(self): 
        return (
            self.MY_MAQUINA.valor_adquisicion * 
            self.tarifa_mantenimiento
        )

    def calc_tarifa_mano_obra(self): 
        return self.calc_tarifa_mantenimiento() * self.mano_obra_percent
    def calc_tarifa_repuesto(self): 
        return self.calc_tarifa_mantenimiento() * self.repuestos_percent
    
    def calc_mo_hora(self): 
        return (
            self.calc_tarifa_mano_obra() / 
            self.MY_MAQUINA.horas_operativas_anual
        )
    def calc_rep_hora(self): 
        return (
            self.calc_tarifa_repuesto() / 
            self.MY_MAQUINA.horas_operativas_anual
        )
    def calc_mantenimiento_hora(self): 
        return self.calc_mo_hora() + self.calc_rep_hora()
    
