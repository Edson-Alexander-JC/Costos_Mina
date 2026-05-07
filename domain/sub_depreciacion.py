import streamlit as st
from interfaces.tab import Tab
from domain.maquinaria_domain import MaquinariaDomain

class SubDepreciacion(Tab):

    def __init__(self):
        self.valor_residual:float = 0
        self.my_maquinaria = None

    def set_data(self,data:MaquinariaDomain):
        self.my_maquinaria = data

    def render(self):
        self.valor_residual = self.set_input("float","Valor residual: ",self.valor_residual)
        if(st.button("Calcular Deprecicacion")):
           self.render_depreciacion()

    def render_depreciacion(self):
        depreciacion:float = (
                (self.my_maquinaria.valor_adquisicion - 
                self.valor_residual) / 
                self.my_maquinaria.vida_economica_util
             ) * -1
        self.set_output("float","Deprecicacion: ",depreciacion,"$")
        self.my_maquinaria.set_depreciacion(depreciacion)
        st.write(depreciacion)