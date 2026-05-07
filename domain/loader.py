import json
import os
import streamlit as st
from interfaces.tab import Tab
from interfaces.data_maquinaria import DataMaquinaria
class Loader(Tab):

    def __init__(self):
        self.ruta = "data/maquinaria.json"
        self.my_maquinaria = None
        self.load_data()

    def render(self):
        modelos:list=[]
        col1, col2 = st.columns(2)
        with col1:
            self.marca = self.set_input("select","Marca","select_get_marca",
                ["Nuevo","CAT","Komatsu","IPESA","CGM Rental","Rivera Diesel","Pro MP"])
            modelos = self.load_modelos(self.marca)
        with col2:
            if modelos:
                self.modelo = self.set_input("select","Modelo","select_get_modelo",modelos)
            else:
                self.modelo = self.set_input("string","Modelo","set_modelo")

    def save_data(self,datos):
        contenido = self.acces_to_data_file()
        # 3. Crear marca si no existe
        if self.marca not in contenido:
            contenido[self.marca] = {}
        # 4. Crear modelo si no existe
        if self.modelo not in contenido[self.marca]:
            contenido[self.marca][self.modelo] = {}
        # 5. Guardar datos
        contenido[self.marca][self.modelo] = datos

        # 6. Guardar archivo
        with open(self.ruta, "w") as f:
            json.dump(contenido, f, indent=4)

    def load_data(self):
        contenido = self.acces_to_data_file()
        self.data = contenido

    def acces_to_data_file(self):
        # 1. Crear carpeta si no existe
        os.makedirs("data", exist_ok=True)
        # 2. Cargar archivo si existe
        if os.path.exists(self.ruta):
            with open(self.ruta, "r") as f:
                contenido = json.load(f)
                return contenido
        else: 
                contenido = {}
                return contenido

    def load_modelos(self,marca:str):
        return list(self.data.get(marca, {}).keys())
      
    def load_maquina(self,modelo):
        return self.data.get(self.marca, {}).get(modelo, {})
    
    def get_maquinaria(self):
        if not self.marca or not self.modelo: return None
        return self.data[self.marca][self.modelo]

    def get_clase_maquinaria(self):
        if self.my_maquinaria: return self.my_maquinaria
        maquinaria = self.data[self.marca][self.modelo]
        return DataMaquinaria(
            maquinaria["kind_of_maq"],#valor_adquisicion:float,
            maquinaria["valor_adquisicion"],#valor_adquisicion:float,
            maquinaria["vida_economica_util"],#vida_economica_util:float,
            maquinaria["combustible_percent"],#combustible_percent:float,
            maquinaria["lubricante_percent"],#lubricante_percent:float,
            maquinaria["potencia_KW"],#potencia_KW:float,
            maquinaria["capacidad"],#capacidad:float,
            maquinaria["interes"],#interes:float,
            maquinaria["disponibilidad_mec"],#disponibilidad_mec:float,
            maquinaria["seguro"],#seguro:float,# 0.75% al 1.5% o  2% al 4%
            maquinaria["horas_operativas_anual"],#horas_operativas_anual:int
            maquinaria["importado"],#importado:bool
        )
