## Instruções

### Intrudução
O Objetivo foi criar dois microsserviços, um para criar e autenticar usuários,
outro para cadastrar contatos após o cliente obter o token de autenticação.

### Instalações Local (Caso necessário)
* Nesse projeto foi utilizado o gerênciador de pacotes poetry.
  * Para instalar bastar seguir as instruções no site do [poetry](https://python-poetry.org/docs/)
* Crie uma virtualenv com o comando 
  ```
  $ poetry shell
  ```
* Para instalar as dependências utilize o comando:

```
$ poetry install
```

### Infraestrutura
* Nesses projetos são utilizados dois SQGDs:
  * Postgresql
  * MySQL

### Subir Infra e API
Para subir o ambiente, rode o comando

```
$ docker-compose up -d
```

#### Os containers que subirão são:
* postgresql_local
* mysql_local
* customer_service_api
* customer_auth_service_api

obs: As configurações das bases de dados são feitas no arquivo `api/config.py` 

### Tests
* Foram criados testes para verificar a integridade do funcionamento da aplicação,
  * Testes Unitários:
    * Localização dos testes unitários `tests/unit/test_contact.py`
    * Acesse o diretório do projeto ex: `cd mercafacil-challenge/customer-auth-service-api` e rode o comando `$ python -m pytest`:
  * Testes HTTP:
    * Para rodar é necessário ter a instalação do RestClient e rodar os testes 
      dentro do arquivo [POST.http](./tests/http/POST.http)

### Customer Service API
* Microsserviço com o objetivo de adicionar novos contatos
* Porta: 5000
* Endpoints:
  * `api/contacts`
    * Metodos: `POST`
    * Objetivo: Criar novos contatos
    * Informar nos headers:
      * authentication-token: qwopiejf3984yehfdeasfnn
    * 
      ```json
      PAYLOAD: {
        "contacts": [
          {
            "name": "macapa",
            "cellphone": "5541988315943"
          },
          {
            "name": "macapa",
            "cellphone": "5541988315943"
          },
        ]
      }
      ```
       ou 
      ```json
      PAYLOAD: 
          {
            "name": "macapa",
            "cellphone": "5541988315943"
          }
      ```

Ao criar um usuário, é necessário informar o domínio de e-mail como <b>macapa</b> ou <b>varejao</b>,
Ex: `teste@varejao.com` ou `teste@macapa.com`, pois isso define em qual base será cadastrado
o contrato.

Até por uma questão de segurança, caso um algum domínio de e-mail não previso tente cadastrar,
algum contato indevido.

### Customer Auth Service API
* Microsserviço com o objetivo de prover e autenticar o usuário
* Porta: 5001
* Endpoints:
  * `/api/users`
    * Metodos: `POST`
    * Objetivo: Criar um novo usuário
    * 
      ```json
      PAYLOAD: {
        "name": "Oscar da Silva",
        "email": "oscar@macapa.com",
        "password": "123"
      }
      ```

   * `/api/signin`
    * Metodos: `POST`
    * Objetivo: Realiza o login
    * 
      ```json
      PAYLOAD: {
        "email": "oscar@macapa.com",
        "password": "123"
      }
      ```
  * `/api/token/validate`
    * Metodos: `POST`
    * Objetivo: Valida o token enviado nos `headers` da requisição no `authentication-token`
    * 
      ```json
      authentication-token: ...
      ```