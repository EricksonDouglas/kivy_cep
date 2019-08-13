import unittest
from validador import Validador

class TestCep(unittest.TestCase):

    def test_valido(self):
        self.assertDictEqual(Validador.cep("123456"),{"valido":1})
        self.assertDictEqual(Validador.cep("234534"),{"valido":1})

    def test_None(self):
        self.assertEqual(Validador.cep("1234567"),None)
        self.assertEqual(Validador.cep("fasjia"),None)
        self.assertEqual(Validador.cep("129i23"),None)

    def test_invalido(self):
        self.assertDictEqual(Validador.cep("121212"),{"valido":0,"repetitivo":[1,2]})
        self.assertDictEqual(Validador.cep("234521"),{"valido":0,"repetitivo":[2]}) 


if __name__ == "__main__": unittest.main()
