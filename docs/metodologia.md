# METODOLOGIA DE TRABALHO
## Inventário de Equipamentos de Rede

## 1. Introdução

Este documento descreve a metodologia utilizada para realizar o inventário dos equipamentos de rede de uma infraestrutura informática.

O objetivo é estabelecer um procedimento organizado para identificar, recolher, registar e atualizar as informações dos equipamentos.

## 2. Levantamento dos equipamentos

A primeira etapa consiste em identificar todos os equipamentos existentes na infraestrutura de rede.

Serão considerados equipamentos como:

- Routers;
- Switches;
- Firewalls;
- Access Points;
- Servidores;
- Bastidores de rede.

O levantamento deverá ser realizado com autorização do responsável pela infraestrutura.

## 3. Recolha de informações

Para cada equipamento serão recolhidas as seguintes informações:

| Informação | Descrição |
|---|---|
| ID | Código de identificação |
| Nome | Nome do equipamento |
| Tipo | Categoria do equipamento |
| Marca | Fabricante |
| Modelo | Modelo comercial |
| Número de série | Identificador do fabricante |
| Endereço IP | Endereço de gestão |
| Endereço MAC | Identificação da interface de rede |
| Localização | Local de instalação |
| Estado | Situação operacional |
| Observações | Informação adicional |

## 4. Identificação e classificação

Cada equipamento deverá possuir um identificador único.

Os equipamentos serão classificados de acordo com o seu tipo e função na infraestrutura.

Esta classificação permitirá facilitar a consulta e a organização do inventário.

## 5. Registo dos equipamentos

Após a recolha dos dados, as informações serão introduzidas no ficheiro de inventário.

O ficheiro principal será:

`inventario/inventario-equipamentos.csv`

Os dados deverão ser preenchidos de forma consistente, evitando duplicações e erros de identificação.

## 6. Verificação dos dados

Após o registo, será realizada uma verificação para confirmar:

- Correção dos endereços IP.
- Correspondência dos endereços MAC.
- Identificação correta da marca e modelo.
- Número de série corretamente registado.
- Localização física dos equipamentos.
- Estado operacional atualizado.

## 7. Atualização do inventário

Sempre que existir uma alteração na infraestrutura, o inventário deverá ser atualizado.

Exemplos:

- Instalação de um novo equipamento.
- Substituição de um switch.
- Alteração de um endereço IP.
- Desativação de um equipamento.
- Mudança de localização.

## 8. Utilização do GitHub

O GitHub será utilizado para armazenar os documentos e ficheiros do projeto.

Cada atualização relevante deverá ser acompanhada de uma descrição que permita identificar as alterações realizadas.

O histórico de versões permitirá acompanhar a evolução do trabalho.

## 9. Segurança

A recolha e o armazenamento das informações deverão respeitar as regras de segurança da organização.

Não deverão ser publicados dados de autenticação, palavras-passe ou informações confidenciais da infraestrutura.

## 10. Conclusão

A metodologia definida permite realizar o inventário de forma organizada, consistente e documentada.

A aplicação destas etapas contribuirá para melhorar a gestão, manutenção e controlo dos equipamentos de rede.
