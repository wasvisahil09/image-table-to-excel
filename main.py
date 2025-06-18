from img2table.ocr import TesseractOCR
from img2table.document import Image

# --- Configuration ---
# You NEED to define the 'src' variable with the path to your image file.
# Replace 'path/to/your/image.png' with the actual path to your image.
src = "/workspaces/image-table-to-excel/image/image copy 2.png" # <<<--- IMPORTANT: SET YOUR IMAGE PATH HERE

# Optional: Define the output Excel file path
output_excel_path = "table.xlsx"

# Instantiation of OCR
ocr = TesseractOCR(n_threads=1, lang="eng")

# Instantiation of document (an image in this case)
# Removed 'dpi=200' as it's not a valid argument for Image.__init__()
doc = Image(src) # <<<--- CORRECTED LINE

# Table extraction
extracted_tables = doc.extract_tables(ocr=ocr,
                                      implicit_rows=True,
                                      borderless_tables=False,
                                      min_confidence=50)

# --- Post-extraction Actions ---

# 1. Print information about extracted tables (optional)
print(f"Found {len(extracted_tables)} table(s) in '{src}'.")
for i, table in enumerate(extracted_tables):
    num_rows = len(table.content) if table.content else 0
    num_cols = len(table.content[0]) if table.content and len(table.content) > 0 else 0
    print(f"Table {i+1}: Bbox={table.bbox}, Rows={num_rows}, Columns={num_cols}")

# 2. Export the extracted tables to an Excel file
doc.to_xlsx(output_excel_path, ocr=ocr)

print(f"All tables from '{src}' exported to '{output_excel_path}'.")