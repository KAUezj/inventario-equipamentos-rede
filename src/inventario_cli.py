import csv
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

ESTADOS_VALIDOS = {"Ativo", "Manutencao", "Inativo"}


def carregar_inventario(caminho: Path = INVENTARIO_PATH) -> list[dict[str, str]]:
    if not caminho.exists():
        raise FileNotFoundError(f"Ficheiro de inventário não encontrado: {caminho}")
    with caminho.open(mode="r", encoding="utf-8", newline="") as f:
        leitor = csv.DictReader(f)
        if leitor.fieldnames != COLUNAS:
            raise ValueError(
                f"Cabeçalho inválido em {caminho}. Esperado: {COLUNAS}, obtido: {leitor.fieldnames}"
            )
        return [{col: (linha.get(col) or "").strip() for col in COLUNAS} for linha in leitor]


def guardar_inventario(registos: list[dict[str, str]], caminho: Path = INVENTARIO_PATH) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open(mode="w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=COLUNAS)
        escritor.writeheader()
        escritor.writerows(registos)


def listar_equipamentos(registos: list[dict[str, str]]) -> None:
    if not registos:
        print("\nNenhum equipamento registado no inventário.")
        return
    print(f"\nTotal de equipamentos: {len(registos)}")
    print("-" * 95)
    for eq in registos:
        print(
            f"[{eq['ID']}] {eq['Equipamento']} ({eq['Marca']} {eq['Modelo']}) | "
            f"IP: {eq['Endereco_IP']} | Local: {eq['Localizacao']} | Estado: {eq['Estado']}"
        )
    print("-" * 95)


def pesquisar_equipamentos(registos: list[dict[str, str]], termo: str) -> list[dict[str, str]]:
    termo_limpo = termo.strip().lower()
    if not termo_limpo:
        return []
    return [
        eq
        for eq in registos
        if any(termo_limpo in (eq.get(campo) or "").lower() for campo in COLUNAS)
    ]


def adicionar_equipamento(registos: list[dict[str, str]], novo: dict[str, str]) -> list[dict[str, str]]:
    eq_id = novo["ID"].strip().upper()
    if not eq_id:
        raise ValueError("O ID do equipamento é obrigatório.")
    if any(eq["ID"].strip().upper() == eq_id for eq in registos):
        raise ValueError(f"Já existe um equipamento com o ID '{eq_id}'.")

    estado = novo["Estado"].strip()
    if estado not in ESTADOS_VALIDOS:
        raise ValueError(f"Estado inválido '{estado}'. Use um de: {', '.join(sorted(ESTADOS_VALIDOS))}.")

    registo_limpo = {col: novo.get(col, "").strip() for col in COLUNAS}
    registo_limpo["ID"] = eq_id
    registo_limpo["Estado"] = estado

    atualizados = list(registos)
    atualizados.append(registo_limpo)
    return atualizados


def atualizar_estado(registos: list[dict[str, str]], eq_id: str, novo_estado: str) -> list[dict[str, str]]:
    id_alvo = eq_id.strip().upper()
    estado_limpo = novo_estado.strip()
    if estado_limpo not in ESTADOS_VALIDOS:
        raise ValueError(
            f"Estado inválido '{estado_limpo}'. Use um de: {', '.join(sorted(ESTADOS_VALIDOS))}."
        )

    encontrado = False
    atualizados: list[dict[str, str]] = []
    for eq in registos:
        copia = dict(eq)
        if copia["ID"].strip().upper() == id_alvo:
            copia["Estado"] = estado_limpo
            encontrado = True
        atualizados.append(copia)

    if not encontrado:
        raise KeyError(f"Equipamento com ID '{id_alvo}' não encontrado.")
    return atualizados


def resumo_estados(registos: list[dict[str, str]]) -> dict[str, int]:
    contagem = {"Ativo": 0, "Manutencao": 0, "Inativo": 0, "Outro": 0}
    for eq in registos:
        estado = eq.get("Estado", "")
        if estado in contagem:
            contagem[estado] += 1
        else:
            contagem["Outro"] += 1
    return contagem


def menu() -> None:
    while True:
        print("\n=== INVENTÁRIO DE EQUIPAMENTOS DE REDE (CLI) ===")
        print("1. Listar equipamentos")
        print("2. Pesquisar equipamento")
        print("3. Adicionar equipamento")
        print("4. Atualizar estado operacional")
        print("5. Ver resumo por estado")
        print("0. Sair")
        opcao = input("Escolha uma opção: ").strip()

        try:
            registos = carregar_inventario()
            if opcao == "1":
                listar_equipamentos(registos)
            elif opcao == "2":
                termo = input("Termo de pesquisa (ID, IP, marca, localização ou estado): ")
                resultados = pesquisar_equipamentos(registos, termo)
                listar_equipamentos(resultados)
            elif opcao == "3":
                novo = {
                    "ID": input("ID (ex.: SW-03): "),
                    "Equipamento": input("Equipamento (ex.: Switch Acesso): "),
                    "Marca": input("Marca (ex.: Cisco): "),
                    "Modelo": input("Modelo (ex.: Catalyst 2960): "),
                    "Numero_Serie": input("Número de Série: "),
                    "Endereco_IP": input("Endereço IP: "),
                    "Endereco_MAC": input("Endereço MAC: "),
                    "Localizacao": input("Localização: "),
                    "Estado": input("Estado (Ativo / Manutencao / Inativo): "),
                    "Observacoes": input("Observações: "),
                }
                atualizados = adicionar_equipamento(registos, novo)
                guardar_inventario(atualizados)
                print("Equipamento adicionado e guardado com sucesso.")
            elif opcao == "4":
                eq_id = input("ID do equipamento a atualizar: ")
                novo_estado = input("Novo estado (Ativo / Manutencao / Inativo): ")
                atualizados = atualizar_estado(registos, eq_id, novo_estado)
                guardar_inventario(atualizados)
                print("Estado atualizado com sucesso.")
            elif opcao == "5":
                resumo = resumo_estados(registos)
                print("\nResumo por estado:")
                for estado, total in resumo.items():
                    print(f"  - {estado}: {total}")
            elif opcao == "0":
                print("A sair...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except (FileNotFoundError, ValueError, KeyError) as exc:
            print(f"Erro: {exc}")


if __name__ == "__main__":
    menu()
