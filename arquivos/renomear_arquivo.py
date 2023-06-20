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


# if __name__ == '__main__':
#     vazia = []
#     listona = {'1153 David Bowie - Lets Dance.mp3', '4326 Beirut - 1 - The Gulag Orkestar.mp3',
#                '5874 Alice in Chains - Down in a Hole (MTV Unplugged).mp3', '3142 Autoramas - 3 - Verdugo.mp3',
#                '9129 Cat Power-Maybe Not.mp3'}
#
#     lista_orig = [{'arquivo': 'Alice in Chains - Down in a Hole (MTV Unplugged).mp3',
#                    'hash': 'd9840588dc4f3aa0716bde3a3e05a6f8b99be2f001657fdee99e02660b712847'},
#                   {'arquivo': 'Autoramas - 3 - Verdugo.mp3',
#                    'hash': '5eae4ccb1424b6a6a3c4b206adf93b97041d942d283d8a389ab400cf29fd89e6'},
#                   {'arquivo': 'Beirut - 1 - The Gulag Orkestar.mp3',
#                    'hash': '5c0bc743da5576c5d42314ef70850a079e56e1380c38ee93e0349c62abc5a85d'},
#                   {'arquivo': 'Cat Power-Maybe Not.mp3',
#                    'hash': '0b7aefad8289f01c99a98fc55f5a10fb2e03c2425ab09c592aca4e7d80271d71'},
#                   {'arquivo': 'David Bowie - Lets Dance.mp3',
#                    'hash': 'c4a74adb883ff9d19e77f3e09b1f9e70655dda76001f2f45fcf4b81566bf2fe8'}]
#
#     hash_orig = '0b7aefad8289'
#     hash_novo = '0b7aefad8289'
#     comp = comparar_hashes(hash_orig, hash_novo)
#     pasta = '/home/luciano/Música/pendrive/teste-randomize'
#
#
#     for e in listona.copy():
#         elem = decouple_lista(listona)
#         print(listona)
#         print(renomear_arquivo(lista_orig, elem))
#         print('')
#         print(f'Hashes to hashes: {comp}')
