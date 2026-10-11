import os
from pathlib import Path

# ==================================================
# CONFIGURAÇÕES GERAIS DO PROJETO
# ==================================================
# Os caminhos abaixo são apenas exemplos. Ajuste aqui ou
# sobrescreva com variáveis de ambiente:
#   ACERVO_ORIGEM, ACERVO_DESTINO, ACERVO_BANCO, ACERVO_DRY_RUN

# Pasta onde estão os arquivos originais
PASTA_ORIGEM = Path(os.environ.get("ACERVO_ORIGEM", r"E:\ORIGEM"))

# Pasta onde o sistema criará a estrutura organizada
PASTA_DESTINO = Path(os.environ.get("ACERVO_DESTINO", r"E:\DESTINO"))

# Banco SQLite
BANCO_DADOS = os.environ.get("ACERVO_BANCO", "arquivo_digital.db")

# MODO DE SEGURANÇA
# True = apenas simulação
# False = copia os arquivos de verdade
DRY_RUN = os.environ.get("ACERVO_DRY_RUN", "1").strip().lower() not in (
    "0", "false", "nao", "não", "no"
)

# Categorias principais
CATEGORIAS = [
    "FAMILIA",
    "PESSOAL",
    "TRABALHO",
    "ESTUDOS",
    "FINANCEIRO",
    "RELIGIAO",
    "SOFTWARE",
    "BACKUP",
    "IMAGENS",
    "VIDEOS",
    "AUDIO",
    "DOCUMENTOS",
    "OUTROS",
    "_REVISAO_MANUAL"
]

# Extensões suportadas
EXTENSOES_SUPORTADAS = {
    ".pdf", ".doc", ".docx", ".odt", ".txt", ".rtf",
    ".xls", ".xlsx", ".csv", ".ods",
    ".ppt", ".pptx",
    ".jpg", ".jpeg", ".png", ".tiff", ".webp", ".bmp",
    ".cr2", ".cr3", ".nef", ".arw", ".dng", ".raf",
    ".mp4", ".mov", ".avi", ".mkv", ".wmv",
    ".mp3", ".wav", ".flac", ".aac",
    ".zip", ".rar", ".7z", ".exe", ".msi"
}
