from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from urllib.request import urlopen


def read_pdf(pdf_file):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdf_file)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    return content

pdf_file = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
output_string = read_pdf(pdf_file)
print(output_string)
pdf_file.close()

