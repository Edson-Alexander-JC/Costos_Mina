import streamlit as st
from interfaces.tab import Tab

class TabMantenimiento(Tab):

    def __init__(self):
        self.my_maquinaria = None
    def set_data(self,data): 
        self.my_maquinaria = data
    def render(self):
        st.subheader("Mantenimiento")

        col1, col2, col3 = st.columns([1, 2, 3])

        with col1:
            self.set_col1(self.col1[0], self.col1[1])
            st.button("Calcular Operación", key="btn_op")

        with col2:
            self.set_col2(self.col2[0], self.col2[1])

        with col3:
            self.set_col3(self.col3[0], self.col3[1])

    def set_inputs(self, title: str, label_value: list):
        st.markdown(title)
        for x in label_value:
            st.number_input(x, key=x)

    def set_viewputs(self, title: str, label_value: dict):
        st.markdown(title)
        for x in label_value:
            st.metric(x, label_value[x])

    def set_col1(self, title: str, label_value: list):
        self.set_inputs(title, label_value)

    def set_col2(self, title: str, label_value: dict):
        self.set_viewputs(title, label_value)

    def set_col3(self, title: str, label_value: dict):
        self.set_viewputs(title, label_value)