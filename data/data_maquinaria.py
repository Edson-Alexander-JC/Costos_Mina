class DataMaquinaria:
    #responsabilidad: brindarme los datos para calcular costos variables y fijos
    def __init__(self,
        valor_adquisicion:float,
        vida_economica_util:float,
        valor_residual:float,
        combustible_percent:float,
        lubricante_percent:float,
        potencia_KW:float,
        capacidad:float,
        interes:float,
        disponibilidad_mec:float,
        seguro:float,# 0.75% al 1.5% o  2% al 4%
        horas_operativas_anual:int
    ):
        self.valor_adquisicion:float = valor_adquisicion
        self.vida_economica_util:float = vida_economica_util
        self.valor_residual:float = valor_residual
        self.combustible_percent:float = combustible_percent
        self.lubricante_percent:float = lubricante_percent
        self.potencia_KW:float = potencia_KW
        self.capacidad:float = capacidad
        self.interes:float = interes
        self.disponibilidad_mec:float = disponibilidad_mec
        self.seguro:float = seguro
        self.horas_operativas_anual:float = horas_operativas_anual