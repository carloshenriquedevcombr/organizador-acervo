import os
import sys
import tempfile
from pathlib import Path

# Banco temporário para os testes (nunca usa o banco real)
_PASTA_TESTE = Path(tempfile.mkdtemp(prefix="acervo_testes_"))
os.environ["ACERVO_BANCO"] = str(_PASTA_TESTE / "teste.db")
os.environ["ACERVO_ORIGEM"] = str(_PASTA_TESTE / "origem")
os.environ["ACERVO_DESTINO"] = str(_PASTA_TESTE / "destino")
os.environ["ACERVO_DRY_RUN"] = "1"

ROOT_DIR = Path(__file__).resolve().parents[1]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
