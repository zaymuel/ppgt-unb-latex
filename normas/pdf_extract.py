from pypdf import PdfReader
import pathlib

def pdf_to_markdown_pypdf(pdf_path):
    """
    Extracts text from a PDF using pypdf and saves it as a Markdown file
    with the exact same base name as the original PDF.
    """
    try:
        # We wrap the input path in a Path object
        input_path_obj = pathlib.Path(pdf_path)
        
        # We create the output path by replacing the extension with .md
        md_path = input_path_obj.with_suffix('.md')
        
        reader = PdfReader(input_path_obj)
        extracted_text = []

        # Loop through all pages and extract text
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                extracted_text.append(f"## Page {i + 1}\n\n{text}\n")

        # Join the pages and save to the markdown file
        final_markdown = "\n".join(extracted_text)
        md_path.write_text(final_markdown, encoding='utf-8')
        
        print(f"Success! Saved to: {md_path}")

    except FileNotFoundError:
        print(f"Error: The file '{pdf_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # You only need to provide the input file now!
    input_file = "Normas_de_redacao_para_Dissertacoes_e_Teses_EM_TRANSPORTES_2023.pdf"
    
    pdf_to_markdown_pypdf(input_file)