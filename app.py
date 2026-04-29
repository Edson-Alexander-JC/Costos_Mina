import streamlit as st
import pandas as pd

st.title("Sistema de Costos Mineros")

tab1, tab2, tab3 = st.tabs([
    "Costos Operación",
    "Mantenimiento",
    "Mano de Obra"
])

# ---------------- TAB 1 ----------------
with tab1:
    st.subheader("Costos de Operación")

    horas = st.number_input("Horas")
    costo = st.number_input("Costo por hora")

    if st.button("Calcular Operación"):
        total = horas * costo
        st.write("Costo Operación:", total)

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
