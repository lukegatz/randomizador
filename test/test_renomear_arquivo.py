import os
from unittest import TestCase, mock
from unittest.mock import patch

from hash.hashing import hash_pipe
from test.mocks import mock_lista, mock_lista_vazia
from arquivos.renomear_arquivo import decouple_lista, info_arquivo, renomear_arquivo


class Test(TestCase):

    def setUp(self):
        self.test_folder = '/home/luciano/Música/pendrive/teste-randomize/teste'
        os.makedirs(self.test_folder, exist_ok=True)
        # Cria arquivo para ser renomeado
        with open(f'{self.test_folder}/original.txt', 'w') as file:
            file.write('Original content')

        self.hash_mock = hash_pipe(f'{self.test_folder}/original.txt')

    def tearDown(self):
        # Remove o arquivo e a pasta de teste
        for file_name in os.listdir(self.test_folder):
            file_path = os.path.join(self.test_folder, file_name)
            os.remove(file_path)
        os.rmdir(self.test_folder)

    def test_renomear_arquivo_sucesso(self):
        lista_original = [
            {'arquivo': 'original.txt', 'hash': self.hash_mock}
        ]
        arquivo_ren = '9999 original.txt'
        pasta = self.test_folder

        result = renomear_arquivo(lista_original, arquivo_ren, pasta)
        self.assertEqual(result, 'Sucesso!')

        # Verifica se o arquivo foi renomeado corretamente
        self.assertFalse(os.path.exists(f'{pasta}/original.txt'))
        self.assertTrue(os.path.exists(f'{pasta}/9999 original.txt'))

    def test_renomear_arquivo_arquivo_nao_encontrado(self):
        lista_original = []
        arquivo_ren = 'renomeado.txt'
        pasta = self.test_folder

        result = renomear_arquivo(lista_original, arquivo_ren, pasta)
        self.assertEqual(result, 'Arquivo não encontrado na lista original')

        # Verifica se nenhum arquivo foi renomeado
        self.assertTrue(os.path.exists(f'{pasta}/original.txt'))
        self.assertFalse(os.path.exists(f'{pasta}/renomeado.txt'))

    def test_renomear_arquivo_erro_desconhecido(self):
        lista_original = [
            {'arquivo': 'original.txt', 'hash': '1234567890'}
        ]
        arquivo_ren = '9999 original.txt'
        pasta = self.test_folder

        # Força o erro de leitura desconhecido definindo hash_orig e hash_pesq como diferentes
        result = renomear_arquivo(lista_original, arquivo_ren, pasta)
        self.assertEqual(result, 'Erro desconhecido')

        # Verifica se nenhum arquivo foi renomeado
        self.assertTrue(os.path.exists(f'{pasta}/original.txt'))
        self.assertFalse(os.path.exists(f'{pasta}/renomeado.txt'))

    def test_renomear_arquivo_os_error(self):
        lista_original = [
            {'arquivo': 'original.txt', 'hash': '1234567890'}
        ]
        arquivo_ren = '9999 original.txt'
        pasta = self.test_folder

        # Força um erro OS
        with mock.patch("arquivos.renomear_arquivo.renomear_arquivo") as mock_error:
            mock_error.side_effect = OSError
        self.assertRaises(OSError)

    @patch("arquivos.renomear_arquivo.decouple_lista")
    def test_decouple_lista(self, mock_elemento):
        mock_elemento.return_value = '0002 Beirut -  - The Gulag Orkestar.mp3'
        elemento = decouple_lista(mock_lista)
        self.assertEqual(elemento, mock_elemento.return_value, "Retorno do decouple_lista!")

    @patch("arquivos.renomear_arquivo.decouple_lista")
    def test_decouple_lista_vazia(self, mock_elemento):
        mock_elemento.return_value = ''
        elemento = decouple_lista(mock_lista_vazia)
        self.assertRaises(IndexError)

    @patch("mocks.pasta")
    @patch("mocks.mock_lista")
    @patch("arquivos.renomear_arquivo.renomear_trim")
    def test_renomear_trim(self, func_renomear, mock_lista, pasta):
        func_renomear(mock_lista, pasta)
        func_renomear.assert_called_once_with(mock_lista, pasta)

    @patch("mocks.arquivo_ren_mock")
    @patch("mocks.mock_arquivos")
    @patch("arquivos.renomear_arquivo.info_arquivo")
    def test_info_arquivo(self, info, lista_original, arquivo_ren):
        lista_original.return_value = [{
            'arquivo': 'Beirut -  - The Gulag Orkestar.mp3',
            'hash': '',
        }]
        arquivo_ren.return_value = '0002 Beirut -  - The Gulag Orkestar.mp3'
        info.return_value = {
            'original': 'Beirut -  - The Gulag Orkestar.mp3',
            'novo_nome': '0002 Beirut -  - The Gulag Orkestar.mp3',
            'hash_orig': '',
        }
        info_arq = info_arquivo(lista_original.return_value, arquivo_ren.return_value)
        self.assertEqual(info.return_value, info_arq, "Retorno do info_arquivo!")
