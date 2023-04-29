import PyPDF2

def getFields(pdf_path):
    # Open the PDF file in read-binary mode
    pdf_file = open(pdf_path, 'rb')

    # Create a PdfReader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Get all the form fields in the PDF file
    form_fields = pdf_reader.get_fields()

    return form_fields
