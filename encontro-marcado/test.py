from unittest import TestCase, main
from solucao import encontra_rota
from time import time


class TestEncontroMarcado(TestCase):
    def setUp(self):
        self.B1 = [(0, 0, 0, 1), (1, 1, 1, 2), (1, 0, 2, 0),
                   (1, 1, 2, 1), (1, 2, 2, 2)]
        self.B2 = [(0, 0, 0, 1), (0, 1, 0, 2), (1, 1, 1, 2),
                   (1, 0, 2, 0), (1, 1, 2, 1), (1, 2, 2, 2)]

    def test_rota_possivel(self):
        self.assertNotEqual(encontra_rota(5, 5, 4, 3, self.B1), "IMPOSSIVEL")

    def test_rota_impossivel(self):
        self.assertEqual(encontra_rota(5, 5, 4, 3, self.B2), "IMPOSSIVEL")


if __name__ == "__main__":
    main()
