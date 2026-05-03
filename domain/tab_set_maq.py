import json
import os
import streamlit as st
from interfaces.tab import Tab

st.subheader("Mantenimiento")
maq_atributes_list:dict = {
    "valor adquisicion":"valor_adquisicion",
    "vida economica_util":"vida_economica_util",
    "valor residual":"valor_residual",
    "consumo de combustible":"combustible_percent",
    "consumo de lubricante":"lubricante_percent",
    "potencia (KW)":"potencia_KW",
    "capacidad":"capacidad",
    "interes":"interes",
    "disponibilidad mecanica":"disponibilidad_mec",
    "seguro":"seguro",
    "horas operativas anuales":"horas_operativas_anual",
}

class TabSetMaq(Tab):

    def __init__(self):pass

    def render(self):
        self.set_inputs()
    
    def set_inputs(self):
        for x in maq_atributes_list:
            st.number_input(x, key=maq_atributes_list[x])

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