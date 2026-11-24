import tempfile
import unittest
from pathlib import Path

from src import inventario_cli as cli


def exemplo_equipamento(eq_id: str = "SW-03", estado: str = "Ativo") -> dict[str, str]:
    return {
        "ID": eq_id,
        "Equipamento": "Switch Acesso",
        "Marca": "Cisco",
        "Modelo": "Catalyst 2960",
        "Numero_Serie": "SN998877",
        "Endereco_IP": "192.168.1.50",
        "Endereco_MAC": "00:1A:2B:3C:4D:50",
        "Localizacao": "Sala TI",
        "Estado": estado,
        "Observacoes": "Porta uplink ativa",
    }


class TestInventarioCLI(unittest.TestCase):
    def setUp(self) -> None:
        self.base = [exemplo_equipamento("RTR-01", "Ativo")]

    def test_persistencia_csv(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            caminho = Path(tmp) / "inventario.csv"
            cli.guardar_inventario(self.base, caminho)
            carregado = cli.carregar_inventario(caminho)
            self.assertEqual(carregado, self.base)

    def test_adicionar_e_validar_duplicado(self) -> None:
        atualizado = cli.adicionar_equipamento(self.base, exemplo_equipamento("SW-03"))
        self.assertEqual(len(atualizado), 2)
        with self.assertRaises(ValueError):
            cli.adicionar_equipamento(atualizado, exemplo_equipamento("sw-03"))

    def test_validacao_ip_mac_e_estado(self) -> None:
        with self.assertRaises(ValueError):
            cli.validar_ip("999.999.1.1")
        with self.assertRaises(ValueError):
            cli.validar_mac("AA-BB-CC-DD-EE-FF")
        with self.assertRaises(ValueError):
            cli.validar_estado("Pendente")

    def test_atualizar_estado_e_pesquisar(self) -> None:
        atualizado = cli.atualizar_estado(self.base, "RTR-01", "Manutencao")
        self.assertEqual(atualizado[0]["Estado"], "Manutencao")
        resultados = cli.pesquisar_equipamentos(atualizado, "Manutencao")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0]["ID"], "RTR-01")


if __name__ == "__main__":
    unittest.main()