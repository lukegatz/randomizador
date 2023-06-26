import os, re
from typing import Union, Any

from hash.hashing import comparar_hashes, hash_pipe


def decouple_lista(lista_ren: list) -> Union[list[Any], Any]:
    """

    :param lista_ren A lista com os novos nomes de arquivos para o processo de rename
    :return: O último elemento retirado da lista (um string)
    """
    try:
        item_ren = lista_ren.pop()
    except IndexError as IE:
        print(f'ERRO: Lista vazia! {IE}')
        return []
    return item_ren


def renomear_trim(lista_original: list, pasta: str):
    """

    :param lista_original: A lista de arquivos que será formatada
    :param pasta: A pasta na qual será aplicado o processo de rename
    :return: None ou OSError
    """
    for arquivo in lista_original:
        nome_arquivo, extensao = arquivo.rsplit('.', 1)
        original = f'{nome_arquivo}.{extensao}'
        nome_arquivo = re.sub(r'^\d+', '', nome_arquivo).lstrip()
        novo_arquivo = f'{nome_arquivo}.{extensao}'
        try:
            os.rename(f"{pasta}/{original}", f"{pasta}/{novo_arquivo}")
        except OSError as e:
            return f'Erro ao renomear o arquivo: {str(e)}'


def renomear_arquivo(lista_original: list, arquivo_ren: str, pasta: str) -> str:
    """

    :param lista_original: A lista de arquivos -- com hashes -- que serão renomeados
    :param arquivo_ren: O nome do arquivo a ser renomeado
    :param pasta: A pasta em que está sendo aplicada a reordenação
    :return: Um string indicando o sucesso da operação ou a mensagem de erro, quando aplicável
    """
    if not (info := info_arquivo(lista_original, arquivo_ren)):
        return 'Arquivo não encontrado na lista original'

    hash_orig = info['hash_orig']
    hash_pesq = hash_pipe(f'{pasta}/{info["original"]}')

    if comparar_hashes(hash_orig, hash_pesq):
        try:
            os.rename(f"{pasta}/{info['original']}", f"{pasta}/{info['novo_nome']}")
            return 'Sucesso!'
        except OSError as e:
            return f'Erro ao renomear o arquivo: {str(e)}'
    return 'Erro desconhecido'


def info_arquivo(lista_original: list, arquivo_ren: str) -> dict:
    """

    :param lista_original: A lista de arquivos sobre a qual iremos iterar
    :param arquivo_ren: O nome com o qual o arquivo constante na lista será renomeado
    :return: Um dictionary contendo nome original do arquivo, o novo nome com o qual o arquivo
        será renomeado e o hash do arquivo original
    """
    return next(
        (
            {
                'original': item['arquivo'],
                'novo_nome': arquivo_ren,
                'hash_orig': item['hash'],
            }
            for item in lista_original
            if arquivo_ren[5:] == item['arquivo']
        ),
        {},
    )