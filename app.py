import streamlit as st
from main import gerar_material_adaptado
import os

st.set_page_config(page_title="Agente IA - Materiais Adaptados", layout="centered")

st.title("🧠 Agente de IA para Materiais Adaptados")

tema = st.text_input("📘 Tema da Matéria")
serie = st.text_input("🏫 Série/Ano Escolar")
laudo = st.text_area("🧾 Tipo de Laudo do Aluno")

if st.button("📄 Gerar Material PDF"):
    if tema and serie and laudo:
        gerar_material_adaptado(tema, serie, laudo)
        pdf_path = "saida/materia_adaptada.pdf"
        if os.path.exists(pdf_path):
            with open(pdf_path, "rb") as f:
                st.success("✅ PDF gerado com sucesso!")
                st.download_button("📥 Baixar PDF", f, file_name="material_adaptado.pdf")
    else:
        st.warning("⚠️ Preencha todos os campos antes de gerar o material.")