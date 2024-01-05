from fpdf import FPDF
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.image('shirtificate.png', 10,70,w=190)
pdf.set_text_color(255,255,255)
pdf.set_font("helvetica", "B", 24)

pdf.cell(0,214,"I took cs50",align="C")

pdf.output("new2.pdf")