# Inventário de Equipamentos de Rede

Protótipo funcional para gestão e consulta de inventário de equipamentos de rede em formato CSV, desenvolvido no âmbito da unidade curricular / trabalho experimental em equipa (Sprint 2 — `v0.2`).

## Arquitetura do Repositório

```text
inventario-equipamentos-rede/
├── README.md                              # Visão geral, arquitetura e instruções de uso
├── .gitignore                             # Ficheiros ignorados pelo Git
├── app/                                   # Componentes adicionais / aplicação
├── docs/                                  # Documentação do projeto
│   ├── proposta-projeto.md
│   ├── metodologia.md
│   └── documentacao-tecnica.md
├── inventario/                            # Dados operacionais do inventário
│   └── inventario-equipamentos.csv
├── modelos/                               # Modelo base normalizado
│   └── modelo-inventario.csv
├── src/                                   # Código-fonte do protótipo CLI
│   └── inventario_cli.py
└── tests/                                 # Testes unitários
    └── test_inventario_cli.py