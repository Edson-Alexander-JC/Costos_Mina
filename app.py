import streamlit as st
import pandas as pd
#TABS
from domain.tab_mantenimiento import TabMantenimiento
from domain.tab_mano_obra import TabManoObra
from domain.tab_maquinaria import TabMaquinaria
from domain.tab_set_maq import TabSetMaq
#DOMAINS
from domain.maquinaria_domain import MaquinariaDomain
from domain.mantenimiento_maq import MantenimientoDomain
from domain.mano_obra import ManoObraDomain
#DATA_SETS
from interfaces.data_maquinaria import DataMaquinaria
from interfaces.data_mantenimiento import DataMantenimiento
from interfaces.data_obrero import DataObrero

data = {
    0: ("Maquinaria", [
            "valor1", 
            "valor2"
        ]),
    1: ("Resultados", {"res1": 0, "res2": 0}),
    2: ("Resumen", {"total": 0})
}

tab_man = TabMantenimiento(data)
tab_maq = TabMaquinaria()
tab_mo = TabManoObra()



st.title("Costos Mineros")

tab1, tab2, tab3, tab4 = st.tabs([
    "Set Maquinaria Data"
    "Costos Operación",
    "Mantenimiento",
    "Mano de Obra"
])

# ---------------- TAB 1 ----------------
with tab1:
    tab_set_maq = TabSetMaq()
    tab_set_maq.render()
# ---------------- TAB 2 ----------------
with tab2:
    tab_man.render()
# ---------------- TAB 3 ----------------
with tab3:
    tab_man.render()
# ---------------- TAB 4 ----------------
with tab4:
    tab_man.render()
