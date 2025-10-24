import pdfplumber
import re

pdf_path = "ECM516.pdf"

with pdfplumber.open(pdf_path) as pdf:
    texto = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

print("Texto extraído com sucesso.\n")

trecho_match = re.search(
    r"bibliografia básica\s*(.*?)\s*informações\s+sobre\s+provas\s+e\s+trabalhos",
    texto,
    re.IGNORECASE | re.DOTALL
)

trecho = trecho_match.group(1).strip() if trecho_match else None

print("Trecho desejado:\n\n\n\n", trecho if trecho else "Não encontrado")

codigo_match = re.search(r"([A-Z]{2,}\d{3,})\s*Course\b", trecho, re.IGNORECASE)
codigo = codigo_match.group(1) if codigo_match else None

curso_match = re.search(r"Materia:\s*(?:\n\s*)?(.+)", trecho, re.IGNORECASE)
curso = curso_match.group(1).strip() if curso_match else None

print("Código da Disciplina:", codigo)
print("Curso:", curso)


