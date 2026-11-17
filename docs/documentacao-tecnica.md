# DOCUMENTAÇÃO TÉCNICA
## Projeto: Inventário de Equipamentos de Rede

## 1. Apresentação

Este documento apresenta as características técnicas e a organização do projeto académico de inventário de equipamentos de rede.

O projeto pretende demonstrar a importância da identificação, organização e gestão dos equipamentos utilizados numa infraestrutura informática.

## 2. Arquitetura do inventário

O inventário será organizado através de ficheiros CSV, permitindo armazenar e consultar os dados dos equipamentos.

A documentação será mantida em formato Markdown e o GitHub será utilizado para armazenar e controlar as versões dos ficheiros.

## 3. Tipos de equipamentos

### 3.1 Router
Equipamento responsável pelo encaminhamento de pacotes de dados entre diferentes redes.

### 3.2 Switch
Equipamento utilizado para interligar dispositivos dentro de uma rede local (LAN).

### 3.3 Firewall
Equipamento ou solução de segurança responsável por controlar o tráfego de rede de acordo com regras definidas.

### 3.4 Access Point
Dispositivo que permite a ligação de equipamentos à rede através de tecnologia Wi-Fi.

### 3.5 Servidor
Equipamento que disponibiliza serviços e recursos aos restantes dispositivos da infraestrutura.

## 4. Estrutura dos dados

Cada equipamento será identificado através dos seguintes campos:

| Campo | Tipo de informação |
|---|---|
| ID | Identificador único |
| Equipamento | Nome do dispositivo |
| Marca | Fabricante |
| Modelo | Referência do equipamento |
| Número de série | Identificação individual |
| Endereço IP | IPv4 ou IPv6 |
| Endereço MAC | Endereço físico da interface |
| Localização | Local de instalação |
| Estado | Ativo, inativo ou manutenção |
| Observações | Informação complementar |

## 5. Exemplo de inventário

| ID | Equipamento | Marca | Endereço IP | Estado |
|---|---|---|---|---|
| 001 | Router | Cisco | 192.168.1.1 | Ativo |
| 002 | Switch | HP | 192.168.1.2 | Ativo |
| 003 | Access Point | Ubiquiti | 192.168.1.3 | Ativo |
| 004 | Firewall | Fortinet | 192.168.1.4 | Ativo |
| 005 | Servidor | Dell | 192.168.1.10 | Ativo |

*Nota: Os dados apresentados são meramente ilustrativos e não representam equipamentos reais.*

## 6. Tecnologias utilizadas

- GitHub: alojamento do projeto.
- Git: controlo de versões.
- Markdown: documentação técnica.
- CSV: armazenamento dos registos.

## 7. Organização do repositório

```text
inventario-equipamentos-rede/
│
├── README.md
├── .gitignore
│
├── docs/
│   ├── proposta-projeto.md
│   ├── metodologia.md
│   └── documentacao-tecnica.md
│
├── inventario/
│   └── inventario-equipamentos.csv
│
└── modelos/
    └── modelo-inventario.csv
```

## 8. Segurança e boas práticas

- Utilizar dados fictícios na demonstração académica.
- Não divulgar palavras-passe ou credenciais.
- Evitar publicar informações confidenciais.
- Manter os ficheiros organizados.
- Registar as alterações no GitHub.

## 9. Conclusão

A documentação técnica estabelece a estrutura e os critérios utilizados na elaboração do inventário.

Através deste projeto académico será possível demonstrar conhecimentos de redes informáticas, gestão de equipamentos, organização de informação e utilização de ferramentas de controlo de versões.
