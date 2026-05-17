# app.py
import streamlit as st
import random
import time

st.set_page_config(page_title="Ecuaciones de Primer Grado", page_icon="📘")

# CSS para animaciones
st.markdown("""
<style>
.big-text {
    font-size: 35px;
    font-weight: bold;
    color: #4CAF50;
    text-align: center;
    animation: aparecer 1s ease-in-out;
}

@keyframes aparecer {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.correcto {
    animation: pulse 0.6s infinite alternate;
    color: green;
    font-size: 28px;
    font-weight: bold;
    text-align: center;
}

@keyframes pulse {
    from {transform: scale(1);}
    to {transform: scale(1.1);}
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-text">📘 Generador de Ecuaciones</p>', unsafe_allow_html=True)

# Generar ecuación
def generar():
    a = random.randint(1, 10)
    x = random.randint(1, 20)
    b = random.randint(1, 15)
    c = a * x + b
    return a, x, b, c

# Guardar datos
if "datos" not in st.session_state:
    st.session_state.datos = generar()

a, x_real, b, c = st.session_state.datos

# Mostrar ecuación
st.subheader("Resuelve la ecuación:")
st.latex(f"{a}x + {b} = {c}")

# Entrada usuario
respuesta = st.number_input("Ingresa el valor de x:", step=1)

# Botón verificar
if st.button("Verificar respuesta"):
    
    with st.spinner("Verificando..."):
        time.sleep(1)

    if respuesta == x_real:
        st.balloons()
        st.markdown(
            '<p class="correcto">✅ ¡Correcto!</p>',
            unsafe_allow_html=True
        )
    else:
        st.error(f"❌ Incorrecto. La respuesta correcta era x = {x_real}")

# Nueva ecuación
if st.button("Nueva ecuación"):
    st.session_state.datos = generar()
    st.rerun()
