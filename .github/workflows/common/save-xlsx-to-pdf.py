import pandas as pd
import pdfkit

df = pd.read_excel("Input List/Full Band/Input List.xlsx")
df.to_html("Input List/Full Band/Input List.html")
pdfkit.from_file("Input List/Full Band/Input List.html", "Input List/Full Band/Input List.pdf")