from fpdf import FPDF
pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.image('shirtificate.png', 10,70,w=190)
pdf.set_font("helvetica","", 47)

pdf.cell(0,57,"CS50 shirtificate",align="C")
pdf.set_text_color(255,255,255)
pdf.set_font("helvetica", "B", 24)

pdf.output("hello2.pdf")
