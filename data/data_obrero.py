class DataObrero:
    #responsabilidad: brindarme los datos para calcular costos variables y fijos
    def __init__(self,
        sueldo: float, 
        horas_trabajo: float, 
        dias_descanso: float, 
        hijos: bool, 
        bonificacion_avance_list: dict,
        eps: bool = False
    ):
        self.sueldo: float = sueldo
        self.horas_trabajo: float = horas_trabajo
        self.dias_descanso: float = dias_descanso
        self.hijos: bool = hijos
        self.bonificacion_avance_list: dict = bonificacion_avance_list
        self.eps: bool = eps
                
                
                
            