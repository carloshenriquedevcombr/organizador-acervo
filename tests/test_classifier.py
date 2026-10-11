import pytest

from src.core.classifier import classificar_arquivo


def _meta(caminho):
    from pathlib import PureWindowsPath
    return {
        "caminho_completo": caminho,
        "extensao": PureWindowsPath(caminho).suffix.lower(),
    }


@pytest.mark.parametrize(
    "caminho, esperado",
    [
        (r"E:\ORIGEM\fotos\IMG_0001.JPG", "IMAGENS"),
        (r"E:\ORIGEM\diversos\planilha_gastos.xlsx", "FINANCEIRO"),
        (r"E:\ORIGEM\diversos\relatorio.pdf", "DOCUMENTOS"),
        (r"E:\ORIGEM\camera\DSC_1234.NEF", "FAMILIA"),
        (r"E:\ORIGEM\musicas\faixa01.mp3", "AUDIO"),
        (r"E:\ORIGEM\instaladores\setup.exe", "SOFTWARE"),
        (r"E:\ORIGEM\projetos\script.py", "PROGRAMACAO"),
        (r"E:\ORIGEM\backup\antigo.zip", "BACKUP"),
        (r"E:\ORIGEM\sem_extensao", "OUTROS"),
        (r"E:\ORIGEM\diversos\arquivo.xyz", "OUTROS"),
    ],
)
def test_classifica_por_extensao(caminho, esperado):
    assert classificar_arquivo(_meta(caminho)) == esperado


def test_palavra_chave_na_pasta_tem_prioridade_sobre_extensao():
    # PDF dentro de uma pasta de curso vai para ESTUDOS, não DOCUMENTOS
    assert classificar_arquivo(_meta(r"E:\ORIGEM\Curso Python\apostila.pdf")) == "ESTUDOS"
    assert classificar_arquivo(_meta(r"E:\ORIGEM\Igreja\culto.mp4")) == "RELIGIAO"
