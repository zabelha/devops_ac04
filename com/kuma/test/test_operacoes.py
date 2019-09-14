from unittest import TestCase 
from com.kuma.operacoes import Operacoes


class TestOperacoes(TestCase):

	def setUp(self):
		self.operacoes = Operacoes()
		
	
	def test_divisao(self):
		self.assertEqual(self.operacoes.divisao([10,2]), 5, "Should be 5")