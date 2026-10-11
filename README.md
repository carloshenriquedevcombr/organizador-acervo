# Organizador de Acervo Digital

Ferramenta em Python para colocar ordem em um HD bagunçado: varre todas as pastas,
classifica cada arquivo por categoria, propõe um nome padronizado com data e
categoria, encontra arquivos duplicados e gera um relatório em CSV.

## O problema

Anos de arquivos acumulados no mesmo disco: fotos do celular, planilhas, PDFs,
instaladores, backups, cursos, músicas. Tudo misturado, sem padrão de pastas e
sem padrão de nomes (`IMG_0001.jpg`, `documento final (2).pdf`, `novo.xlsx`...).
Com centenas de milhares de arquivos, organizar à mão não é viável, e é fácil
perder ou apagar algo importante no caminho.

## Como funciona

1. **Varredura** (`src/core/scanner.py`): percorre a pasta de origem
   recursivamente e coleta nome, extensão, tamanho e datas de cada arquivo.
2. **Classificação** (`src/core/classifier.py`): decide a categoria do arquivo.
   Palavras-chave no caminho têm prioridade (ex.: um PDF dentro de uma pasta
   `Curso` vai para `ESTUDOS`); depois vale a extensão (`.jpg` vai para `IMAGENS`,
   `.xlsx` para `FINANCEIRO`, `.zip` para `BACKUP` e assim por diante).
3. **Renomeação** (`src/core/renamer.py`): gera o nome no padrão
   `AAAA-MM-DD_CATEGORIA_nome-original.ext`, removendo caracteres inválidos no Windows.
4. **Registro** (`src/models/database.py`): grava tudo em um banco SQLite
   (origem, destino proposto, categoria, tamanho), sem registrar o mesmo arquivo duas vezes.
5. **Duplicados** (`src/core/duplicates.py`): agrupa por tamanho e só calcula o
   hash SHA-256 dos arquivos com tamanho repetido, o que poupa muito tempo em discos grandes.
6. **Relatório** (`src/utils/reporter.py`): exporta um CSV completo e mostra um
   resumo por categoria (quantidade e espaço ocupado).

## Segurança

- **Dry-run ligado por padrão.** No modo simulação nada é copiado e nenhuma pasta é
  criada no destino: o sistema só registra no banco o que *faria*. Assim dá para revisar
  o relatório antes de qualquer alteração.
- **Os originais nunca são movidos nem apagados.** Mesmo com o dry-run desligado, o
  programa apenas **copia** (`shutil.copy2`, preservando datas) para a pasta de destino.
- A detecção de duplicados só lista os pares encontrados; a decisão de apagar é sua.

## Stack

- Python 3.11+
- SQLAlchemy + SQLite (registro do acervo)
- pandas (relatório CSV e resumo)
- hashlib / pathlib (biblioteca padrão)
- pytest (testes)

## Como rodar

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Configure as pastas em `config.py` ou por variáveis de ambiente:

| Variável          | Padrão               | Descrição                                   |
|-------------------|----------------------|---------------------------------------------|
| `ACERVO_ORIGEM`   | `E:\ORIGEM`          | Pasta com os arquivos bagunçados            |
| `ACERVO_DESTINO`  | `E:\DESTINO`         | Onde a estrutura organizada será criada     |
| `ACERVO_BANCO`    | `arquivo_digital.db` | Arquivo do banco SQLite                     |
| `ACERVO_DRY_RUN`  | `1`                  | `1` = só simula; `0` = copia de verdade     |

Execução (a partir da raiz do projeto):

```bash
# 1. Varredura e classificação (simulação)
python main.py

# 2. Relatório CSV + resumo por categoria
python src/utils/reporter.py

# 3. Lista de duplicados
python -c "from src.core.duplicates import localizar_duplicados; [print(d) for d in localizar_duplicados()]"

# Diagnóstico rápido do banco (categorias e extensões não classificadas)
python verificar_db.py
```

Depois de revisar o relatório, rode novamente com `ACERVO_DRY_RUN=0` para copiar os arquivos.

### Testes

```bash
pip install -r requirements-dev.txt
pytest
```

Os testes usam arquivos fictícios em pastas temporárias e um banco descartável.

## Exemplo de saída

Dados fictícios:

```
INICIANDO VARREDURA...

MODO DRY-RUN: nenhum arquivo será copiado.

PROCESSAMENTO FINALIZADO

TOTAL PROCESSADO: 6

============================================================
LOCALIZANDO DUPLICADOS
============================================================

Arquivos carregados: 6
Candidatos: 2

DUPLICADOS ENCONTRADOS: 1

============================================================
RESUMO POR CATEGORIA
============================================================

IMAGENS                      2 arquivos         0.00 GB
ESTUDOS                      1 arquivos         0.00 GB
AUDIO                        1 arquivos         0.00 GB
FINANCEIRO                   1 arquivos         0.00 GB
OUTROS                       1 arquivos         0.00 GB
```

Trecho do CSV gerado:

| nome_original    | novo_nome                            | categoria  |
|------------------|--------------------------------------|------------|
| IMG_0001.jpg     | 2015-08-22_IMAGENS_IMG_0001.jpg      | IMAGENS    |
| apostila.pdf     | 2017-02-10_ESTUDOS_apostila.pdf      | ESTUDOS    |
| gastos 2018.xlsx | 2018-12-30_FINANCEIRO_gastos 2018.xlsx | FINANCEIRO |

## Estrutura

```
├── main.py                 # ponto de entrada: varre, classifica e registra
├── config.py               # pastas, banco, dry-run, extensões
├── verificar_db.py         # diagnóstico do banco
├── src/
│   ├── core/               # scanner, classifier, renamer, duplicates
│   ├── models/             # modelo SQLAlchemy / SQLite
│   └── utils/              # relatório CSV
└── tests/                  # testes com pytest
```

## Licença

MIT. Veja [LICENSE](LICENSE).
