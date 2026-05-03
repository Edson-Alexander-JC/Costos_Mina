import streamlit as st
from abc import ABC, abstractmethod
class Tab(ABC):
    @abstractmethod
    def render(self):pass

    def set_input(type:str,label:str,key:str, options=None):
        match type:
            case "string":
                return st.text_input(label, key=key)

            case "number":
                return st.number_input(label, key=key)

            case "float":
                return st.number_input(label, key=key, format="%.2f")

            case "select":
                return st.selectbox(label, options, key=key)

            case "list":
                return self.input_list(label, key)

            case _:
                st.warning(f"Tipo no soportado: {tipo}")