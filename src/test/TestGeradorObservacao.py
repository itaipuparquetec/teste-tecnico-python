import unittest

from src.main.GeradorObservacao import GeradorObservacao


class TestGeradorObservacao(unittest.TestCase):

    def setUp(self):
        self.geradorObservacao = GeradorObservacao()

    def test_deve_gerar_observacao_sem_nota(self):
        numerosNotaFiscal = []
        observacao = self.geradorObservacao.geraObservacao(numerosNotaFiscal)
        self.assertEqual("", observacao)

    def test_deve_gerar_observacao_com_uma_nota(self):
        numerosNotaFiscal = [1]
        observacao = self.geradorObservacao.geraObservacao(numerosNotaFiscal)
        self.assertEqual("Fatura da nota fiscal de simples remessa: 1.", observacao)

    def test_deve_gerar_observacao_com_duas_notas(self):
        numerosNotaFiscal = [1, 3]
        observacao = self.geradorObservacao.geraObservacao(numerosNotaFiscal)
        self.assertEqual("Fatura das notas fiscais de simples remessa: 1 e 3.", observacao)

    def test_deve_gerar_observacao_com_diversas_notas(self):
        numerosNotaFiscal = [1, 2, 3, 4, 5]
        observacao = self.geradorObservacao.geraObservacao(numerosNotaFiscal)
        self.assertEqual("Fatura das notas fiscais de simples remessa: 1, 2, 3, 4 e 5.", observacao)


if __name__ == "__main__":
    unittest.main()
