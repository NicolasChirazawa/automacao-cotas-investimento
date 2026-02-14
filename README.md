<h1 align="center">Automação de Cotas de Investimento</h1>

<p align="center">
  <img src="https://img.shields.io/static/v1?label=%20&labelColor=9cccf4&message=Python&color=grey&style=for-the-badge&logo=python&logoColor=black"/>
  <img src="https://img.shields.io/static/v1?label=%20&labelColor=fcbe96&message=Jupyter&color=grey&style=for-the-badge&logo=jupyter&logoColor=black"/>
</p>

<p align="center">
  <a href="#descricao">Descrição</a> •
  <a href="#como-iniciar">Como iniciar</a> •
  <a href="#funcionalidades">Funcionalidades</a> •
  <a href="#estrutura-do-projeto">Estrutura</a>
</p>

<h2 name="descricao"> Descrição </h2>

Projeto de automação para coleta, processamento e análise de dados de fundos de investimento, comparando a valorização de cotas com indicadores macroeconômicos como CDI e inflação (IPCA).

O objetivo é construir uma base estruturada para análise histórica e geração de gráficos comparativos.

---

<h2 name="como-iniciar">Como iniciar</h2>

### 1️⃣ Softwares necessários

- [Python](https://www.python.org/downloads/)

Recomendação: utilizar um editor como o [Visual Studio Code](https://code.visualstudio.com/) com suporte a Jupyter Notebook.

### 2️⃣ Acessando o projeto

Clone o repositório:

```bash
git clone https://github.com/NicolasChirazawa/automacao-cotas-investimento.git
```

Ou baixe o arquivo `.zip` diretamente pelo GitHub.

### 3️⃣ Instalação de dependências

O projeto possui um arquivo `requirements.txt` na raiz contendo as dependências necessárias.

Execute:

```bash
pip install -r requirements.txt
```

### 4️⃣ Configuração

Existe um arquivo em:

```
/app/options_template.json
```

Utilize-o como base para configurar as opções do projeto.

---

<h2 name="funcionalidades"> Funcionalidades </h2>

O projeto está dividido em dois principais módulos:

### Planilhas

<details>
  <summary><strong>CVM</strong></summary>

A CVM ([Comissão de Valores Mobiliários](https://www.infomoney.com.br/guias/cvm-comissao-de-valores-mobiliarios/)) é responsável por fiscalizar e garantir a transparência do mercado de capitais brasileiro.

Funcionalidades:

- Download e descompactação de planilhas `.zip` da CVM por período selecionado;  
- Criação e filtragem de dados por investimento;
- Cálculo da valorização da cota;

<sub>Desde maio de 2022, os arquivos passaram a ser disponibilizados em formato `.csv` compactado.</sub>

</details>

<details>
  <summary><strong>Métricas – Ipeadata</strong></summary>

O Ipeadata ([Instituto de Pesquisa Econômica Aplicada](https://www.ipea.gov.br/portal/)) é uma base pública com séries históricas macroeconômicas do Brasil.

Atualmente o projeto trabalha com:

<details>
  <summary><strong>CDI (Certificado de Depósito Interbancário)</strong></summary>

Taxa de juros de empréstimos interbancários de curtíssimo prazo, amplamente utilizada como indexador de investimentos como CDBs, LCIs, LCAs e fundos.

</details>

<details>
  <summary><strong>Inflação (IPCA)</strong></summary>

Índice Nacional de Preços ao Consumidor Amplo, utilizado como principal indicador oficial de inflação no Brasil.

</details>

Resultados gerados:

- Construção de planilhas do CDI diário;
- Cálculo da valorização acumulada do CDI;

</details>

---

### Gráficos

- Geração de gráfico comparativo entre o preço de cotas dado um período de tempo;
- Valorização de cota perante a indicadores econômicos; - Em breve -
- Simulação de valor de resgate; - Em breve -

---

<h2 name="estrutura-do-projeto"> Estrutura do Projeto </h2>

```
app
├── data
│   └── (dados baixados e processados)
├── options_template.json
└── src
    ├── graphics
    │   └── produce_graphic_by_data.ipynb
    ├── spreadsheets
    │   ├── cvm
    │   │   ├── download_cvm_data.ipynb
    │   │   └── process_cvm_data.ipynb
    │   └── metrics
    │       └── cdi
    │           ├── process_cdi_data.ipynb
    │           └── valuation_cdi_data.ipynb
    └── utils
        ├── classes
        │   ├── cvm_link.py
        │   ├── ipea.py
        │   └── pandas_dataframe.py
        └── functions
            └── date_transform.py
```
---
