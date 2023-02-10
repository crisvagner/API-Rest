from controllers.UserController import UserController

user = UserController()


@app.route('/users', 'POST')  # Rota Publica <<<
user.create()


@app.route('/users/<id>', 'DELETE')  # Rota Privada
user.delete()


@app.route('/users/<id>', 'GET')  # Rota Publica <<<
user.find()


@app.route('/users', 'GET')  # Rota Privada
user.findMany()


@app.route('/users/<id>', 'PUT')  # Rota Privada
user.update()
