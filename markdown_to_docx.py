import subprocess
import tempfile
from pathlib import Path

def markdown_to_docx(markdown_text: str, output_path: str):
    """
    Converte uma string em Markdown para um arquivo .docx usando Pandoc.

    Requisitos:
    - pandoc instalado no sistema (https://pandoc.org)

    Args:
        markdown_text (str): Conteúdo em Markdown
        output_path (str): Caminho final do .docx
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".md", mode='w', encoding='utf-8') as tmp_md:
        tmp_md.write(markdown_text)
        tmp_md_path = tmp_md.name

    try:
        subprocess.run(["pandoc", tmp_md_path, "-o", output_path], check=True)
        print(f"✅ Arquivo .docx gerado em: {output_path}")
    except subprocess.CalledProcessError as e:
        print("❌ Erro ao gerar .docx com pandoc:", e)
    finally:
        Path(tmp_md_path).unlink()
