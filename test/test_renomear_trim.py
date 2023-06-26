import unittest
import os

from arquivos.renomear_arquivo import renomear_trim


class TestRenomearTrim(unittest.TestCase):

    def setUp(self):
        self.test_folder = '/home/luciano/Música/pendrive/teste-randomize/teste'
        os.makedirs(self.test_folder, exist_ok=True)
        # Cria arquivos para serem renomeados
        with open(f'{self.test_folder}/1111 file.txt', 'w') as file1:
            file1.write('File 1 content')
        with open(f'{self.test_folder}/2222 file_1.txt', 'w') as file2:
            file2.write('File 2 content')

    def tearDown(self):
        # Remove os arquivos e a pasta de teste
        for file_name in os.listdir(self.test_folder):
            file_path = os.path.join(self.test_folder, file_name)
            os.remove(file_path)
        os.rmdir(self.test_folder)

    def test_renomear_trim(self):
        lista_original = ['1111 file.txt', '2222 file_1.txt']
        pasta = self.test_folder
        renomear_trim(lista_original, pasta)

        # Verifica se os arquivos foram renomeados corretamente
        self.assertFalse(os.path.exists(f'{pasta}/1111 file.txt'))
        self.assertFalse(os.path.exists(f'{pasta}/2222 file_1.txt'))
        self.assertTrue(os.path.exists(f'{pasta}/file.txt'))
        self.assertTrue(os.path.exists(f'{pasta}/file_1.txt'))

    def test_renomear_trim_lista_vazia(self):
        lista_original = []
        pasta = self.test_folder
        renomear_trim(lista_original, pasta)

        # Verifica se nenhum arquivo foi renomeado
        self.assertFalse(os.path.exists(f'{pasta}/file.txt'))
        self.assertFalse(os.path.exists(f'{pasta}/file_1.txt'))

    def test_renomear_trim_arquivo_inexistente(self):
        lista_original = ['nonexistent.txt']
        pasta = self.test_folder
        renomear_trim(lista_original, pasta)

        # Verifica se nenhum arquivo foi renomeado
        self.assertFalse(os.path.exists(f'{pasta}/file.txt'))
        self.assertFalse(os.path.exists(f'{pasta}/file_1.txt'))
        self.assertRaises(OSError)

