import json
import os
import streamlit as st
from interfaces.tab import Tab

maq_list:list = [
    ["select","Tipo de maquinaria","kind_of_maq",["Perforadora","Retroexcavadora","Volquete"]],
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
        self.marca:dict = {}
        self.modelo:dict = {}
    def render(self):
        st.subheader("Añadir Maquinaria")
        self.set_Marca_Modelo()
        st.divider()
        self.set_atributos()
        st.divider()
        col = st.columns(1)[0]
        with col:  
            if st.button("Guardar maquinaria", use_container_width=True):
                self.datos["marca"] = self.marca
                self.datos["modelo"] = self.modelo
                self.guardar_maquinaria()

    def guardar_maquinaria(self):
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
        if self.marca not in contenido:
            contenido[self.marca] = {}
        # 4. Crear modelo si no existe
        if self.modelo not in contenido[self.marca]:
            contenido[self.marca][self.modelo] = {}
        # 5. Guardar datos
        contenido[self.marca][self.modelo] = self.datos

        # 6. Guardar archivo
        with open(ruta, "w") as f:
            json.dump(contenido, f, indent=4)

    def set_Marca_Modelo(self):
        col1, col2 = st.columns(2)
        with col1:
            self.marca = self.set_input("select","Marca","select_set_marca",
                ["CAT","Komatsu","IPESA","CGM Rental","Rivera Diesel","Pro MP"])
                     
        with col2:
            self.modelo = self.set_input("string","Modelo","select_set_modelo")
    def set_atributos(self):
        col1, col2, col3 = st.columns(3)

        for i, item in enumerate(maq_list):
            tipo = item[0]
            label = item[1]
            key = item[2]
            options = item[3] if len(item) > 3 else None

            if i % 3 == 0:
                with col1:
                    valor = self.set_input(tipo, label, f"setmaq_{key}", options)

            elif i % 3 == 1:
                with col2:
                    valor = self.set_input(tipo, label, f"setmaq_{key}", options)

            else:
                with col3:
                    valor = self.set_input(tipo, label, f"setmaq_{key}", options)

            self.datos[key] = valor
        
    def guardar_data(self):pass
    