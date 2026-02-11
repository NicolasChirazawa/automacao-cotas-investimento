<div align=center>
  <img src="https://img.shields.io/static/v1?label=%20&labelColor=9cccf4&message=Python&color=grey&style=for-the-badge&logo=python&logoColor=black"/>
  <img src="https://img.shields.io/static/v1?label=%20&labelColor=fcbe96&message=Jupyter&color=grey&style=for-the-badge&logo=jupyter&logoColor=black"/>
</div> <br>

<div align="center">
  • <a href=#descricao>Descrição</a> 
  • <a href=#inicializar>Inicializando</a> 
  •
</div>

<h2 name="descricao">💻 Descrição</h2>
Um projeto abrangente sobre <Strong>fundos de investimento</Strong> (multimercado, pósfixado...) que se propõem a automatizar coleta de dados, e elucidar ideias a partir do 
choque destes com métricas. <br> 

<h2 name="inicializar">🚀 Iniciando</h2>

<h3>Softwares necessários</h3>

• <a href="https://www.python.org/ftp/python/pymanager/python-manager-25.2.msix">Python</a>;
<h6>Recomendação: Um editor de código <a href="https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user">(Visual Studio Code)</a> que tenha suporte ao 'Jupyter Notebook'; </h6>

<h3>Meios de acessar o projeto</h3>

<a href="https://github.com/NicolasChirazawa/automacao-cotas-investimento.git">Clone</a> o projeto ou <a href="https://github.com/NicolasChirazawa/automacao-cotas-investimento/archive/refs/heads/main.zip">baixe-o</a>; <br>

<h3>Baixar dependências</h3>

Há um arquivo na raiz do projeto <em>./requirements.txt</em> que mostra dependências irão ser instaladas, para usar o projeto, basta usar o comando abaixo:

```bash
pip install -r requirements.txt
```

<h3>⚙️ Como configurar?</h3>

<h4>'JSON'</h4>
Há um arquivo no caminho '/app/option_template.json' para configurar o projeto. <br> <br>

<h2 name="inicializar">📄 Funcionalidades </h2>
Há dois módulos principais:

<h3>🗂️ Planilhas</h3>
As planilhas são geradas na extensão '.CSV' <a href='https://en.wikipedia.org/wiki/Comma-separated_values'>(Comma Separated Values)</a> e podem ser reaproveitadas fora do sistema caso seja do seu interesse.

<h4>CVM</h4>
A planilha de 'CVM' <a href='https://www.infomoney.com.br/guias/cvm-comissao-de-valores-mobiliarios/'>(Comissão de Valores Mobiliários)</a> utiliza dos dados fornecidos diariamente, para construir uma planilha geral com os dados acumu

<h3>📈 Gráfico</h3>
