# Aladin Api

Desafio técnico usando o framework Django para buscar uma API externa, modificar e retornar dados.

### Pré-requisitos

1. `Python` na sua versão 3

### Instalação

1. Clone o repository:
   ```bash
   git clone https://github.com/beterrabaA/aladin_api_test
   ```
2. Acessar o diretório:
    ```bash
    cd aladin_api_test
   ```
3. Instalar as dependências:
   ```bash
   pip install -r requirements.txt 
   ```
4. Rodar a aplicação: 
    ```bash
    python manage.py runserver
   ```
   or
    ```bash
    python3 manage.py runserver
   ```

### Endpoints

- **`GET /api/v1/items/`**: Endpoint principal da aplicação. Responsável por buscar dados na API externa, realizar as modificações da regra de negócio e retornar os dados processados.
- **`GET /api/v1/schema/`**: Retorna o schema estruturado OpenAPI do projeto (gerado através do `drf-spectacular`).
- **`GET /api/v1/docs/`**: Disponibiliza a interface gráfica interativa do Swagger UI. Acesse esta rota pelo navegador para explorar a documentação completa da API e realizar testes manuais.

### Testes

Nesse projeto existe testes unitários.Para rodar execute o comando

```bash
    python manage.py test
```