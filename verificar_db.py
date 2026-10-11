from collections import Counter

from src.models.database import (
    session,
    ArquivoMetadata
)

arquivos = session.query(
    ArquivoMetadata
).all()

contador_categoria = Counter()
contador_extensao = Counter()

for arquivo in arquivos:

    contador_categoria[
        arquivo.categoria
    ] += 1

    if arquivo.categoria == "OUTROS":

        contador_extensao[
            arquivo.extensao
        ] += 1

print("\n===== CATEGORIAS =====\n")

for categoria, total in sorted(
    contador_categoria.items(),
    key=lambda x: x[1],
    reverse=True
):
    print(
        f"{categoria:<20} {total:>10,}"
    )

print("\n===== TOP 50 EXTENSÕES EM OUTROS =====\n")

for ext, total in contador_extensao.most_common(50):

    print(
        f"{ext:<15} {total:>10,}"
    )
