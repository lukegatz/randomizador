import hashlib


def hash_pipe(file):
    # file = ".\myfile.txt"             # Location of the file (can be set a different way)
    block_size = 65536                  # The size of each read from the file

    file_hash = hashlib.sha256()        # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file, 'rb') as f:         # Open the file to read it's bytes
        fb = f.read(block_size)         # Read from the file. Take in the amount declared above
        while len(fb) > 0:              # While there is still data being read from the file
            file_hash.update(fb)        # Update the hash
            fb = f.read(block_size)     # Read the next block from the file

    print(file_hash.hexdigest())        # Get the hexadecimal digest of the hash
    return file_hash.hexdigest()


def gerar_hash(lista_arq, pasta):
    lista_ren = []
    # Se o hash for o mesmo fazer o rename
    for arq in lista_arq:
        chave = hash_pipe(f'{pasta}/{arq}')
        item = {'arquivo': arq, 'hash': chave}
        lista_ren.append(item)
    return lista_ren


def comparar_hashes(hash_orig, hash_ren):
    return hash_orig == hash_ren


# def hashes_to_hashes(lista_rand):
#     pass
