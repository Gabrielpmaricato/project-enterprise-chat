import fitz  # PyMuPDF

def ler_pdf(caminho_pdf):
    texto_completo = ""
    
    # Abre o arquivo PDF
    with fitz.open(caminho_pdf) as doc:
        for pagina_num, pagina in enumerate(doc, start=1):
            texto = pagina.get_text()
            texto_completo += f"\n--- Página {pagina_num} ---\n{texto}"
    
    return texto_completo

# Exemplo de uso
caminho = "C:/Users/Gabriel/OneDrive/Área de Trabalho/reportlab-sample.pdf"
conteudo = ler_pdf(caminho)
print(conteudo)
