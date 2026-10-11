def classificar_arquivo(arquivo_meta):

    caminho = arquivo_meta["caminho_completo"].lower()
    extensao = arquivo_meta["extensao"].lower()

    # ==========================================
    # RELIGIÃO (PRIORIDADE ALTA)
    # ==========================================

    if (
        "igreja" in caminho
        or "biblia" in caminho
        or "bíblia" in caminho
        or "sermao" in caminho
        or "sermão" in caminho
        or "pregacao" in caminho
        or "pregação" in caminho
        or "evangelho" in caminho
        or "jesus" in caminho
        or "pastor" in caminho
        or "culto" in caminho
        or "gospel" in caminho
    ):
        return "RELIGIAO"

    # ==========================================
    # ESTUDOS (PRIORIDADE ALTA)
    # ==========================================

    elif (
        "curso" in caminho
        or "faculdade" in caminho
        or "estudo" in caminho
        or "estudos" in caminho
        or "udemy" in caminho
        or "alura" in caminho
        or "treinamento" in caminho
        or "certificacao" in caminho
        or "certificação" in caminho
        or "aula" in caminho
    ):
        return "ESTUDOS"

    # ==========================================
    # PROGRAMAÇÃO
    # ==========================================

    elif extensao in [

        ".py",
        ".pyw",
        ".pyi",
        ".pyc",

        ".js",
        ".ts",
        ".jsx",
        ".tsx",

        ".html",
        ".css",

        ".json",
        ".xml",
        ".yaml",
        ".yml",

        ".sql",

        ".java",
        ".c",
        ".cpp",
        ".cs",

        ".php",

        ".ipynb",

        ".md",

        ".sh",
        ".bat",
        ".ps1",

        ".dll",
        ".lib",

        ".so",

        ".toml",
        ".cfg",
        ".ini",

        ".prisma",

        ".asm",
        ".obj",

        ".npy",
        ".npz"

    ]:
        return "PROGRAMACAO"

    # ==========================================
    # DESIGN GRÁFICO
    # ==========================================

    elif extensao in [

        ".cdr",
        ".cdrx",
        ".cdrz",

        ".ai",
        ".eps",

        ".psd",

        ".indd",

        ".svg"

    ]:
        return "DESIGN"

    # ==========================================
    # FONTES
    # ==========================================

    elif extensao in [

        ".ttf",
        ".otf",
        ".woff",
        ".woff2"

    ]:
        return "FONTES"

    # ==========================================
    # BANCO DE DADOS
    # ==========================================

    elif extensao in [

        ".db",
        ".sqlite",
        ".sqlite3",
        ".mdb",
        ".accdb"

    ]:
        return "BANCO_DADOS"

    # ==========================================
    # DOCUMENTOS
    # ==========================================

    elif extensao in [

        ".pdf",
        ".doc",
        ".docx",
        ".odt",
        ".txt",
        ".rtf"

    ]:
        return "DOCUMENTOS"

    # ==========================================
    # FINANCEIRO
    # ==========================================

    elif extensao in [

        ".xls",
        ".xlsx",
        ".xlsm",
        ".csv",
        ".ods"

    ]:
        return "FINANCEIRO"

    # ==========================================
    # APRESENTAÇÕES
    # ==========================================

    elif extensao in [

        ".ppt",
        ".pptx"

    ]:
        return "TRABALHO"

    # ==========================================
    # IMAGENS
    # ==========================================

    elif extensao in [

        ".jpg",
        ".jpeg",
        ".png",
        ".bmp",
        ".webp",
        ".tiff",
        ".tif",
        ".heic",
        ".jfif",
        ".avif"

    ]:
        return "IMAGENS"

    # ==========================================
    # RAW FOTOGRÁFICO
    # ==========================================

    elif extensao in [

        ".cr2",
        ".cr3",
        ".nef",
        ".arw",
        ".dng",
        ".raf"

    ]:
        return "FAMILIA"

    # ==========================================
    # VÍDEOS
    # ==========================================

    elif extensao in [

        ".mp4",
        ".mov",
        ".avi",
        ".mkv",
        ".wmv",
        ".3gp"

    ]:
        return "VIDEOS"

    # ==========================================
    # ÁUDIO
    # ==========================================

    elif extensao in [

        ".mp3",
        ".wav",
        ".flac",
        ".aac",
        ".m4a"

    ]:
        return "AUDIO"

    # ==========================================
    # BACKUP / COMPACTADOS
    # ==========================================

    elif extensao in [

        ".zip",
        ".rar",
        ".7z",
        ".gz"

    ]:
        return "BACKUP"

    # ==========================================
    # SOFTWARE
    # ==========================================

    elif extensao in [

        ".exe",
        ".msi",
        ".msix"

    ]:
        return "SOFTWARE"

    # ==========================================
    # SEM EXTENSÃO
    # ==========================================

    elif extensao == "":
        return "OUTROS"

    # ==========================================
    # PADRÃO
    # ==========================================

    return "OUTROS"
