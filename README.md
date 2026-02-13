<div align=center>
  <img src="https://img.shields.io/static/v1?label=%20&labelColor=9cccf4&message=Python&color=grey&style=for-the-badge&logo=python&logoColor=black"/>
  <img src="https://img.shields.io/static/v1?label=%20&labelColor=fcbe96&message=Jupyter&color=grey&style=for-the-badge&logo=jupyter&logoColor=black"/>
</div> <br>

<div align="center">
  • <a href=#descricao>Descrição</a> 
  • <a href=#inicializar>Inicializando</a> 
  • <a href=#estrutura>Estrutura</a> 
  • <a href=#funcionalidades>Funcionalidades</a>
  •
</div>

<h2 name="descricao">💻 Descrição</h2>
Um projeto para automatizar a coleta de dados de investimento e analisar, baseado no histórico destes, e com medidos macroeconômicos, como o CDI e a inflação. <br> 

<h2 name="inicializar">🚀 Iniciando</h2>

<h3>Softwares necessários</h3>

• <a href="https://www.python.org/ftp/python/pymanager/python-manager-25.2.msix">Python</a>;
<h6>Recomendação: Um editor de código (<a href="https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user">Visual Studio Code</a>) que tenha suporte ao 'Jupyter Notebook'; </h6>

<h3>Meios de acessar o projeto</h3>

<a href="https://github.com/NicolasChirazawa/automacao-cotas-investimento.git">Clone-o</a> ou <a href="https://github.com/NicolasChirazawa/automacao-cotas-investimento/archive/refs/heads/main.zip">baixe-o</a>; <br>

<h3>Baixar dependências</h3>

Há um arquivo na raiz do projeto <em>./requirements.txt</em> que dispõem as dependências a serem instaladas. Para utilizar usar o projeto, com a mesma estrutura que desenvolvi, basta usar o comando abaixo:

```bash
pip install -r requirements.txt
```

<h3>⚙️ Como configurar?</h3>

<h4>'JSON'</h4>
Há um arquivo no caminho <em>'/app/option_template.json'</em> para configurar as opções disponibilizadas no projeto. <br> <br>

<h2 name="estrutura">📦 Estrutura do Projeto </h2>

```
┌─ app
│  ┌─ * data
│  │  ├─ /*/Todos os daods gerados ao longo do projeto */
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

<h2 name="funcionalidades">📄 Funcionalidades </h2>
Há dois módulos principais:

<h3>🗂️ Planilhas</h3>
As planilhas são geradas na extensão '.csv' (<a href='https://en.wikipedia.org/wiki/Comma-separated_values'>Comma Separated Values</a>) e podem ser reaproveitadas fora do sistema caso seja do seu interesse.

<h4>CVM</h4>
É baixado as planilhas da 'CVM' (<a href='https://www.infomoney.com.br/guias/cvm-comissao-de-valores-mobiliarios/'>Comissão de Valores Mobiliários</a>) baseado nos meses da sua escolha*. Após o 'download', é fornecido a opção da filtragem pelos investimentos que também decidiu.

<h6>* Desde de maio de 2022, os arquivos passavam a ser '.csv' zippados.</h6>

<h4>Métricas</h4>
É consultado algumas das bases de dados que o 'Ipeadata' disponibiliza para construir métricas que serão importantes para comparações da evolução do histórico de seus investimentos escolhidos. Estas são: <br> <br>

- CDI: Certificado de D  epósito interbancário;
- Inflação;

<h3>📈 Gráficos</h3>
