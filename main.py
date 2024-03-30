from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index,row in df.iterrows():


pdf.output("output.pdf")