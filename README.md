<h1 align="center">
    <img alt="Proffy" src=".github/logo.png" height="100px" /><br/>
    Python | Selenium | Requests
</h1>

<p align="center">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/T635/P.A.I.F?style=social">&nbsp;
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/T635/P.A.I.F?style=social">&nbsp;
  <img alt="GitHub language count" src="https://img.shields.io/github/stars/T635/P.A.I.F?style=social">&nbsp;
</p>
<p align="center">
  <a href="#bookmark-sobre">Sobre</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rocket-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#boom-como-executar">Como Executar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>
<br/>

## Sobre
O **P.A.I.F** é uma aplicação desktop feita para automatizar o processo de postagem de imagens em grupos do Facebook, para isto foi necessário fazer analisar todas as requisições http/https feitas entre o navegador e a plataforma após, elas foram reproduzidas no programa.

## Tecnologias

- [Python](https://www.python.org/)
- [Selenium](https://selenium-python.readthedocs.io/)
- [Requests](https://requests.readthedocs.io/en/master/)

## Como Executar

- ### **Pré-requisitos**

  - É **necessário** possuir o **[Python 3.8](https://www.python.org/)** instalado.
  - É **necessário** possuir o **[Git](https://git-scm.com/)** instalado e configurado.
  - Também, é **preciso** ter o gerenciador de pacotes **[PIP](https://pip.pypa.io/en/stable/installing/)**.
  - É **essencial** ter o **[Selenium](https://selenium-python.readthedocs.io/)** .
  - Por fim, é necessário o driver de seu **[navegador](https://selenium-python.readthedocs.io/installation.html#drivers)** instalado.

1. Faça um clone do repositório:

```sh
  $ git clone https://github.com/T635/P.A.I.F.git
```

2. Executando a Aplicação:

```sh
  # Caso use linux, instale o driver na pasta /usr/local/bin/
  # Para qualquer outro S.O faz-se necessário modificar a 10° linha do arquivo functions.py para a localização real do driver
  $ cd P.A.I.F
  $ python3.8 main.py
```



