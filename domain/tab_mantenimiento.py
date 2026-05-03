import streamlit as st
from interfaces.tab import Tab

class TabMantenimiento(Tab):

    def __init__(self,data:dict):
        self.col1 = data[0]
        self.col2 = data[1]
        self.col3 = data[3]

    def render(self):
            st.subheader("Mantenimiento")

            col1, col2, col3 = st.columns([1, 2,3])
            with col1:
                self.set_col1(col1[0],col1[1])
                calcular = st.button("Calcular Operación", key="btn_op")

            with col2:
                self.set_col2(col2[0],col2[1])
            with col3:
                self.set_col3(col3[0],col3[1])


    def set_inputs(self, title: str, label_value: list):
        st.markdown(title)
        for x in label_value:
            st.number_input(x,key=x)
        
    def set_viewputs(title:str,label_value:dict):
        st.markdown(title)
        for x in label_value:
            st.metric(x,label_value[x])
        

    def set_col1(self,title:str,label_value:array):
        self.set_inputs(title,label_value)
    def set_col2(self,title:str,label_value:dict):
        self.set_mini_view(title,label_value)
    def set_col3(self,title:str,label_value:dict):
        self.set_mini_view(title,label_value)