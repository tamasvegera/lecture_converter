from fpdf import FPDF

def convert_to_pdf(filename, text, output_dir):
    if output_dir[-1] != '/':
        output_dir += '/'

    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('Arial', '', 'arial.ttf', uni=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 5, txt=text)
    pdf.output(output_dir + filename)
