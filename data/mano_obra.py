class ManoObra:
    RMV: float = 1130.0
    VACACIONES: int = 30
    DIAS_CALENDARIO: int = 360

    def __init__(self, 
                 sueldo: float, 
                 horas_trabajo: float, 
                 dias_descanso: float, 
                 hijos: int, 
                 lista: dict):
        self.sueldo_bruto = sueldo
        self.dias_descanso = dias_descanso
        self.hijos = hijos
        self.lista = lista
        self.horas_trabajo = horas_trabajo
        self.gratificacion = 0.0
        self.cts = 0.0
        self.dias_efectivos = 0.0
        self.cmho:float = 0.0

    def get_asignacion_familiar(self) -> float:
        return self.RMV * 0.1 if self.hijos > 0 else 0.0

    def calc_bonos_productividad(self) -> float:
        if len(self.lista) == 0:
            return 0.0

        suma = sum(self.lista.values())
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
    
    def get_horas_efectivas_año(self):
        return self.dias_efectivos * self.horas_trabajo

    def get_afp(self):
        prima:float = 0.0137 * self.sueldo_bruto
        comision:float = 0.0169 * self.sueldo_bruto
        aporte:float = 0.10 * self.sueldo_bruto
        return prima + comision + aporte
    
    def get_essalud(self): return
    
    def get_ls(self):


    def get_CMHO(self):
        if self.cmho != 0: return self.cmho
        self.cmho = (self.sueldo_bruto * 12)/self.get_horas_efectivas_año()
        
        self.cmho = self.cmho * (1 + )

        return self.cmho

