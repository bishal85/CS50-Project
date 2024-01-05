from fpdf import FPDF
class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10,70,190)
        self.set_font("helvetica","", 48)
        self.cell(0,57,"CS50 shirtificate",align="C")
        self.ln(20)

def main():
    string=input(" ")

    string1(string)
def string1(b):
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font("helvetica",size=24)



    pdf.set_text_color(255,255,255)
    pdf.cell(0,214,f"{b} took cs50",align="C")
    pdf.output("shirtificate.pdf")
if __name__=="__main__":
    main()
