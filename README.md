# Music Stats API


## Stack

 - Python 3.6
 - Flask

## Desenvolvendo

Se não estiver usando docker, basta criar um virtual env e ativá-lo.

Para rodar a app, use o seguinte comando.

`python -m app.run`

## Rodando os testes

Para rodar todos os testes, utilize o seguinte comando na raiz do projeto:

`python -m nose`

Para rodar os testes de unidade, utilize o seguinte comando na raiz do projeto:

`python -m nose tests/unit`

Para rodar os testes de integração, utilize o seguinte comando na raiz do projeto:

`python -m nose tests/unit tests/integration`

Para medir o coverage, utilize o seguinte comando na raiz do projeto:

`python -m nose --with-coverage --cover-package=app  --cover-inclusive --cover-html`

## Pylint

Escreva código Python compatível com bom score no Pylint :heart:

`python $(which pylint) app`

## Docker

Toda a stack necessária para rodar a aplicação pode ser levantada através de um docker-compose. Nesse docker-compose, subimos um servidor Flask.

`docker-compose up`

A aplicação será exposta por padrão na porta 5000.