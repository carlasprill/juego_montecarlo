import streamlit as st
import random

# Reglas de puntuación
def obtener_reglas():
    return {
        'unos': lambda d: d.count(1) * 1,
        'doses': lambda d: d.count(2) * 2,
        'treses': lambda d: d.count(3) * 3,
        'cuatros': lambda d: d.count(4) * 4,
        'cincos': lambda d: d.count(5) * 5,
        'seses': lambda d: d.count(6) * 6,
        'trio': lambda d: sum(d) if any(d.count(x) >= 3 for x in d) else 0,
        'cuaterna': lambda d: sum(d) if any(d.count(x) >= 4 for x in d) else 0,
        'full': lambda d: 25 if sorted([d.count(x) for x in set(d)]) == [2, 3] else 0,
        'escalera_pequena': lambda d: 30 if any(set(seq).issubset(set(d)) for seq in [[1,2,3,4], [2,3,4,5], [3,4,5,6]]) else 0,
        'escalera_grande': lambda d: 40 if sorted(d) in ([1,2,3,4,5], [2,3,4,5,6]) else 0,
        'yahtzee': lambda d: 50 if d.count(d[0]) == 5 else 0,
        'chance': lambda d: sum(d)
    }

REGLAS_PUNTUACION = obtener_reglas()

# Función para lanzar dados
def lanzar_dados(num_dados):
    return [random.randint(1, 6) for _ in range(num_dados)]

# Inicialización de estado en sesión
if 'ronda' not in st.session_state:
    st.session_state.ronda = 1
    st.session_state.dados = lanzar_dados(5)
    st.session_state.tiro = 1
    st.session_state.jugador = 1
    st.session_state.puntajes = {1: [], 2: []}
    st.session_state.categorias_usadas = {1: [], 2: []}

# Título
st.title("🎲 Yahtzee con Streamlit - Simulación Montecarlo")

st.markdown(f"**Ronda {st.session_state.ronda} | Jugador {st.session_state.jugador} | Lanzamiento {st.session_state.tiro}**")

# Mostrar dados
dados = st.session_state.dados
col1, col2, col3, col4, col5 = st.columns(5)
cols = [col1, col2, col3, col4, col5]

dados_a_relanzar = []
for i in range(5):
    with cols[i]:
        if st.checkbox(f"Dado {i+1}: 🎲 {dados[i]}", key=f"dado_{i}"):
            dados_a_relanzar.append(i)

# Botón para relanzar
if st.session_state.tiro < 3:
    if st.button("🔁 Relanzar Dados"):
        for i in dados_a_relanzar:
            dados[i] = random.randint(1, 6)
        st.session_state.dados = dados
        st.session_state.tiro += 1
        st.rerun()

# Mostrar categorías disponibles
categorias_disponibles = [cat for cat in REGLAS_PUNTUACION if cat not in st.session_state.categorias_usadas[st.session_state.jugador]]
st.markdown("### 🧮 Categorías disponibles")
for cat in categorias_disponibles:
    puntuacion = REGLAS_PUNTUACION[cat](dados)
    st.markdown(f"- **{cat}**: {puntuacion}")

# Selección de categoría
categoria = st.selectbox("Selecciona una categoría para puntuar", categorias_disponibles)
if st.button("✅ Confirmar categoría"):
    puntos = REGLAS_PUNTUACION[categoria](dados)
    st.session_state.puntajes[st.session_state.jugador].append(puntos)
    st.session_state.categorias_usadas[st.session_state.jugador].append(categoria)

    # Cambiar turno o avanzar ronda
    if st.session_state.jugador == 1:
        st.session_state.jugador = 2
    else:
        st.session_state.jugador = 1
        st.session_state.ronda += 1

    # Reiniciar turno
    st.session_state.tiro = 1
    st.session_state.dados = lanzar_dados(5)

    # Fin del juego
    if st.session_state.ronda > 13:
        st.markdown("## 🏁 Juego finalizado")
        st.stop()
    st.rerun()

# Mostrar puntajes
st.markdown("---")
st.markdown("### 📊 Puntajes actuales")
st.write(f"Jugador 1: {sum(st.session_state.puntajes[1])} puntos")
st.write(f"Jugador 2: {sum(st.session_state.puntajes[2])} puntos")