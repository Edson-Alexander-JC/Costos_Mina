import json
import os
import streamlit as st
from interfaces.tab import Tab
from domain.maquinaria_domain import MaquinariaDomain

class TabSetMaq(Tab):
    
    maq_list = [
        {"tipo": "select", 
         "label": "Tipo de maquinaria", 
         "key": "kind_of_maq",
         "options": ["Perforadora", "Retroexcavadora", "Volquete"]
        },
        {"tipo": "float","label": "Valor adquisicion","key": "valor_adquisicion"},
        {"tipo": "number","label": "Vida economica util","key": "vida_economica_util"},
        {"tipo": "float","label": "Consumo de combustible","key": "combustible_percent"},
        {"tipo": "float","label": "Consumo de lubricante","key": "lubricante_percent"},
        {"tipo": "float","label": "Potencia (KW)","key": "potencia_KW"},
        {"tipo": "float","label": "Capacidad","key": "capacidad"},
        {"tipo": "float","label": "Interes","key": "interes"},
        {"tipo": "float","label": "Disponibilidad mecanica","key": "disponibilidad_mec"},
        {"tipo": "float","label": "Seguro","key": "seguro"},
        {"tipo": "number","label": "Horas operativas anuales","key": "horas_operativas_anual"},
        {"tipo": "bool","label": "es importado","key": "importado"},
    ]

    def __init__(self):
        self.datos = {}
        self.data = {}

    def set_data(self,data):
        self.data = data
        
    def render(self):
        col1, col2, col3 = st.columns(3)
        for i, item in enumerate(self.maq_list):
            tipo = item["tipo"]
            label = item["label"]
            key = item["key"]
            options = item.get("options")

            if i % 3 == 0:
                with col1:
                    valor = self.set_input(tipo, label,key,options)

            elif i % 3 == 1:
                with col2:
                    valor = self.set_input(tipo, label,key,options)

            else:
                with col3:
                    valor = self.set_input(tipo, label,key,options)

            self.datos[key] = valor