# 🎲 Yahtzee Montecarlo con Streamlit

Bienvenido a la aplicación web interactiva de Yahtzee basada en Montecarlo. ¡Sigue estos pasos para instalar, configurar y jugar!

---

## 🚀 Instalación rápida

1. **Clona o descarga** este proyecto  
```bash
git clone https://github.com/carlasprill/juego_montecarlo.git
```

2. **(Opcional) Crea un entorno virtual**

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. **Instala dependencias**

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecutar la app

```bash
streamlit run yahtzee_app.py
```

* Abre tu navegador en `http://localhost:8501` (o el puerto que indique la consola).
* Si `8501` está ocupado, prueba:

```bash
streamlit run yahtzee_app.py --server.port 8502
```

---

## 🎮 Cómo jugar

1. **Encabezado dinámico**
   📄 Muestra Ronda ▶️ Jugador ▶️ Tiro actual.

2. **Selecciona dados a relanzar**

   * Haz clic en el checkbox bajo cada dado 🎲 para marcarlo.
   * Pulsa **🔁 Relanzar Dados** (máx. 3 tiros por turno).

3. **Elige categoría**

   * Tras tu último tiro, abre el desplegable y selecciona dónde puntuar.
   * Verás los **puntos posibles** al lado.

4. **Confirma tu elección**

   * Pulsa **✅ Puntuar**.
   * El turno pasará al siguiente jugador o avanzará de ronda.

5. **Consulta tus puntajes**

   * En la **barra lateral**, verás el total acumulado de Jugador 1 y Jugador 2.

6. **Fin de la partida**

   * Tras 13 rondas (o tu configuración), la app mostrará globos 🎈 y anunciará el ganador o empate.

---

¡Disfruta de Yahtzee en tu navegador! 🥳

---