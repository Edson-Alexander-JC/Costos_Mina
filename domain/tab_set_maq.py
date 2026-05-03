import json
import os
import streamlit as st
from interfaces.tab import Tab

st.subheader("Mantenimiento")
maq_list:dic = [
    ["string","Marca","marca"],
    ["string","Modelo","modelo"],
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

    def __init__(self):pass

    def render(self):
        self.set_inputs()
    
    def set_inputs(self):
        for x in maq_list:
            st.number_input(x, key=maq_list[x])

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