from unittest import TestCase 
from com.kuma.operacoes import Operacoes


class TestOperacoes(TestCase):

	def setUp(self):
		self.operacoes = Operacoes()
		
	
	def test_divisao(self):
		self.assertEqual(self.operacoes.divisao([2,10]), 5, "Should be 5")