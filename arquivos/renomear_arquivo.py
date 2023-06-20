import os, re
from hash.hashing import comparar_hashes, hash_pipe


def decouple_lista(lista_ren):
    try:
        item_ren = lista_ren.pop()
    except IndexError as IE:
        print(f'ERRO: Lista vazia! {IE}')
        return []
    return item_ren


def renomear_trim(lista_original, pasta):
    for arquivo in lista_original:
        nome_arquivo, extensao = arquivo.rsplit('.', 1)
        original = f'{nome_arquivo}.{extensao}'
        nome_arquivo = re.sub(r'^\d+', '', nome_arquivo).lstrip()
        novo_arquivo = f'{nome_arquivo}.{extensao}'
        os.rename(f"{pasta}/{original}", f"{pasta}/{novo_arquivo}")


def renomear_arquivo(lista_original, arquivo_ren, pasta):
    info = info_arquivo(lista_original, arquivo_ren)
    hash_orig = None
    hash_pesq = None

    for item in lista_original:
        if arquivo_ren[5:] == item['arquivo']:
            hash_orig = item['hash']
            hash_pesq = hash_pipe(f'{pasta}/{item["arquivo"]}')

    if comparar_hashes(hash_orig, hash_pesq):
        # print(f"O original eh {info['original']}")
        os.rename(f"{pasta}/{info['original']}", f"{pasta}/{info['novo_nome']}")
        return 'Sucesso!'
    else:
        return 'Num deu certo naum! :('


def info_arquivo(lista_original, arquivo_ren):
    info = {}

    for item in lista_original:
        if arquivo_ren[5:] == item['arquivo']:
            info['original'] = item['arquivo']
            info['novo_nome'] = arquivo_ren
            info['hash_orig'] = item['hash']

    return info