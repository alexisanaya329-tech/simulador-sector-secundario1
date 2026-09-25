import streamlit as st
import time

# Configuración de la página
st.set_page_config(
    page_title="Simulador del Sector Secundario",
    page_icon="🏭",
    layout="wide"
)

# Título y encabezado
st.title("🏭 Simulador del Sector Secundario")
st.subheader("Transformación de Materia Prima, Optimización y Análisis de Procesos")

st.markdown("""
Esta aplicación simula el funcionamiento de una planta industrial:
recibe materias primas, las procesa para obtener productos finales y evalúa la eficiencia operativa.
""")

# Barra lateral para selección de la industria
st.sidebar.header("⚙️ Configuración de la Planta")
industria = st.sidebar.selectbox(
    "Selecciona el Tipo de Industria:",
    ["Siderúrgica (Acero)", "Maderera (Muebles)", "Textil (Ropa)"]
)

st.sidebar.divider()

# Parámetros según la industria seleccionada
if industria == "Siderúrgica (Acero)":
    materia_nombre = "Hierro y Carbón (Toneladas)"
    producto_nombre = "Vigas de Acero"
    img_materia = "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=600&q=80"
    img_proceso = "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=600&q=80"
    img_producto = "https://images.unsplash.com/photo-1535813547-99c456a41d4a?auto=format&fit=crop&w=600&q=80"
    ratio_optimo = 1.5  # 1.5 Tn de materia prima por 1 Tn de producto

elif industria == "Maderera (Muebles)":
    materia_nombre = "Lotes de Madera en Bruto"
    producto_nombre = "Mesas y Sillas de Madera"
    img_materia = "https://images.unsplash.com/photo-1520116468816-95b69f847357?auto=format&fit=crop&w=600&q=80"
    img_proceso = "https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=600&q=80"
    img_producto = "https://images.unsplash.com/photo-1538688525198-9b88f6f53126?auto=format&fit=crop&w=600&q=80"
    ratio_optimo = 2.0

else:  # Textil
    materia_nombre = "Fardos de Algodón"
    producto_nombre = "Prendas de Vestir"
    img_materia = "https://images.unsplash.com/photo-1605000797499-95a51c5269ae?auto=format&fit=crop&w=600&q=80"
    img_proceso = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=600&q=80"
    img_producto = "https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?auto=format&fit=crop&w=600&q=80"
    ratio_optimo = 1.2

# Controles de simulación
cant_materia = st.sidebar.slider(f"Cantidad de {materia_nombre}:", 10, 200, 100)
eficiencia_maquinaria = st.sidebar.slider("Eficiencia de la Maquinaria (%):", 30, 100, 80)

# Cálculo de producción
materia_efectiva = cant_materia * (eficiencia_maquinaria / 100)
unidades_producidas = int(materia_efectiva / ratio_optimo)
desperdicio = cant_materia - (unidades_producidas * ratio_optimo)

# Visualización del proceso por etapas
st.header("🔄 Flujo del Proceso Industrial")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 1. Entrada: Materia Prima")
    st.image(img_materia, use_container_width=True)
    st.metric(label="Ingreso de Recursos", value=f"{cant_materia} Unidades")

with col2:
    st.markdown("### 2. Transformación")
    st.image(img_proceso, use_container_width=True)
    st.metric(label="Eficiencia de Planta", value=f"{eficiencia_maquinaria}%")

with col3:
    st.markdown("### 3. Salida: Producto Final")
    st.image(img_producto, use_container_width=True)
    st.metric(label="Producto Obtencion", value=f"{unidades_producidas} {producto_nombre}")

st.divider()

# Botón de simulación e informe
if st.button("🚀 Ejecutar Análisis de Planta"):
    with st.spinner("Procesando materia prima y analizando métricas de rendimiento..."):
        time.sleep(1)

    st.header("📊 Diagnóstico y Detección de Problemas")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.metric("Total Producido", f"{unidades_producidas} unidades")
        st.metric("Desperdicio Estimado", f"{desperdicio:.1f} unidades")

    with col_b:
        # Detección de problemas e ineficiencias
        if eficiencia_maquinaria < 60:
            st.error("⚠️ **Problema Crítico:** Falta de mantenimiento u obsolescencia en la maquinaria. Se está perdiendo gran parte del recurso en la transformación.")
        elif desperdicio > (cant_materia * 0.35):
            st.warning("⚠️ **Problema Detectado:** Exceso en el consumo de materia prima. La tasa de merma/desperdicio es demasiado alta.")
        else:
            st.success("✅ **Proceso Optimizado:** La planta opera con niveles adecuados de rendimiento y bajo desperdicio.")

    st.subheader("💡 Recomendaciones del Ingeniero")
    if eficiencia_maquinaria < 60:
        st.info("• Aplicar mantenimiento preventivo a los equipos.\n• Capacitar al personal operario.")
    elif desperdicio > (cant_materia * 0.35):
        st.info("• Ajustar los parámetros de corte/fundición para reducir mermas.\n• Reutilizar los desperdicios en un modelo de economía circular.")
    else:
        st.info("• Mantener los estándares actuales y monitorear indicadores clave (KPIs).")
