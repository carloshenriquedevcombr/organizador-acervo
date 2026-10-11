import hashlib
from collections import defaultdict
from pathlib import Path

from src.models.database import (
    session,
    ArquivoMetadata
)


def calcular_hash(caminho_arquivo):
    """
    Calcula SHA256 do arquivo.
    """

    sha256 = hashlib.sha256()

    try:

        with open(caminho_arquivo, "rb") as arquivo:

            while True:

                bloco = arquivo.read(1024 * 1024)

                if not bloco:
                    break

                sha256.update(bloco)

        return sha256.hexdigest()

    except Exception as erro:

        print(
            f"ERRO HASH: {caminho_arquivo}"
        )

        print(erro)

        return None


def localizar_duplicados():

    print()
    print("=" * 60)
    print("LOCALIZANDO DUPLICADOS")
    print("=" * 60)
    print()

    arquivos = session.query(
        ArquivoMetadata
    ).all()

    print(
        f"Arquivos carregados: {len(arquivos):,}"
    )

    # ---------------------------------
    # Agrupa por tamanho
    # ---------------------------------

    grupos_tamanho = defaultdict(list)

    for arquivo in arquivos:

        try:

            tamanho = int(
                arquivo.tamanho
            )

            grupos_tamanho[
                tamanho
            ].append(arquivo)

        except:
            pass

    candidatos = []

    for tamanho, grupo in grupos_tamanho.items():

        if len(grupo) > 1:

            candidatos.extend(grupo)

    print(
        f"Candidatos: {len(candidatos):,}"
    )

    # ---------------------------------
    # HASH
    # ---------------------------------

    grupos_hash = defaultdict(list)

    contador = 0

    for arquivo in candidatos:

        contador += 1

        if contador % 500 == 0:

            print(
                f"{contador:,} hashes calculados..."
            )

        caminho = arquivo.caminho_origem

        if not Path(caminho).exists():
            continue

        hash_arquivo = calcular_hash(
            caminho
        )

        if hash_arquivo:

            grupos_hash[
                hash_arquivo
            ].append(arquivo)

    duplicados = []

    for hash_arquivo, grupo in grupos_hash.items():

        if len(grupo) > 1:

            original = grupo[0]

            for duplicado in grupo[1:]:

                duplicados.append({

                    "hash":
                    hash_arquivo,

                    "arquivo_original":
                    original.caminho_origem,

                    "arquivo_duplicado":
                    duplicado.caminho_origem,

                    "tamanho":
                    original.tamanho
                })

    print()
    print(
        f"DUPLICADOS ENCONTRADOS: {len(duplicados):,}"
    )

    return duplicados
