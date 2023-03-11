# Job Insights
[1/6] [Ciência da Computação](https://github.com/xitusz/Trybe/tree/main/04_Ci%C3%AAncia-da-Computa%C3%A7%C3%A3o)

---

## Sumário

- [Contexto](#contexto)
- [Habilidades Desenvolvidas](#habilidades-desenvolvidas)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Clonando Repositório](#clonando-repositório)
- [Instalando Dependências](#instalando-dependências)
- [Executando Aplicação](#executando-aplicação)
- [Executando Testes](#executando-testes)

---

## Contexto

* Projeto desenvolvido para colocar em prática conhecimentos adquiridos em Python

---

## Habilidades Desenvolvidas

* Utilizar o terminal interativo do Python.
* Utilizar estruturas condicionais e de repetição.
* Utilizar funções built-in do Python.
* Utilizar tratamento de exceções.
* Realizar a manipulação de arquivos.
* Escrever funções.
* Escrever testes com Pytest.
* Escrever seus próprios módulos e importá-los em outros códigos.

---

## Tecnologias Utilizadas

* Python

---

## Clonando Repositório:

* Clone o repositório
  ```sh
    git clone git@github.com:xitusz/job-insights.git
  ```

---

## Instalando Dependências

* Entre na pasta do repositório que você clonou:
  ```sh
    cd job-insights
  ```

* Crie o ambiente virtual
  ```sh
    python3 -m venv .venv && source .venv/bin/activate
  ```

* Instale as dependências
  ```sh
    python3 -m pip install -r dev-requirements.txt
  ```

* Se aparecer algum erro relacionado a 'wheel', instale-o
  ```sh
    python3 -m pip install wheel && python3 -m pip install -r dev-requirements.txt
  ```

---

## Executando Aplicação

* Entre na pasta do repositório que você clonou:
  ```sh
    cd job-insights
  ```

* Inicie o projeto com o flask e depois entre no 'http://localhost:5000/'
  ```sh
    flask run
  ```

---

## Executando Testes

* Os testes que eu desenvolvi foram 'tests/brazilian/test_brazilian_jobs.py', 'tests/counter/test_counter.py' e 'tests/sorting/test_sorting.py'. Os demais foram desenvolvidos pela [Trybe](https://www.betrybe.com/)

* Entre na pasta do repositório que você clonou:
  ```sh
    cd job-insights
  ```

* Crie o ambiente virtual
  ```sh
    python3 -m venv .venv && source .venv/bin/activate
  ```

* Rode os testes
  ```sh
    python3 -m pytest
  ```

---
