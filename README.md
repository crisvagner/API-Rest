## API REST

### Sobre o projeto

O projeto é um sistema de registro e login, com acesso a uma pagina onde o usuário teria um sistema de crud. A API Rest foi desenvolvida com Python e Flask e o Front End ainda não finalizei mas a ideia seria desenvolve-lo com React e fazer a integração com a API em Flask.

### Objetivo

Aprender sobre React, Flask e integração entre o Back-End e o Fron-End.

### Observações

Apenas a API esta funcionando embora não esteja finalizada, o fron-end do projeto não foi finalizado.

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
