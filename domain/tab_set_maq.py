import json
import os
import streamlit as st
from interfaces.tab import Tab


maq_list:list = [
    ["float","Valor adquisicion","valor_adquisicion"],
    ["number","Vida economica util","vida_economica_util"],
    ["float","Valor residual","valor_residual"],
    ["float","Consumo de combustible","combustible_percent"],
    ["float","Consumo de lubricante","lubricante_percent"],
    ["float","Potencia (KW)","potencia_KW"],
    ["float","Capacidad","capacidad"],
    ["float","Interes","interes"],
    ["float","Disponibilidad mecanica","disponibilidad_mec"],
    ["float","Seguro","seguro"],
    ["number","Horas operativas anuales","horas_operativas_anual"],
]

class TabSetMaq(Tab):
    def __init__(self):
        self.datos:dict = {}
    def render(self):
        st.subheader("Set Maquinaria")
        self.set_Marca_Modelo()
        st.divider()
        self.set_atributos()
        st.divider()
        if st.button("Guardar maquinaria"):
            self.guardar_data()

    def guardar_maquinaria(marca: str, modelo: str, datos: dict):
        ruta = "data/maquinaria.json"

        # 1. Crear carpeta si no existe
        os.makedirs("data", exist_ok=True)

        # 2. Cargar archivo si existe
        if os.path.exists(ruta):
            with open(ruta, "r") as f:
                contenido = json.load(f)
        else:
            contenido = {}

        # 3. Crear marca si no existe
        if marca not in contenido:
            contenido[marca] = {}

        # 4. Crear modelo si no existe
        if modelo not in contenido[marca]:
            contenido[marca][modelo] = {}

        # 5. Guardar datos
        contenido[marca][modelo] = datos

        # 6. Guardar archivo
        with open(ruta, "w") as f:
            json.dump(contenido, f, indent=4)

    def set_Marca_Modelo(self):
        col1, col2 = st.columns(2)
        with col1:
            self.set_input("string","Marca","marca")
        with col2:
            self.set_input("string","Modelo","modelo")
    def set_atributos(self):
        col1, col2, col3 = st.columns(3)

        for i, (tipo, label, key) in enumerate(maq_list):

            if i % 3 == 0:
                with col1:
                    valor = self.set_input(tipo, label, f"setmaq_{key}")

            elif i % 3 == 1:
                with col2:
                    valor = self.set_input(tipo, label, f"setmaq_{key}")

            else:
                with col3:
                    valor = self.set_input(tipo, label, f"setmaq_{key}")

            self.datos[key] = valor
        
    def guardar_data(self):pass