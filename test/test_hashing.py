import os
from unittest import TestCase
from unittest.mock import patch

from hash.hashing import hash_pipe, gerar_hash


class Test(TestCase):

    def setUp(self) -> None:
        self.test_folder = '/home/luciano/Música/pendrive/teste-randomize/teste'
        os.makedirs(self.test_folder, exist_ok=True)
        # Cria arquivo para gerar o hash
        with open(f'{self.test_folder}/original.txt', 'w') as file:
            file.write('Original content')

        self.hash_mock = hash_pipe(f'{self.test_folder}/original.txt')

    def tearDown(self):
        # Remove o arquivo e a pasta de teste
        for file_name in os.listdir(self.test_folder):
            file_path = os.path.join(self.test_folder, file_name)
            os.remove(file_path)
        os.rmdir(self.test_folder)

    @patch("hash.hashing.gerar_hash")
    def test_gerar_hash(self, lista_hash):
        lista = ['original.txt']
        lista_hash.return_value = [{
            'arquivo': 'original.txt',
            'hash': self.hash_mock,
        }]
        saida = gerar_hash(lista, self.test_folder)
        self.assertEqual(saida, lista_hash.return_value, 'Compara a saída do gerar_hash com o modelo')
