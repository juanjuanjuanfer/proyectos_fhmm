import streamlit as st
import os


st.set_page_config(page_title="Página principal", page_icon=":floppy_disk:", layout="wide", initial_sidebar_state="collapsed")

st.markdown("## Proyectos disponibles")

# Get all files in the pages directory
pages_dir = "pages"
if not os.path.exists(pages_dir):
    st.error("No se encontró el directorio 'pages'. Favor de notificar al administrador.")
else:
    page_files = [f for f in os.listdir(pages_dir) if f.endswith(".py")]
    
    if not page_files:
        st.warning("No pages found inside 'pages' directory.")
    else:
        for file in sorted(page_files):
            page_name = file.replace(".py", "").replace("_", " ").title()
            if st.button(page_name):
                file = f"pages/{file}"
                st.switch_page(file)

st.markdown("---")
st.info("Has click en una página para ver los datos.")