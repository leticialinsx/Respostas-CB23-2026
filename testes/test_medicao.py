"""Seus testes do Marco 2 (veja a seção 5 do ENUNCIADO_MARCO2.md).

Regras: pelo menos 4 testes seus (o exemplo abaixo não conta), uma docstring em cada teste
dizendo qual caso ele cobre, e floats comparados com assertAlmostEqual, math.isclose ou
np.allclose, a não ser que a igualdade exata seja justamente o que você quer testar.
"""
import math
import unittest

import numpy as np

from elevatoria.acumuladores import AcumuladorIngenuo, AcumuladorKahan


class TestAcumuladorIngenuoExemplo(unittest.TestCase):
    """Exemplo do formato. `AcumuladorIngenuo` é código existente da base."""

    def test_sem_parcelas(self):
        """Sem nenhuma parcela, o total é zero."""
        self.assertEqual(AcumuladorIngenuo().total, 0.0)


# Issue #7: regressão do AcumuladorKahan

def _somar(acumulador, parcelas) -> float:
    """Soma as parcelas com o acumulador dado e devolve o total."""
    for parcela in parcelas:
        acumulador.adicionar(parcela)
    return acumulador.total


class TestAcumuladorKahanRegressao(unittest.TestCase):
    """Testes de regressão da issue #7 (escritos antes da correção)."""

    def test_um_milhao_de_decimos_de_litro(self):
        """Um milhão de parcelas de 0,1 deve dar 100000, com erro bem abaixo do ingênuo (1,3e-6)."""
        total = _somar(AcumuladorKahan(), [0.1] * 1_000_000)
        self.assertAlmostEqual(total, 100000.0, delta=1e-8)

    def test_kahan_bem_melhor_que_o_ingenuo(self):
        """O erro do Kahan deve ser pelo menos mil vezes menor que o do ingênuo."""
        parcelas = [0.1] * 1_000_000
        erro_ingenuo = abs(_somar(AcumuladorIngenuo(), parcelas) - 100000.0)
        erro_kahan = abs(_somar(AcumuladorKahan(), parcelas) - 100000.0)
        self.assertLessEqual(erro_kahan, erro_ingenuo / 1000)

    def test_parcelas_menores_que_o_arredondamento(self):
        """Parcelas de 1e-16 somadas a 1.0 se perdem no ingênuo, mas o Kahan as acumula."""
        parcelas = [1.0] + [1e-16] * 1_000_000
        self.assertAlmostEqual(_somar(AcumuladorKahan(), parcelas), 1.0 + 1e-10, delta=1e-12)
        self.assertEqual(_somar(AcumuladorIngenuo(), parcelas), 1.0)

    def test_valores_variados_contra_math_fsum(self):
        """Com valores sortidos, o Kahan fica mais perto da soma exata (math.fsum) que o ingênuo."""
        parcelas = np.random.default_rng(7).uniform(0.0, 1.0, 200_000).tolist()
        exato = math.fsum(parcelas)
        erro_ingenuo = abs(_somar(AcumuladorIngenuo(), parcelas) - exato)
        erro_kahan = abs(_somar(AcumuladorKahan(), parcelas) - exato)
        self.assertLess(erro_kahan, erro_ingenuo)


if __name__ == "__main__":
    unittest.main()
