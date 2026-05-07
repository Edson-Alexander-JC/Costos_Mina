import streamlit as st
from interfaces.tab import Tab
from domain.maquinaria_domain import MaquinariaDomain

class TabMaquinaria(Tab):
    
    def __init__(self): self.my_maquinaria = None
    def set_data(self,data):
        self.my_maquinaria = data
    def render(self):
        st.subheader("Costos por posecion")
        self.rend_costos_pos()
        st.divider()
        st.subheader("Costos de operacion")
        self.rend_costos_op()
        st.divider()
        st.subheader("Costos del operador")
        self.rend_costos_ope()

    def rend_costos_pos(self): 
        depresicion = self.my_maquinaria.calc_depreciacion()
        interes = self.my_maquinaria.calc_interes()
        impuestos_pos = self.my_maquinaria.calc_impuestos()
        seguro = self.my_maquinaria.calc_seguro()
        costos_pos = [
            {"tipo":"float","label":"depreciacion","value":depresicion,"unidad":""},
            {"tipo":"float","label":"interes","value":interes,"unidad":""},
            {"tipo":"float","label":"impuestos","value":impuestos_pos,"unidad":""},
            {"tipo":"float","label":"seguro","value":seguro,"unidad":""},
        ]
        self.render_outputs(costos_pos)
        costos_posecion = self.my_maquinaria.calc_costos_posecion()
        self.set_output("float","COSTOS DE POSECION",costos_posecion)
    def rend_costos_op(self):
        combustible = self.my_maquinaria.set_costos_combustible(10)
        libricante = self.my_maquinaria.set_costos_lubricante(10)
        filto = self.my_maquinaria.calc_costos_filtros()
        neumaticos = self.my_maquinaria.set_costos_neumaticos(100,50)
        piezas_desgaste = self.my_maquinaria.suma_costos_piezas()
        mantenimiento = self.my_maquinaria.set_mantenimiento(10)
        costos_op = [
            {"tipo":"float","label":"combustible","value":combustible,"unidad":"asds"},
            {"tipo":"float","label":"libricante","value":libricante,"unidad":"asds"},
            {"tipo":"float","label":"filto","value":filto,"unidad":"asds"},
            {"tipo":"float","label":"neumaticos","value":neumaticos,"unidad":"asds"},
            {"tipo":"float","label":"piezas_desgaste","value":piezas_desgaste,"unidad":"asds"},
            {"tipo":"float","label":"mantenimiento","value":mantenimiento,"unidad":"asds"},
        ]
        self.render_outputs(costos_op)
        costo_horario_operacion = self.my_maquinaria.calc_horario_operacion()
        self.set_output("float","COSTO HORARIO DE OPERACION",costo_horario_operacion)
    def rend_costos_ope(self): 
        mano_obra = self.my_maquinaria.set_costos_mano_obra(10)
        
        self.set_output("float","COSTO DEL OPERADOR",mano_obra)


    def render_outputs(self, lista: list):

        columnas = min(len(lista), 3)

        for inicio in range(0, len(lista), columnas):

            fila = lista[inicio:inicio + columnas]

            cols = st.columns(columnas)

            for i, item in enumerate(fila):

                with cols[i]:

                    with st.container(border=True):

                        self.set_output(
                            item["tipo"],
                            item["label"],
                            item["value"],
                            item.get("unidad", "")
                        )