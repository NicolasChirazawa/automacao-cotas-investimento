<div align=center>
  <img src="https://img.shields.io/static/v1?label=%20&labelColor=9cccf4&message=Python&color=grey&style=for-the-badge&logo=python&logoColor=black"/>
  <img src="https://img.shields.io/static/v1?label=%20&labelColor=fcbe96&message=Jupyter&color=grey&style=for-the-badge&logo=jupyter&logoColor=black"/>
</div> <br>

<div align="center">
  • <a href=#descricao>Descrição</a> 
  • <a href=#inicializar>Como iniciar?</a> 
  • <a href=#funcionalidades>Funcionalidades</a>
  • <a href=#estrutura>Estrutura</a> 
  •
</div>

<h2 name="descricao">Descrição</h2>
Um projeto para automatizar a coleta de dados de investimento e analisar entre choques destes com medidos macroeconômicos, a exemplo do CDI e da inflação. <br> 

<h2 name="inicializar">Como iniciar</h2>

<h3>1° Passo: Softwares necessários</h3>

• <a href="https://www.python.org/ftp/python/pymanager/python-manager-25.2.msix">Python</a>;
<h6>Recomendação: Um editor de código (<a href="https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user">Visual Studio Code</a>) que tenha suporte ao 'Jupyter Notebook'; </h6>

<h3>2° Passo: Meios de acessar o projeto</h3>

<a href="https://github.com/NicolasChirazawa/automacao-cotas-investimento.git">Clone-o</a> ou <a href="https://github.com/NicolasChirazawa/automacao-cotas-investimento/archive/refs/heads/main.zip">baixe-o</a>; <br>

<h3>3° Passo: Instalação de dependências</h3>

Há um arquivo na raiz do projeto <em>./requirements.txt</em> que dispõem as dependências a serem instaladas. Para utilizar usar o projeto, com a mesma estrutura que desenvolvi, basta usar o comando abaixo:

```bash
pip install -r requirements.txt
```

<h3>4° Passo: Configuração do JSON</h3>
Há um arquivo no caminho <em>'/app/option_template.json'</em> para configurar as opções disponibilizadas no projeto. <br> <br>

<h2 name="funcionalidades">Funcionalidades </h2>
Há dois módulos principais de funcionalidades:

<h3>🗂️ Planilhas</h3>

<details>
  <summary> <h4>CVM</h4> </summary>
  
  A CVM (<a href='https://www.infomoney.com.br/guias/cvm-comissao-de-valores-mobiliarios/'>Comissão de Valores Mobiliários</a>) é um órgão fundamental para construção 
  de segurança do investidor, realizando a fiscalização e mantendo a transparência do mercado de capital brasileiro.
    <br> <br>
    • Download e dezip de planilhas da CVM através de datas a sua escolha [1]; <br>
    • Criação e filtragem de data das planilhas por investimento; <br>
    • Cálculo da valorização da cota de investimento; <br> 
    <h6>[1]: Desde de maio de 2022, os arquivos passavam a ser '.csv' zippados.</h6>
</details> 

<details>
  <summary> <h4>Métricas - Ipeadata</h4> </summary>

  O Ipeadata (<a href="https://www.ipea.gov.br/portal/component/assuntos/interna?id=216">Instituto de Pesquisa Econômica Avançada</a>) é uma base dados pública que abrange séries históricas anuais, mensais e diárias sobre diversos registros macroeconômicos, financeiros, regionais e sociais do Brasil. Está sendo trabalhado com as seguintes métricas:
  
  - CDI (Certificado de Depósito Interbancário);
  - Inflação - em breve -;
    <br> <br>
</details> 

<h3>📈 Gráficos</h3>

<h2 name="estrutura">📦 Estrutura do Projeto </h2>

```
┌─ app
│  ┌─ * data
│  │  ├─ /*/Todos os dados baixados e processados ao longo do projeto */
│  ├─ options_template.json
│  └─ src
│     ├─ graphics
│     │  └─ produce_graphic_by_data.ipynb
│     ├─ spreedsheets
│     │  ├─ cvm
│     │  │  ├─ download_cvm_data.ipynb
│     │  │  └─ process_cvm_data.ipynb
│     │  └─ metrics
│     │     └─ cdi
│     │        ├─ process_cdi_data.ipynb
│     │        └─ valuation_cdi_data.ipynb
│     └─ utils
│        ├─ classes
│        │  ├─ cvm_link.py
│        │  ├─ ipea.py
│        │  └─ pandas_dataframe.py
│        └─ functions
│           └─ date_transform.py
```
