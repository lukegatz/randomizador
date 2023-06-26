from unittest import TestCase
from unittest.mock import patch

from arquivos.trim_arquivo import trim_file


class Test(TestCase):

    @patch("mocks.mock_lista")
    def test_trim_file(self, lista_mock):
        lista_mock.return_value = ['9184 Cat Power-Maybe Not.flv',
              '6665 David Bowie - Lets Dance.mp4',
              '1234 Autoramas -  - Verdugo.ogg',
              '5678 Alice in Chains - Down in a Hole (MTV Unplugged).mp3',
              '9012 Beirut -  - The Gulag Orkestar.mp3']
        saida = trim_file(lista_mock.return_value)
        lista = list(saida)
        self.assertRegex(lista[0][0:4], "\D{4}", "Verifica se os nomes, após o trim, estão no formato exigido")
