from fpdf import FPDF


def main():
    string=input(" ")

    string1(string)
def string1(b):
    pdf = FPDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.image("./shirtificate.png", 10,70,190)
    pdf.set_font("helvetica","", 48)
    pdf.cell(0,57,"CS50 shirtificate",align="C")
    pdf.set_font("helvetica",size=24)



    pdf.set_text_color(0,0,255)
    pdf.cell(0,214,f"{b} took cs50",align="C")
    pdf.output("b.pdf")
if __name__=="__main__":
    main()
