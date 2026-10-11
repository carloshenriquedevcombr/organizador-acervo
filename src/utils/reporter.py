import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

import pandas as pd

from src.models.database import (
    session,
    ArquivoMetadata
)


def bytes_para_gb(valor):

    return round(
        valor / (1024 * 1024 * 1024),
        2
    )


def gerar_relatorio_csv():

    arquivos = session.query(
        ArquivoMetadata
    ).all()

    dados = []

    for arquivo in arquivos:

        try:
            tamanho = int(
                arquivo.tamanho
            )
        except:
            tamanho = 0

        dados.append({
            "nome_original": arquivo.nome_original,
            "novo_nome": arquivo.novo_nome,
            "categoria": arquivo.categoria,
            "extensao": arquivo.extensao,
            "tamanho_bytes": tamanho,
            "caminho_origem": arquivo.caminho_origem,
            "caminho_destino": arquivo.caminho_destino
        })

    df = pd.DataFrame(dados)

    # ==================================
    # CSV COMPLETO
    # ==================================

    arquivo_saida = "relatorio_acervo.csv"

    df.to_csv(
        arquivo_saida,
        index=False,
        encoding="utf-8-sig"
    )

    # ==================================
    # RESUMO POR CATEGORIA
    # ==================================

    resumo = (
        df.groupby("categoria")
        .agg(
            quantidade=("categoria", "count"),
            tamanho_total=("tamanho_bytes", "sum")
        )
        .sort_values(
            by="tamanho_total",
            ascending=False
        )
    )

    print()
    print("=" * 60)
    print("RESUMO POR CATEGORIA")
    print("=" * 60)
    print()

    for categoria, linha in resumo.iterrows():

        tamanho_gb = bytes_para_gb(
            linha["tamanho_total"]
        )

        print(
            f"{categoria:<20}"
            f"{linha['quantidade']:>10,} arquivos"
            f"   {tamanho_gb:>10,.2f} GB"
        )

    print()
    print("=" * 60)
    print()

    total_gb = bytes_para_gb(
        df["tamanho_bytes"].sum()
    )

    print(
        f"TOTAL DO ACERVO: {total_gb:,.2f} GB"
    )

    print()
    print(
        f"CSV GERADO: {arquivo_saida}"
    )
    print()


if __name__ == "__main__":
    gerar_relatorio_csv()
