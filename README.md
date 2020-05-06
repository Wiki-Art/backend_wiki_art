# history project

## Sobre o projeto
O projeto visa a criação de um ambiente virtual para divulgação e produção de conteúdo sobre a arte barroca presente nas Igrejas do período colonial brasileiro. Além de fornecer de modo acessível as grande obras presentes nestes magníficos patrimônios de nossa cultura, busca-se ainda detectar as mais variadas influências presentes na produção do barroco brasileiro, tais como gravuras europeias, trechos de livros que contam as histórias dos santos e da Igreja, folhetos litúrgicos, entre outros.

## Motivação 
A motivação deste projeto é para estudo e um melhor entendimento da tecnologia GraphQL, pois ao realizar 
estudos iniciais desta tecnologia no 1º LabootCamp promovido pelo LABHacker. Foi definido este tema pois
é um tema real referente a tese de mestrado do historiador Rafael Lima Meireles de Queiroz.


## Configurações Iniciais
1. Criar um arquivo na pasta **core** do projeto com o nome **settings.ini**

```ini
[settings]
DEBUG=True
SECRET_KEY=secret_key
ALLOWED_HOSTS=['127.0.0.1', 'localhost', '0.0.0.0']
TIME_ZONE=America/Sao_Paulo
LANGUAGE_CODE=pt-br
NAME=mydatabase
USER=user
HOST=127.0.0.1
PORT=5432
```

## Iniciando o projeto
1. Instale as dependências do ambiente virtual
```console
pipenv install
```

2. Execute as migrations
```console
pipenv run src/manage.py makemigrations
pipenv run src/manage.py migrate
```

3. Inicie o projeto
```console
pipenv run src/manage.py runserver
```
O projeto irá iniciar na porta padrão 8000 e tendo como host o 127.0.0.1
