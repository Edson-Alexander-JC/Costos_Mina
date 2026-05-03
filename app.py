import streamlit as st
import pandas as pd
from domain import tab_maquinaria, tab_mantenimiento as TabMantenimiento, tab_obrero

data = {
    0: ("Entradas", ["valor1", "valor2"]),
    1: ("Resultados", {"res1": 0, "res2": 0}),
    3: ("Resumen", {"total": 0})
}
tab_m = TabMantenimiento(data)
st.title("Costos Mineros")

tab1, tab2, tab3 = st.tabs([
    "Costos Operación",
    "Mantenimiento",
    "Mano de Obra"
])

# ---------------- TAB 1 ----------------
with tab1:
    tab_m.render()

# ---------------- TAB 2 ----------------
with tab2:
    st.subheader("Mantenimiento")

    costo_op = st.number_input("Costo operación base")

    if st.button("Calcular Mantenimiento"):
        mantenimiento = costo_op * 0.15
        st.write("Mantenimiento:", mantenimiento)

# ---------------- TAB 3 ----------------
with tab3:
    st.subheader("Mano de Obra")

    trabajadores = st.number_input("N° trabajadores")
    salario = st.number_input("Salario")

    if st.button("Calcular Mano de Obra"):
        total = trabajadores * salario
        st.write("Costo Mano de Obra:", total)
