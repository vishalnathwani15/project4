from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm",format="A4")
pdf.set_auto_page_break(auto=False,margin=0)
df = pd.read_csv("topics.csv")

for index ,row in df.iterrows():
     pdf.add_page()
     pdf.set_font(family="Times",style="B",size=24)
     pdf.set_text_color(0,0,0)
     pdf.cell(w=0,h=12,txt=row["Topic"],align="L",ln=1)
     pdf.line(10,22,200,22)
     # this is for footer
     pdf.ln(260)
     pdf.set_font(family="Times",size=10)
     pdf.set_text_color(180,180,180)
     pdf.cell(w=0,h=12,txt=row["Topic"],align="R")
     #multiple page creation
     for i in range(row["Pages"]-1):
          pdf.add_page()
          # this is for footer
          pdf.ln(272)
          pdf.set_font(family="Times",size=10)
          pdf.set_text_color(180,180,180)
          pdf.cell(w=0,h=12,txt=row["Topic"],align="R")


# pdf.add_page()
# pdf.set_font(family="Arial",style="B",size=12)
# pdf.cell(w=0,h=12,txt="Vishal There",align="L",ln=1)
pdf.output("output1.pdf")