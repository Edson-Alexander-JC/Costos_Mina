import json
import os
import streamlit as st
from interfaces.tab import Tab

st.subheader("Mantenimiento")
maq_list:list = [
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
        st.subheader("Set Maquinaria")
        col1, col2 = st.columns(2)
        datos = {}
        for i, (tipo, label, key) in enumerate(maq_list):

            if i % 2 == 0:
                with col1:
                    valor = self.set_input(tipo, label, f"setmaq_{key}")
            else:
                with col2:
                    valor = self.set_input(tipo, label, f"setmaq_{key}")

            datos[key] = valor

        if st.button("Guardar maquinaria"):
            marca = datos["marca"]
            modelo = datos["modelo"]

            self.guardar_maquinaria(marca, modelo, datos)

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