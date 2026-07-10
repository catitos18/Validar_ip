import unittest
from validar_ip import es_ip_valida


class TestValidarIP(unittest.TestCase):

    # IP válida
    def test_ip_valida(self):
        self.assertTrue(es_ip_valida("192.168.1.1"))

    # Octeto mayor a 255
    def test_octeto_mayor_255(self):
        self.assertFalse(es_ip_valida("256.168.1.1"))

    # IP con letras
    def test_ip_con_letras(self):
        self.assertFalse(es_ip_valida("192.abc.1.1"))

    # Menos de 4 partes
    def test_menos_de_4_partes(self):
        self.assertFalse(es_ip_valida("192.168.1"))

    # Más de 4 partes
    def test_mas_de_4_partes(self):
        self.assertFalse(es_ip_valida("192.168.1.1.5"))


if __name__ == "__main__":
    unittest.main()