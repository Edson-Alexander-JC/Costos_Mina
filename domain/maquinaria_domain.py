from interfaces.data_maquinaria import DataMaquinaria
class MaquinariaDomain:
    #Responsabilidad; procesar los datos de DataMaquinaria
    def __init__(self,data:DataMaquinaria):
        self.MY_MAQUINA = data
        self.depreciacion:float = 0.0

        self.COSTOS_COMBUSTIBLE = 0.0
        self.COSTOS_LUBRICANTE = 0.0
        self.COSTOS_NEUMATICO = 0.0
        self.COSTOS_MANTENIMIENTO = 0.0
        self.COSTOS_MANO_OBRA = 0.0
        self.COSTOS_PIEZAS_DESGASTE = {}

    def calc_igv(self) -> float: 
        return self.MY_MAQUINA.valor_adquisicion * 0.18
    def calc_importacion_taxes(self) -> float: 
        if(self.MY_MAQUINA.importado == False): return 0.0
        return self.MY_MAQUINA.valor_adquisicion * 0.035
    def calc_inversion_media_anual(self):
        return (
            self.MY_MAQUINA.valor_adquisicion + 
            self.MY_MAQUINA.valor_residual) / 2
    def calc_costos_insumos(self,porcentaje:float,precio:float):
            return porcentaje * precio    
# costos de posecion
    def set_depreciacion(self,depreciacion): self.depreciacion = depreciacion
        
    def calc_interes(self):
        return (
            self.calc_inversion_media_anual() * 
            self.MY_MAQUINA.interes
        )
    def calc_impuestos(self):
        return (
            self.calc_igv() + 
            self.calc_importacion_taxes()
        )
    def calc_seguro(self):
        return (
            self.MY_MAQUINA.valor_adquisicion * 
            self.MY_MAQUINA.seguro
        )
#
    def calc_costos_posecion(self):
        return (
            self.depreciacion+
            self.calc_interes()+
            self.calc_impuestos()+
            self.calc_seguro()
        ) / self.MY_MAQUINA.horas_operativas_anual
# costos de operacion
    def set_costos_combustible(self,precio:float):
        self.COSTOS_COMBUSTIBLE = (
            self.calc_costos_insumos(self.MY_MAQUINA.combustible_percent,precio)
        )
    def set_costos_lubricante(self,precio:float):
        self.COSTOS_LUBRICANTE = (
            self.calc_costos_insumos(self.MY_MAQUINA.lubricante_percent,precio)
        )
    def calc_costos_filtros(self):
        return (
            0.02 * 
            (
                self.COSTOS_COMBUSTIBLE + 
                self.COSTOS_LUBRICANTE
            )
        )
    def set_costos_neumaticos(self,precio,vida_util): 
        self.COSTOS_NEUMATICO = precio/vida_util
    def set_costos_piezas_desgaste(self,
        nombre:str,precio:float,cantidad:int,vida_util:int):
        self.COSTOS_PIEZAS_DESGASTE[nombre] = (precio * cantidad) / vida_util
    def set_mantenimiento(self,costo:float):
        self.COSTOS_MANTENIMIENTO = costo
    def suma_costos_piezas(self):
        return sum(self.COSTOS_PIEZAS_DESGASTE.values())
#       
    def calc_horario_operacion(self):
        return (
            self.COSTOS_COMBUSTIBLE +
            self.COSTOS_LUBRICANTE +
            self.calc_costos_filtros()+
            self.COSTOS_NEUMATICO +
            self.suma_costos_piezas()+
            self.COSTOS_MANTENIMIENTO
        )
# costos del operador
    def set_costos_mano_obra(self,costo:float):
        self.COSTOS_MANO_OBRA = costo
#
