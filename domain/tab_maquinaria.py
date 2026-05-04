import json
import os
import streamlit as st
from interfaces.tab import Tab
from domain.maquinaria_domain import MaquinariaDomain

class TabMaquinaria(Tab):

    PATH:str = "/data/maquinaria.json"

    def __init__(self):
        self.marca = None
        self.modelo = None
        self.my_maquinaria = None
        self.contenedor = st.container()
        self.data = {}
    def render(self):
        st.subheader("Maquinaria")
        self.set_Marca_Modelo()
        st.divider()


    def load_modelos(self,marca:str):
        ruta = "data/maquinaria.json"
       
        if not os.path.exists(ruta):
            return []

        with open(ruta, "r") as f:
            contenido = json.load(f)

        self.data = contenido

        return list(contenido.get(marca, {}).keys())

    def set_Marca_Modelo(self):
        modelos:list=[]
        col1, col2 = st.columns(2)
        with col1:
            self.marca = self.set_input("select","Marca","select_get_marca",
                ["CAT","Komatsu","IPESA","CGM Rental","Rivera Diesel","Pro MP"])
            modelos = self.load_modelos(self.marca) if self.marca else []
        with col2:
            self.modelo = self.set_input("select","Modelo","select_get_modelo",modelos)


    def put_datos(self):
        if(self.marca != None and self.modelo != None):
            for x in self.data:
                pass

    def load_maq_data(self,modelo):
        return self.data.get(self.marca, {}).get(modelo, {})