# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10kNssZzRcW6H1rHnkg1JOmInYChrbgTt
"""

import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Calculadora de IMC", page_icon="🧮", layout="centered")

# Título de la aplicación
st.title("Calculadora del Índice de Masa Corporal (IMC)")

# Función para calcular el IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Input del usuario
peso = st.number_input("Introduce tu peso en kilogramos (kg):", min_value=0.0, format="%.2f")
altura = st.number_input("Introduce tu altura en metros (m):", min_value=0.0, format="%.2f")

# Primer botón: Mostrar fórmula
if st.button("Mostrar fórmula del IMC"):
    st.write("La fórmula del IMC es: ")
    st.latex(r"\text{IMC} = \frac{\text{peso (kg)}}{\text{altura (m)}^2}")

# Segundo botón: Calcular IMC
if st.button("Calcular IMC"):
    if peso > 0 and altura > 0:
        imc = calcular_imc(peso, altura)
        st.write(f"Tu IMC es: {imc:.2f}")

        # Interpretación del IMC
        if imc < 18.5:
            st.write("Estás en bajo peso.")
        elif 18.5 <= imc < 24.9:
            st.write("Tienes un peso normal.")
        elif 25.0 <= imc < 29.9:
            st.write("Tienes sobrepeso.")
        else:
            st.write("Tienes obesidad.")
    else:
        st.warning("Por favor, introduce valores válidos para peso y altura.")

# Pie de página
st.write("Calcula tu IMC para saber si estás en un rango saludable.")



