import docx

def convert_to_doc(filename, text, output_dir):
    if output_dir[-1] != '/':
        output_dir += '/'

    doc = docx.Document()
    doc.add_paragraph(text)
    doc.save(output_dir + filename)
