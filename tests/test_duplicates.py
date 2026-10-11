import pytest

from src.core.duplicates import calcular_hash, localizar_duplicados
from src.models.database import ArquivoMetadata, init_db, session


@pytest.fixture
def banco_limpo():
    init_db()
    session.query(ArquivoMetadata).delete()
    session.commit()
    yield session
    session.query(ArquivoMetadata).delete()
    session.commit()


def _registrar(caminho):
    session.add(
        ArquivoMetadata(
            nome_original=caminho.name,
            caminho_origem=str(caminho),
            extensao=caminho.suffix,
            tamanho=str(caminho.stat().st_size),
        )
    )


def test_hash_igual_para_conteudo_igual(tmp_path):
    a = tmp_path / "a.txt"
    b = tmp_path / "b.txt"
    a.write_text("mesmo conteudo")
    b.write_text("mesmo conteudo")
    assert calcular_hash(a) == calcular_hash(b)


def test_hash_de_arquivo_inexistente_retorna_none(tmp_path):
    assert calcular_hash(tmp_path / "nao_existe.bin") is None


def test_localiza_duplicados_por_hash(tmp_path, banco_limpo):
    original = tmp_path / "ferias.jpg"
    copia = tmp_path / "copia" / "ferias (1).jpg"
    mesmo_tamanho = tmp_path / "outra.jpg"
    unico = tmp_path / "unico.txt"

    copia.parent.mkdir()
    original.write_bytes(b"foto ficticia 123")
    copia.write_bytes(b"foto ficticia 123")
    mesmo_tamanho.write_bytes(b"foto ficticia 999")  # mesmo tamanho, outro conteúdo
    unico.write_bytes(b"x")

    for caminho in (original, copia, mesmo_tamanho, unico):
        _registrar(caminho)
    session.commit()

    duplicados = localizar_duplicados()

    assert len(duplicados) == 1
    par = duplicados[0]
    assert {par["arquivo_original"], par["arquivo_duplicado"]} == {str(original), str(copia)}
    assert par["hash"] == calcular_hash(original)
