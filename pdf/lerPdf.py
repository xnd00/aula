## pip install PyPDF2
import PyPDF2

# Abra o arquivo PDF em modo de leitura binária
with open('seu_arquivo.pdf', 'rb') as pdf_file:
    # Crie um objeto PdfReader
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    
    # Verifique se o arquivo PDF possui pelo menos uma página
    if pdf_reader.numPages > 0:
        # Leitura de todas as páginas e concatenação do texto
        texto_completo = ''
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            texto_completo += page.extractText()
        
        # Imprime o texto completo
        print(texto_completo)
    else:
        print("O arquivo PDF está vazio ou não possui páginas.")
