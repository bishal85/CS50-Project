from fpdf import FPDF
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.image('shirtificate.png', 10,70,w=190)

pdf.set_font("helvetica", "B", 16)
pdf.cell(0,214,"I took cs50",align="C")

pdf.output("he2.pdf")
