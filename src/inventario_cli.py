from __future__ import annotations

import csv
import ipaddress
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INVENTARIO_PATH = BASE_DIR / "inventario" / "inventario-equipamentos.csv"

COLUNAS = [
    "ID",
    "Equipamento",
    "Marca",
    "Modelo",
    "Numero_Serie",
    "Endereco_IP",
    "Endereco_MAC",
    "Localizacao",
    "Estado",
    "Observacoes",
]

ESTADOS_VALIDOS = ("Ativo", "Manutencao", "Inativo")
MAC_REGEX = re.compile(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$")


def validar_ip(endereco_ip: str) -> str:
    valor = endereco_ip.strip()
    try:
        ipaddress.ip_address(valor)
    except ValueError as exc:
        raise ValueError(f"Endereço IP inválido: '{valor}'.") from exc
    return valor


def validar_mac(endereco_mac: str) -> str:
    valor = endereco_mac.strip().upper()
    if not MAC_REGEX.match(valor):
        raise ValueError(f"Endereço MAC inválido: '{valor}'. Use o formato XX:XX:XX:XX:XX:XX.")
    return valor


def validar_estado(estado: str) -> str:
    valor = estado.strip()
    if valor not in ESTADOS_VALIDOS:
        opcoes = ", ".join(ESTADOS_VALIDOS)
        raise ValueError(f"Estado inválido: '{valor}'. Valores permitidos: {opcoes}.")
    return valor


def carregar_inventario(caminho: Path = INVENTARIO_PATH) -> list[dict[str, str]]:
    if not caminho.exists():
        raise FileNotFoundError(f"Ficheiro não encontrado: {caminho}")

    with caminho.open(mode="r", encoding="utf-8", newline="") as ficheiro:
        leitor = csv.DictReader(ficheiro)
        if leitor.fieldnames != COLUNAS:
            raise ValueError(
                f"Estrutura CSV inválida em {caminho.name}. Colunas esperadas: {COLUNAS}."
            )
        return [{col: (linha.get(col) or "").strip() for col in COLUNAS} for linha in leitor]


def guardar_inventario(registos: list[dict[str, str]], caminho: Path = INVENTARIO_PATH) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open(mode="w", encoding="utf-8", newline="") as ficheiro:
        escritor = csv.DictWriter(ficheiro, fieldnames=COLUNAS)
        escritor.writeheader()
        escritor.writerows(registos)


def adicionar_equipamento(registos: list[dict[str, str]], dados: dict[str, str]) -> list[dict[str, str]]:
    eq_id = dados.get("ID", "").strip().upper()
    if not eq_id:
        raise ValueError("O campo ID é obrigatório.")
    if any(item["ID"].upper() == eq_id for item in registos):
        raise ValueError(f"Já existe um equipamento com o ID '{eq_id}'.")

    novo = {col: dados.get(col, "").strip() for col in COLUNAS}
    novo["ID"] = eq_id
    novo["Endereco_IP"] = validar_ip(novo["Endereco_IP"])
    novo["Endereco_MAC"] = validar_mac(novo["Endereco_MAC"])
    novo["Estado"] = validar_estado(novo["Estado"])

    return [*registos, novo]


def atualizar_estado(registos: list[dict[str, str]], eq_id: str, novo_estado: str) -> list[dict[str, str]]:
    id_alvo = eq_id.strip().upper()
    estado_validado = validar_estado(novo_estado)

    atualizado = False
    resultado: list[dict[str, str]] = []
    for item in registos:
        copia = dict(item)
        if copia["ID"].upper() == id_alvo:
            copia["Estado"] = estado_validado
            atualizado = True
        resultado.append(copia)

    if not atualizado:
        raise KeyError(f"Equipamento com ID '{id_alvo}' não encontrado.")
    return resultado


def pesquisar_equipamentos(registos: list[dict[str, str]], termo: str) -> list[dict[str, str]]:
    termo_normalizado = termo.strip().lower()
    if not termo_normalizado:
        return []
    return [
        item
        for item in registos
        if any(termo_normalizado in item[col].lower() for col in COLUNAS)
    ]


def resumo_estados(registos: list[dict[str, str]]) -> dict[str, int]:
    contagem = {estado: 0 for estado in ESTADOS_VALIDOS}
    for item in registos:
        estado = item.get("Estado", "")
        if estado in contagem:
            contagem[estado] += 1
    return contagem


def imprimir_tabela(registos: list[dict[str, str]]) -> None:
    if not registos:
        print("\nSem registos para apresentar.")
        return

    print(f"\nRegistos encontrados: {len(registos)}")
    print(f"{'ID':<8} {'Equipamento':<18} {'IP':<16} {'Localizacao':<28} {'Estado':<12}")
    print("-" * 86)
    for eq in registos:
        print(
            f"{eq['ID']:<8} {eq['Equipamento']:<18} {eq['Endereco_IP']:<16} "
            f"{eq['Localizacao']:<28} {eq['Estado']:<12}"
        )


def executar_cli() -> None:
    while True:
        print("\nGestão de Inventário de Rede")
        print("1 - Listar equipamentos")
        print("2 - Pesquisar equipamento")
        print("3 - Adicionar equipamento")
        print("4 - Atualizar estado")
        print("5 - Resumo por estado")
        print("0 - Sair")

        opcao = input("Opção: ").strip()
        try:
            registos = carregar_inventario()
            if opcao == "1":
                imprimir_tabela(registos)
            elif opcao == "2":
                termo = input("Termo de pesquisa: ")
                imprimir_tabela(pesquisar_equipamentos(registos, termo))
            elif opcao == "3":
                dados = {
                    "ID": input("ID: "),
                    "Equipamento": input("Equipamento: "),
                    "Marca": input("Marca: "),
                    "Modelo": input("Modelo: "),
                    "Numero_Serie": input("Número de série: "),
                    "Endereco_IP": input("Endereço IP: "),
                    "Endereco_MAC": input("Endereço MAC: "),
                    "Localizacao": input("Localização: "),
                    "Estado": input("Estado (Ativo/Manutencao/Inativo): "),
                    "Observacoes": input("Observações: "),
                }
                guardar_inventario(adicionar_equipamento(registos, dados))
                print("Equipamento registado.")
            elif opcao == "4":
                eq_id = input("ID do equipamento: ")
                novo_estado = input("Novo estado (Ativo/Manutencao/Inativo): ")
                guardar_inventario(atualizar_estado(registos, eq_id, novo_estado))
                print("Estado atualizado.")
            elif opcao == "5":
                resumo = resumo_estados(registos)
                print("\nResumo por estado:")
                for estado, total in resumo.items():
                    print(f"  {estado}: {total}")
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")
        except (FileNotFoundError, ValueError, KeyError) as erro:
            print(f"Erro: {erro}")


