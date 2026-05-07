import streamlit as st
import pandas as pd
from interfaces.tab import Tab
#TABS
from domain.tab_mantenimiento import TabMantenimiento
from domain.tab_mano_obra import TabManoObra
from domain.tab_set_maq import TabSetMaq
from domain.tab_maquinaria import TabMaquinaria
from domain.sub_depreciacion import SubDepreciacion
#DOMAINS
from domain.maquinaria_domain import MaquinariaDomain
from domain.mantenimiento_maq import MantenimientoDomain
from domain.mano_obra import ManoObraDomain
from domain.loader import Loader


data = {
    0: ("Maquinaria", [
            "valor1", 
            "valor2"
        ]),
    1: ("Resultados", {"res1": 0, "res2": 0}),
    2: ("Resumen", {"total": 0})
}

loader = Loader()
tab_mo = TabManoObra()
tab_set_maq = TabSetMaq()
depreciacion = SubDepreciacion()
maquinaria = None

def update_renderizado(marca,modelo):
    data = loader.get_maquinaria() or {}
    if "last_modelo" not in st.session_state: st.session_state.last_modelo = None
    
    if marca and modelo and data:
        maquinaria = loader.get_clase_maquinaria()

        if st.session_state.last_modelo != modelo:
            for k, v in data.items():
                st.session_state[k] = v
            st.session_state.last_modelo = modelo

        tab_set_maq.set_data(data)

        if maquinaria:
            depreciacion.set_data(maquinaria)


def guardar_datos(data,marca,modelo,guardar_click):
    if guardar_click:
        if not marca or not modelo:
            st.warning("Falta marca o modelo")
        else:
            datos = getattr(tab_set_maq, "datos", {})
            loader.save_data(datos)
            st.success("Guardado correctamente")

def calcular_costos(tab_class:Tab):
    if st.session_state.get("calcular", False):
        maquinaria = loader.get_clase_maquinaria()
        if maquinaria:
            tab_class.set_data(maquinaria)
            tab_class.render()
    else:
        st.info("Seleccione una maquinaria y presione calcular")
# ---------------- APP ----------------

st.title("Costos Mineros")

tab1, tab2 = st.tabs([
    "Maquinaria",
    "Mano de Obra"
])

# ---------------- TAB 1 ----------------
with tab1:
    loader.render()
    sub_tab1, sub_tab2, sub_tab3 = st.tabs([
        "Datos de la maquinaria",
        "Costos de la maquinaria",
        "Costos de mantenimiento",
    ])
    with sub_tab1:
        marca = st.session_state.get("select_get_marca")
        modelo = st.session_state.get("select_get_modelo")
        update_renderizado(marca,modelo)
        tab_set_maq.render()

        st.divider()
        depreciacion.render()

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Calcular", key="btn_calcular_top", use_container_width=True):
                st.session_state.calcular = True

        with col2:
            guardar_click = st.button("Guardar", use_container_width=True)
            
        guardar_datos(data,marca,modelo,guardar_click)


    with sub_tab2:
        calcular_costos(TabMaquinaria())
    with sub_tab3:
        calcular_costos(TabMantenimiento())


# ---------------- TAB 2 ----------------
with tab2: pass


    