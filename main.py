from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm",format="A4")

pdf.add_page()
pdf.set_font(family="Times",style="B",size=12)
pdf.cell(w=0,h=12,txt="Vishal here",align="L",ln=1)

pdf.add_page()
pdf.set_font(family="Arial",style="B",size=12)
pdf.cell(w=0,h=12,txt="Vishal There",align="L",ln=1)
pdf.output("output.pdf")