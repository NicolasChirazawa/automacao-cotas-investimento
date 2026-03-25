<h1 align="center">Automação de Cotas de Investimento</h1>

<p align="center">
  <img src="https://img.shields.io/static/v1?label=%20&labelColor=9cccf4&message=Python&color=grey&style=for-the-badge&logo=python&logoColor=black"/>
  <img src="https://img.shields.io/static/v1?label=%20&labelColor=fcbe96&message=Jupyter&color=grey&style=for-the-badge&logo=jupyter&logoColor=black"/>
    <img src="https://img.shields.io/static/v1?label=%20&labelColor=ffffff&message=Sphinx&color=grey&style=for-the-badge&logo=sphinx&logoColor=black"/>
</p>

<p align="center">
  <a href="#inicio-rapido">Início Rápido</a> •
  <a href="#documentacao">Documentação</a> •
  <a href="#funcionalidades">Funcionalidades</a> •
  <a href="#estrutura-do-projeto">Estrutura</a> •
</p>

Projeto de automação para coleta, processamento e análise de dados de fundos de investimento.

O objetivo é construir uma base estruturada para análise histórica, geração de gráficos comparativos e simulações de investimento.

---

<h2 name="inicio-rapido">Início Rápido</h2>

### 1️⃣ Pré-requisitos

- [Python](https://www.python.org/downloads/)

Recomendação: utilizar um editor como o [Visual Studio Code](https://code.visualstudio.com/) com suporte a Jupyter Notebook.

### 2️⃣ Clonar o Projeto

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

Existe um arquivo em `/app/options_template.json`. <br>
Utilize-o como base para configurar as opções do projeto.

---

<h2 name="documentacao">Documentação</h2>

A documentação foi desenvolvida usando o 'Sphinx', a fim de proporcionar um formaro padrão, e compreensível.
Ela está disponibilizada dentro da pasta `/docs/source/index.rst`.

---

<h2 name="funcionalidades"> Funcionalidades </h2>

O projeto está dividido em três principais módulos:

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
  <summary><strong> 🔜 Inflação (IPCA)</strong></summary>

Índice Nacional de Preços ao Consumidor Amplo, utilizado como principal indicador oficial de inflação no Brasil.

</details>

Resultados gerados:

- Construção de planilhas do CDI diário;
- Cálculo da valorização acumulada do CDI;

</details>

---

### Gráficos

  <details>
    <summary>Geração de gráfico comparativo entre o preço de cotas num período de tempo;</summary>
    <img src="https://raw.githubusercontent.com/NicolasChirazawa/automacao-cotas-investimento/refs/heads/main/imgs/Screenshot_1.png">
  </details>
  <details>
    <summary>Valorização de cotas diante indicadores econômicos;</summary>
    <img src="https://raw.githubusercontent.com/NicolasChirazawa/automacao-cotas-investimento/refs/heads/main/imgs/Screenshot_2.png">
  </details>

---

### Simulação

  Baseado no processamento das planilhas, gerar estimativas do valor inicial e final perante a valorização de cotas de investimento, implementando lucro bruto e líquido (usando a taxação do IOF e IR).

  <details>
    <summary>Demonstração;</summary>
    <img src="https://raw.githubusercontent.com/NicolasChirazawa/automacao-cotas-investimento/refs/heads/main/imgs/Screenshot_3.png">
  </details>

---

<h2 name="estrutura-do-projeto"> Estrutura do Projeto </h2>

```
├── app/
│   ├── src/
│   │   ├── graphics/
│   │   │   ├── quota_metric_valuation.ipynb
│   │   │   └── quota_price_evolution.ipynb
│   │   ├── redeem/
│   │   │   ├── errors_redeem.py
│   │   │   └── redeem_simulation.ipynb
│   │   ├── spreedsheets/
│   │   │   ├── cvm/
│   │   │   │   ├── download_cvm_data.ipynb
│   │   │   │   └── process_cvm_data.ipynb
│   │   │   └── metrics/
│   │   │       └── cdi/
│   │   │           ├── process_cdi_data.ipynb
│   │   │           └── valuation_cdi_data.ipynb
│   │   └── utils/
│   │       ├── classes/
│   │       │   ├── cvm_link.py
│   │       │   ├── ipea_link.py
│   │       │   └── pandas_dataframe.py
│   │       └── functions/
│   │           ├── date_transform.py
│   │           └── tax_calculation.py
│   └── options_template.json
└── requirements.txt

```
