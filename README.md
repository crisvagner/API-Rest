# API REST

## Sobre o projeto

O projeto é uma API Rest desenvolvida com Python e Flask onde é possível fazer um CRUD tanto de usuários como de postagens.

## Objetivo

Aprender sobre o desenvolvimento de APIs com Flask.

## Instruções

Para rodar o servidor da API Rest, digite os seguintes comandos:

```bash
cd api
pip install -r requirements.txt
python.exe -u main.py    
```

### Rotas para Usuário

Rota para registrar usuário:
método POST

request =  (apenas email e senha)

```bash
localhost:5000/users
```

Rota para retornar 1 usuário pelo id:
método GET

```bash
localhost:5000/users/id
```

Rota para retornar todos os usuários:
método GET

```bash
localhost:5000/users
```

Rota para atualizar 1 usuário:
método PUT

```bash
localhost:5000/users/id
```

Rota para deletar 1 usuário:
método DELETE

```bash
localhost:5000/users/id
```

### Rotas para Postagens

request = (apenas titulo,conteúdo e id do usuario autor)

Rota para registrar um post:
método POST

```bash
localhost:5000/posts
```

Rota para retornar 1 post de 1 usuário pelo id:
método GET

```bash
localhost:5000/users/user_id/posts/post_id
```

Rota para retornar todos os posts de 1  usuário:
método GET

```bash
localhost:5000/users/user_id/posts
```

Rota para atualizar 1 post:
método PUT

```bash
localhost:5000/posts/id
```

Rota para deletar 1 post:
método DELETE

```bash
localhost:5000/posts/id
```
