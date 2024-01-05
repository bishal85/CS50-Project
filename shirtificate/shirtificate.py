from fpdf import FPDF
class PDF(FPDF):

    def Header(self):
        self.add_page()
        self.image('shirtificate.png', 10,70,w=190)
        self.set_font("helvetica","", 48)
        self.cell(0,57,"CS50 shirtificate",align="C")
        self.ln(20)

def main():
    string=input(" ")

    string1(string)
def string1(b):
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="A4")


    pdf.set_text_color(255,255,255)

    pdf.set_font("helvetica", "B", 24)
    pdf.cell(0,214,f"{b} took cs50",align="C")
    pdf.output("string.pdf")
if __name__="__main__":
    main()
