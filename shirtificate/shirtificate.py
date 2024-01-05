from fpdf import FPDF
class PDF(FPDF):

    def Header(self):
        self.add_page()
        self.image('shirtificate.png', 10,70,w=190)
        self.set_font("helvetica","", 48)
        self.cell(0,57,"CS50 shirtificate",align="C")
        self.ln(20)

def string1():
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.image('shirtificate.png', 10,70,w=190)

    pdf.set_font("helvetica", "B", 16)
    pdf.cell(0,214,"I took cs50",align="C")

    pdf.output("he2.pdf")
