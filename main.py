from PyPDF2 import PdfFileReader, PdfFileWriter
import os
from rich import traceback
from rich.console import Console
from rich.markdown import Markdown

console = Console()
traceback.install()



MARKDOWN = """
# PDF Merger

## Steps

- 1 Place all the pdf files in the pdf_files folder
- 2 Run the script
- 3 Enter the directory path name (if left blank, the default path will be used)

"""
md = Markdown(MARKDOWN)
console.print(md)


class PDF:

    def get_files():
        files = []
        directory = os.getcwd() + '\\pdf_files'
        for file in os.listdir(directory):
            if file.endswith('.pdf'):
                files.append(directory + '\\' + file)
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
        

       
        path_choice = console.input('\n[bold cyan]Where do you want to export the merged file?\nIf nothing is selected, the file will be exported to merged_pdfs directory.\n')
        # default directory
        default_directory = os.getcwd() + '\\merged_pdfs'

        if (path_choice == ''):
            PDF.merge_pdf(PDF.get_files(), default_directory + '\\merged.pdf')
            console.print(f'[bold cyan]File exported to [green]{default_directory}[/green] directory.')
        else:
            if not os.path.exists(path_choice):
                os.makedirs(path_choice)
                PDF.merge_pdf(PDF.get_files(), path_choice + '\\merged.pdf')
                console.print(f'[bold cyan]File exported to [green] {path_choice} [/green]directory.[/bold cyan]')
            else:
                PDF.merge_pdf(PDF.get_files(), path_choice + '\\merged.pdf')
                console.print(f'[bold cyan]File exported to [green] {path_choice} [/green]directory.[/bold cyan]')
