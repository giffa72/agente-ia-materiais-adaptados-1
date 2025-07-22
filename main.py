from fpdf import FPDF
import os

def gerar_material_adaptado(tema, serie, laudo):
    # Cria pasta de saída se não existir
    os.makedirs("saida", exist_ok=True)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)

    pdf.cell(200, 10, txt="Material Adaptado de Química", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Tema: {tema}")
    pdf.multi_cell(0, 10, f"Série: {serie}")
    pdf.multi_cell(0, 10, f"Laudo do aluno: {laudo}")
    pdf.ln(5)

    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Atividade 1:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, "Observe o desenho abaixo e pinte a opção correta.")
    pdf.image("fig1.png", x=30, y=pdf.get_y(), w=150)
    pdf.ln(65)
    pdf.cell(0, 10, "A) Estado sólido    B) Estado líquido    C) Estado gasoso", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Atividade 2:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, "Complete: A água muda de estado quando ________.")

    pdf.output("saida/materia_adaptada.pdf")