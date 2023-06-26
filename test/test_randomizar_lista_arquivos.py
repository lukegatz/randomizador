import random
from unittest import TestCase
from unittest.mock import patch

from arquivos.randomizar_lista_arquivos import randomizar_lista


class Test(TestCase):

    @patch("mocks.mock_lista")
    def test_randomizar_lista(self, lista_mock):
        lista_mock.return_value = ['Cat Power-Maybe Not.flv',
              'David Bowie - Lets Dance.mp4',
              'Autoramas -  - Verdugo.ogg',
              'Alice in Chains - Down in a Hole (MTV Unplugged).mp3',
              'Beirut -  - The Gulag Orkestar.mp3']
        saida = randomizar_lista(lista_mock.return_value)
        lista = list(saida)
        aleatorio = random.randint(1,len(lista)-1)
        self.assertRegex(lista[aleatorio][0:6], '\d{4} \w', "Verifica se os nomes estão no formato exigido")
