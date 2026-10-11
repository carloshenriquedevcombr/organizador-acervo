from pathlib import Path

from config import (
    PASTA_DESTINO,
    DRY_RUN
)

from src.core.scanner import escanear_diretorio
from src.core.classifier import classificar_arquivo
from src.core.renamer import gerar_novo_nome

from src.models.database import (
    session,
    ArquivoMetadata,
    init_db
)


def rodar_dam():

    # Garante que a tabela existe (banco novo)
    init_db()

    print("\nINICIANDO VARREDURA...\n")

    if DRY_RUN:
        print("MODO DRY-RUN: nenhum arquivo será copiado.\n")

    total = 0

    for meta in escanear_diretorio():

        total += 1

        categoria = classificar_arquivo(meta)

        novo_nome = gerar_novo_nome(
            meta,
            categoria
        )

        pasta_destino = (
            Path(PASTA_DESTINO)
            / categoria
        )

        caminho_final = (
            pasta_destino
            / novo_nome
        )

        if total % 1000 == 0:

            print(
                f"{total:,} arquivos processados..."
            )

        # EVITA DUPLICAÇÃO NO BANCO

        existe = session.query(
            ArquivoMetadata
        ).filter(
            ArquivoMetadata.caminho_origem
            == meta["caminho_completo"]
        ).first()

        if existe:
            continue

        if not DRY_RUN:

            import shutil

            # Só cria pastas no destino quando não é simulação
            pasta_destino.mkdir(
                parents=True,
                exist_ok=True
            )

            shutil.copy2(
                meta["caminho_completo"],
                str(caminho_final)
            )

        registro = ArquivoMetadata(
            nome_original=meta["nome"],
            novo_nome=novo_nome,
            categoria=categoria,
            caminho_origem=meta["caminho_completo"],
            caminho_destino=str(caminho_final),
            extensao=meta["extensao"],
            tamanho=str(meta["tamanho"])
        )

        session.add(registro)

        if total % 1000 == 0:
            session.commit()

    session.commit()

    print("\nPROCESSAMENTO FINALIZADO\n")

    print(
        f"TOTAL PROCESSADO: {total:,}"
    )


if __name__ == "__main__":
    rodar_dam()
