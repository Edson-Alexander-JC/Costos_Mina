import streamlit as st
from abc import ABC, abstractmethod
class Tab(ABC):
    @abstractmethod
    def render(self):pass
    
    def set_input(self, tipo:str,label:str,key:str,options=None,value=None,unidad:str=""):
        col1, col2 = st.columns([4,1])

        with col1:
            match tipo:
                case "string":
                    resultado = st.text_input(label,value=value or "",key=key)
                case "number":
                    resultado = st.number_input(label,min_value=0,step=1,value=value or 0,key=key)
                case "float":
                    resultado = st.number_input(label,value=value or 0.0,format="%.2f",key=key)
                case "select":
                    index = 0
                    if options and value in options: index = options.index(value)

                    resultado = st.selectbox(label,options,index=index,key=key)

                case "list":
                    resultado = self.input_list(label, key)
                case "bool":
                    resultado = st.checkbox(label,value=value if value is not None else False,key=key)
                case _:
                    st.warning("Tipo no soportado: " + tipo)
                    resultado = None
        with col2:
            st.markdown(f"""
                <div style="
                    display:flex;
                    align-items:end;
                    height:68px;
                    font-size:14px;
                    color:gray;
                ">{unidad}</div>
                """,
                unsafe_allow_html=True
            )

        return resultado


    def set_output(self, tipo: str, label: str, value, unidad: str = ""):
        match tipo:

            case "number":
                return st.metric(label, f"{int(value or 0)} {unidad}")

            case "float":
                return st.metric(label, f"{(value or 0):.2f} {unidad}")

            case "string":
                return st.metric(label, f"{value or ''} {unidad}")

            case "bool":
                return st.metric(label, "Sí" if value else "No")

            case _:
                st.warning("Tipo no soportado: " + tipo)
    def set_data(data):pass