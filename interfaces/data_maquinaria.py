class DataMaquinaria:
    #responsabilidad: brindarme los datos para calcular costos variables y fijos
    def __init__(self,
        kind_of_maq:str,
        valor_adquisicion:float,
        vida_economica_util:float,
        combustible_percent:float,
        lubricante_percent:float,
        potencia_KW:float,
        capacidad:float,
        interes:float,
        disponibilidad_mec:float,
        seguro:float,# 0.75% al 1.5% o  2% al 4%
        horas_operativas_anual:int,
        importado:bool
    ):
        self.kind_of_maquinaria:str = kind_of_maq
        self.valor_adquisicion:float = valor_adquisicion
        self.vida_economica_util:float = vida_economica_util
        self.combustible_percent:float = combustible_percent
        self.lubricante_percent:float = lubricante_percent
        self.potencia_KW:float = potencia_KW
        self.capacidad:float = capacidad
        self.interes:float = interes
        self.disponibilidad_mec:float = disponibilidad_mec
        self.seguro:float = seguro
        self.horas_operativas_anual:float = horas_operativas_anual
        self.importado:bool = importado