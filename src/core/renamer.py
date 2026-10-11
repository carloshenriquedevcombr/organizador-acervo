import os
from datetime import datetime

def gerar_novo_nome(arquivo_meta, categoria):
    # Extrai a data de criação
    data = arquivo_meta['data_criacao'].strftime('%Y-%m-%d')
    nome_base = os.path.splitext(arquivo_meta['nome'])[0]
    ext = arquivo_meta['extensao']
    
    # Criamos o nome padronizado
    novo_nome = f"{data}_{categoria}_{nome_base}{ext}"
    
    # Removemos caracteres proibidos para nomes de arquivos no Windows
    caracteres_proibidos = '<>:"/\\|?*'
    for char in caracteres_proibidos:
        novo_nome = novo_nome.replace(char, '_')
        
    return novo_nome
