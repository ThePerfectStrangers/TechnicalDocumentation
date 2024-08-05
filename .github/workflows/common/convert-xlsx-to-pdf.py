import pandas as pd
import pdfkit

# Read Excel file into a DataFrame
df = pd.read_excel("Input List/Full Band/Input List.xlsx")

# Convert DataFrame to HTML
html_content = df.to_html()

# Save HTML content as a PDF
pdfkit.from_string(html_content, "Input List/Full Band/Input List2.pdf")
