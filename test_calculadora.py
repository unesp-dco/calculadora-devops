import unittest
import calculadora

class TestCalculator(unittest.TestCase):
#	def setUp(self):
#        self.calc = Calculator()

    def test_soma(self):
        self.assertEqual(calculadora.calcular('10','1','+'), 11)
        self.assertEqual(calculadora.calcular('10','-110','+'), -100)
        self.assertEqual(calculadora.calcular('10','-110','.'), None)
        self.assertEqual(calculadora.calcular('a','-110','+'), None)
        self.assertEqual(calculadora.calcular('0.005','1','+'), 1.005)
        self.assertEqual(calculadora.calcular('15','-15','+'), 0)


    def test_subtracao(self):
        self.assertEqual(calculadora.calcular('10','1','-'), 9)
        self.assertEqual(calculadora.calcular('0','-1','-'), 1)
        self.assertEqual(calculadora.calcular('-1.56','-1','-'), -0.56)
        self.assertEqual(calculadora.calcular('10','q','-'), None)
        self.assertEqual(calculadora.calcular('10a','1','-'), None)


    def test_multiplicacao(self):
        self.assertEqual(calculadora.calcular('10','0','*'), 0)
        self.assertEqual(calculadora.calcular('100','100','*'), 10000)
        self.assertEqual(calculadora.calcular('10','-0','*'), 0)
        self.assertEqual(calculadora.calcular('10','0.1','*'), 1)
        self.assertEqual(calculadora.calcular('50','1','*'), 50)


    def test_divisao(self):
        self.assertEqual(calculadora.calcular('10','1','/'), 10)
        self.assertEqual(calculadora.calcular('1','10','/'), 0.1)
        self.assertEqual(calculadora.calcular('10','0','/'), None)
        self.assertEqual(calculadora.calcular('25','4','/'), 6.25)
        self.assertEqual(calculadora.calcular('0','0.63','/'), 0)
        self.assertEqual(calculadora.calcular('100','10','//'), None)
        self.assertEqual(calculadora.calcular('100','10','//'), 0)

    def test_exponenciacao(self):
        self.assertEqual(calculadora.calcular('10','1','^'), 10)
        self.assertEqual(calculadora.calcular('10','0','^'), 1)
        self.assertEqual(calculadora.calcular('10','3','^'), 1000)
        self.assertEqual(calculadora.calcular('2.5','4','^'), 39.0625)
        self.assertEqual(calculadora.calcular('9','-1','^'), 0.1111111111111111)
        self.assertEqual(calculadora.calcular('15','0.4','^'), 2.9541769390627777)


if __name__ == '__main__':
    unittest.main()