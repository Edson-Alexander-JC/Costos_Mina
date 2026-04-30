class ManoObra:
    RMV: float = 1130.0
    VACACIONES: int = 30
    DIAS_CALENDARIO: int = 360
    def __init__(self, data_obrero: DataObrero):
        self.MY_OBRERO = data_obrero

    def get_asignacion_familiar(self) -> float:
        return self.RMV * 0.1 if self.MY_OBRERO.hijos > 0 else 0.0

    def calc_bonos_productividad(self) -> float:
        if len(self.MY_OBRERO.bonificacion_avance_list) == 0:
            return 0.0

        suma = sum(
            self.MY_OBRERO.bonificacion_avance_list.values()
        )
        return suma / 6

    def get_gratificacion(self) -> float:
        if self.gratificacion != 0:
            return self.gratificacion

        self.gratificacion = (
            self.get_asignacion_familiar()
            + self.calc_bonos_productividad()
        )
        return self.gratificacion

    def get_dias_efectivos(self) -> float:
        if self.dias_efectivos != 0:
            return self.dias_efectivos

        self.dias_efectivos = (
            self.DIAS_CALENDARIO
            - self.dias_descanso
            - self.VACACIONES
        )
        return self.dias_efectivos

    def get_cts(self, meses_trabajados: int) -> float:
        if self.cts != 0:
            return self.cts

        remuneracion = (
            self.sueldo_bruto
            + self.get_asignacion_familiar()
            + (self.get_gratificacion() / 6)
        )

        self.cts = (remuneracion / 12) * meses_trabajados
        return self.cts

    def get_factor_vacaciones(self) -> float:
        return self.VACACIONES / self.get_dias_efectivos()

    def get_factor_gratificacion(self) -> float:
        return self.get_gratificacion() / self.get_dias_efectivos()
    
    def get_factor_cts(self) -> float:
        return self.cts / (self.sueldo_bruto*12)
    
    def get_horas_efectivas_año(self) -> float:
        return self.dias_efectivos * self.horas_trabajo

    def get_afp(self) -> float:
        prima:float = 0.0137 * self.sueldo_bruto
        comision:float = 0.0169 * self.sueldo_bruto
        aporte:float = 0.10 * self.sueldo_bruto
        return prima + comision + aporte
    
    def get_essalud(self) -> float:
        if(self.eps): return 0.0675 * self.sueldo_bruto
        return 0.09 * self.sueldo_bruto

    def get_eps(self) -> float: 
        if(self.eps): return 0.0225
        return 0

    #LEYES SOCIALES
    def get_ls(self): return self.get_afp + self.get_essalud + self.get_eps

    def get_CMHO(self):
        if self.cmho != 0: return self.cmho
        self.cmho = (self.sueldo_bruto * 12)/self.get_horas_efectivas_año()
        
        self.cmho = self.cmho * (1 + 
        self.get_ls() +  
        self.get_factor_cts() + 
        self.get_factor_gratificacion +
        self.get_factor_vacaciones
        )

        return self.cmho

