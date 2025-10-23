import pdfplumber
import re

pdf_path = "EAL406.pdf"

with pdfplumber.open(pdf_path) as pdf:
    texto = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

print("Texto extraído com sucesso.\n")

# Não remover espaços ainda, vamos fazer a regex mais flexível
trecho_match = re.search(
    r"bibliografia complementar\s*(.*?)\s*informações\s+sobre\s+provas\s+e\s+trabalhos",
    texto,
    re.IGNORECASE | re.DOTALL
)

trecho = trecho_match.group(1).strip() if trecho_match else None

print(texto)
print("Trecho desejado:\n\n\n\n", trecho if trecho else "Não encontrado")


# Normaliza (remove espaços duplos e quebras excessivas)


# # Expressões regulares corrigidas
# codigo_disciplina = re.search(r"Código\s+da\s+Disciplina\s*(?:\n\s*)?(.+)", texto, re.IGNORECASE)
# course_match = re.search(r"Course:\s*(?:\n\s*)?(.+)", texto, re.IGNORECASE)
# curso = course_match.group(1).strip() if course_match else None

# # Exibe resultados
# print("Código da Disciplina:", codigo_disciplina.group(1) if codigo_disciplina else "Não encontrado")
# print("\n\nCurso:", curso)


