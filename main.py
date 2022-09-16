from PyPDF2 import PdfFileReader, PdfFileWriter
import os
from rich import traceback

traceback.install()

class PDF:

    def get_files():
        files = []
        directory = os.getcwd() + '\\pdf_files'
        for file in os.listdir(directory):
            if file.endswith('.pdf'):
                files.append(directory + '\\' + file )
        return files


    def merge_pdf(path, output):
        pdf_writer = PdfFileWriter()
        
        for file in path:
            pdf_reader = PdfFileReader(file)

            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))

        with open(output, 'wb') as out:
            pdf_writer.write(out)


class Main:

    if __name__ == '__main__':
        # print(get_files())
        # get the directory needed
        merge_directory = os.getcwd() + '\\merged_pdfs'
        PDF.merge_pdf(PDF.get_files(), merge_directory + '\\merged.pdf')