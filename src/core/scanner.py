import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from pathlib import Path
from datetime import datetime

from config import PASTA_ORIGEM


def extrair_metadados(caminho_arquivo):
    """
    Extrai informações básicas do arquivo.
    """

    try:
        stats = caminho_arquivo.stat()

        return {
            "nome": caminho_arquivo.name,
            "extensao": caminho_arquivo.suffix.lower(),
            "caminho_completo": str(caminho_arquivo),
            "data_criacao": datetime.fromtimestamp(
                stats.st_ctime
            ),
            "data_modificacao": datetime.fromtimestamp(
                stats.st_mtime
            ),
            "tamanho": stats.st_size
        }

    except Exception as erro:
        print(
            f"ERRO ao ler arquivo: {caminho_arquivo}"
        )
        print(erro)

        return None


def escanear_diretorio():
    """
    Escaneia a pasta origem inteira.
    """

    pasta = Path(PASTA_ORIGEM)

    if not pasta.exists():
        raise FileNotFoundError(
            f"Pasta não encontrada: {pasta}"
        )

    contador = 0

    for arquivo in pasta.rglob("*"):

        if arquivo.is_file():

            meta = extrair_metadados(
                arquivo
            )

            if meta:

                contador += 1

                if contador % 1000 == 0:

                    print(
                        f"{contador:,} arquivos lidos..."
                    )

                yield meta


if __name__ == "__main__":

    print(
        "\nINICIANDO TESTE DO SCANNER\n"
    )

    total = 0

    for arquivo in escanear_diretorio():

        total += 1

        if total <= 5:
            print(arquivo)

    print(
        f"\nTOTAL ENCONTRADO: {total:,} arquivos"
    )
