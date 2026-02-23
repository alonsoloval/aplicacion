import streamlit as st
import pandas as pd

if "actividades" not in st.session_state:
    st.session_state.actividades = []

opcion = st.sidebar.selectbox("Selecciona una pagina:", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

# Pagina Home

if opcion == "Home":
    st.title("Aplicación Python for Analytics")
    st.write("---")
    st.write("**Título del proyecto:** Aplicación Python for Analytics")
    st.write("**Nombre completo del estudiante:** Alonso Lovon Alvarez")
    st.write("**Nombre del curso o especialización:** Especialiación Python for Analytics")
    st.write("**Año:** 2026")
    st.write("**Breve descripción:** Aplicación interactiva que integra los temas y módulos aprendidos en clase (Variables, estructuras de datos, control de flujo, funciones, programación funcional y POO).")
    st.write("**Tecnologías utilizadas:** Python, Streamlit, Pandas")

# Ejercicio 1 - Variables y Condicionales

elif opcion == "Ejercicio 1":
    st.subheader("Ejercicio 1: Verificador de Presupuesto")
    
    presupuesto = st.number_input("Ingresa tu presupuesto:", min_value=0.0)
    gasto = st.number_input("Ingresa tu gasto:", min_value=0.0)
    
    if st.button("Evaluar"):
        diferencia = presupuesto - gasto
        if gasto <= presupuesto:
            st.success("El gasto está dentro del presupuesto.")
        else:
            st.warning("El presupuesto fue excedido.")
        
        st.write(f"**Diferencia entre presupuesto y gasto:** S/. {diferencia:.2f}")

# Ejercicio 2 - Listas y Diccionarios

elif opcion == "Ejercicio 2":
    st.subheader("Ejercicio 2: Registro de Actividades Financieras")
    
    nombre = st.text_input("Nombre de la actividad:")
    tipo = st.selectbox("Tipo de actividad:", ["Operativa", "Inversión", "Financiamiento"])
    presup_act = st.number_input("Presupuesto asignado:", min_value=0.0)
    gasto_act = st.number_input("Gasto real:", min_value=0.0)
    
    if st.button("Agregar Actividad"):
        nueva_actividad = {
            "nombre": nombre,
            "tipo": tipo,
            "presupuesto": presup_act,
            "gasto_real": gasto_act
        }
        st.session_state.actividades.append(nueva_actividad)
        st.success(f"Actividad '{nombre}' agregada con éxito.")
    
    st.write("### Lista de Actividades")
    if len(st.session_state.actividades) > 0:
        
        df = pd.DataFrame(st.session_state.actividades)
        st.dataframe(df)
        
        st.write("### Estado de Actividades")
        for act in st.session_state.actividades:
            estado = "Dentro del presupuesto" if act["gasto_real"] <= act["presupuesto"] else "Presupuesto excedido"
            st.write(f"- **{act['nombre']}**: {estado}")
    else:
        st.write("Aún no hay actividades registradas. Agrega una arriba.")

# Ejercicio 3 - Funciones y Programación Funcional

elif opcion == "Ejercicio 3":
    st.subheader("Ejercicio 3: Retorno Esperado")
    
    tasa = st.slider("Tasa de retorno mensual (%)", min_value=0.0, max_value=20.0, step=0.5) / 100
    meses = st.number_input("Cantidad de meses:", min_value=1, step=1)
    
    def calcular_retorno(actividad, t, m):
        return actividad["presupuesto"] * t * m
        
    if st.button("Calcular Retornos"):
        if len(st.session_state.actividades) > 0:
            retornos = list(map(lambda act: calcular_retorno(act, tasa, meses), st.session_state.actividades))
            
            st.write("### Retorno Esperado por Actividad")
            for act, ret in zip(st.session_state.actividades, retornos):
                st.write(f"- **{act['nombre']}**: S/.{ret:.2f}")
        else:
            st.warning("Ve al Ejercicio 2 y registra al menos una actividad primero.")

# Ejercicio 4 - Programacion Orientada a Objetos

elif opcion == "Ejercicio 4":
    st.subheader("Ejercicio 4: Programacion Orientada a Objetos")
    
    class Actividad:
        def __init__(self, nombre, tipo, presupuesto, gasto_real):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto_real = gasto_real
            
        def esta_en_presupuesto(self):
            return self.gasto_real <= self.presupuesto
            
        def mostrar_info(self):
            return f"Actividad: {self.nombre} | Tipo: {self.tipo} | Presupuesto: S/. {self.presupuesto} | Gasto: S/. {self.gasto_real}"
            
    if len(st.session_state.actividades) > 0:
        st.write("### Información de Objetos Creados")
        objetos_actividad = [Actividad(**act) for act in st.session_state.actividades]
        
        for obj in objetos_actividad:
            st.write(obj.mostrar_info())
            if obj.esta_en_presupuesto():
                st.success("Cumple el presupuesto")
            else:
                st.warning("No cumple el presupuesto")
    else:
        st.write("Ve al Ejercicio 2 y registra al menos una actividad primero para crear los objetos.")




