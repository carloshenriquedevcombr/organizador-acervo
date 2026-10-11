from datetime import datetime

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    DateTime
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from config import BANCO_DADOS

# ==================================================
# CONFIGURAÇÃO DO SQLITE
# ==================================================

engine = create_engine(
    f"sqlite:///{BANCO_DADOS}",
    echo=False
)

Base = declarative_base()

# ==================================================
# TABELA PRINCIPAL
# ==================================================

class ArquivoMetadata(Base):
    __tablename__ = "arquivos"

    id = Column(Integer, primary_key=True)

    nome_original = Column(String(500))
    novo_nome = Column(String(500))

    categoria = Column(String(100))

    caminho_origem = Column(String(2000))
    caminho_destino = Column(String(2000))

    extensao = Column(String(20))

    tamanho = Column(String(50))

    hash_arquivo = Column(String(128))

    data_processamento = Column(
        DateTime,
        default=datetime.utcnow
    )

# ==================================================
# CRIAÇÃO DO BANCO
# ==================================================

def init_db():
    Base.metadata.create_all(engine)

# ==================================================
# SESSÃO
# ==================================================

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

session = SessionLocal()

# ==================================================
# TESTE
# ==================================================

if __name__ == "__main__":
    init_db()
    print("Banco criado com sucesso.")
