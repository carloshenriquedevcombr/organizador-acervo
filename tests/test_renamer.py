from datetime import datetime

from src.core.renamer import gerar_novo_nome


def _meta(nome, extensao):
    return {
        "nome": nome,
        "extensao": extensao,
        "data_criacao": datetime(2019, 3, 7, 10, 30),
    }


def test_nome_padronizado_com_data_e_categoria():
    novo = gerar_novo_nome(_meta("contrato aluguel.pdf", ".pdf"), "DOCUMENTOS")
    assert novo == "2019-03-07_DOCUMENTOS_contrato aluguel.pdf"


def test_remove_caracteres_proibidos_no_windows():
    novo = gerar_novo_nome(_meta('foto:praia?.jpg', ".jpg"), "IMAGENS")
    assert novo == "2019-03-07_IMAGENS_foto_praia_.jpg"
