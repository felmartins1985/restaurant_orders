# Projeto Restaurant Orders 🍳🫒

Consiste em uma aplicação para auxiliar na gestão do inventário e gerenciamento dos pedidos de uma Lanchonete fictícia. 

* Solucionado com a utilizando da linguagem Python

<br />

<details>
  <summary><strong>Descrição das soluções criadas:</strong></summary><br />

| Função/Classe | Descrição | Localização |
|---|---|---|
| `analyze_log` | Função que realiza a leitura dos arquivos contendo as informações dos pedidos realizados e gera o relatório desejado  | `src/analyze_log.py` |
| `TrackOrders` | Classe que simula um sistema de registro contínuo das informações de pedidos | `src/track_orders.py` |
| `InventoryControl` | Classe de gerenciamento do estoque de um estabelecimento | `src/inventory_control.py` |

<br />
</details>



### Estrutura do Projeto

```
.
├── data
│   ├──🔹 mkt_campaign.txt
│   ├──🔸 orders_1.csv
│   └──🔸 orders_2.csv
├── src
│   ├──🔹 analyze_log.py
│   ├──🔹 inventory_control.py
│   ├──🔸 main.py
│   └──🔹 track_orders.py
├──tests
│   └──🔸 __init__.py
├──🔸 dev-requirements.txt
├──🔸 pyproject.toml
├──🔸 README.md
├──🔸 requirements.txt
├──🔸 setup.cfg
└──🔸 setup.py

Legenda:
🔸 Arquivos desenvolvidos pela Trybe (não foram alterados).
🔹 Arquivos desenvolvidos por mim.

```



### Instruções

- Realize o clone do projeto e utilize os comandos a seguir:

```
Para instalar as dependências e iniciar as aplicações:
<-- na raiz do projeto -->
python3 -m venv .venv // para criar o ambiente virtual
source .venv/bin/activate // para ativar o ambiente virtual
python3 -m pip install -r dev-requirements.txt // instalação das dependências
```


### Execução da Aplicação
> No arquivo `main.py` contém os exemplos para execução da aplicação descritos abaixo:
>
> comando: python3 -m src.main


```
Retorno:

hamburguer
{'coxinha', 'pizza', 'misto-quente'}
{'segunda-feira', 'sabado'}
{'pao': 40, 'carne': 33, 'queijo': 48, 'molho': 8, 'presunto': 7, 'massa': 16, 'frango': 8}))
```

#### Campanha de publicidade
> comando: python3 -m src.analyze_log

Função cria o arquivo `data/mkt_campaign.txt` contendo as sequintes análises:

```
Qual o prato mais pedido por 'maria'?

Quantas vezes 'arnaldo' pediu 'hamburguer'?

Quais pratos 'joao' nunca pediu?

Quais dias 'joao' nunca foi à lanchonete?
```

```
Retorno:

hamburguer
1
{'coxinha', 'misto-quente', 'pizza'}
{'segunda-feira', 'sabado'}
```

#### Análises contínuas
> comando: python3 -m src.track_orders

```
Retorno:

Adicionando pedido: ('jorge', 'frango', 'domingo')
Adicionando pedido: ('maria', 'frango', 'segunda-feira')
Adicionando pedido: ('arnaldo', 'peixe', 'sábado')
Adicionando pedido: ('maria', 'carne', 'terça-feira')
Adicionando pedido: ('joao', 'salada', 'segunda-feira')
Prato mais pedido por Maria: carne
Prato nunca pedido por João: {'frango', 'peixe', 'carne'}
Dia(s) que João nunca visitou: {'sábado', 'domingo', 'terça-feira'}
Dia de maior movimento: segunda-feira
Dia de menor movimento: domingo
```


#### Controle de estoque
> comando: python3 -m src.inventory_control

```
Retorno:

Quantidade de ingredientes para comprar: {'pao': 1, 'carne': 1, 'queijo': 2, 'molho': 1, 'presunto': 0, 'massa': 1, 'frango': 0}
Pratos disponíveis no cardápio: {'misto-quente', 'coxinha', 'pizza', 'hamburguer'}
```
