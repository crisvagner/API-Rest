from controllers.PostController import PostController

post = PostController()


@app.route('/users/<id>/post/', 'POST')  # Rota Publica <<<
post.create()


@app.route('/users/<id>/post/<id>', 'DELETE')  # Rota Privada
post.delete()


@app.route('/users/<id>/post/<id>', 'GET')  # Rota Publica <<<
post.find()


@app.route('/users/<id>/post', 'GET')  # Rota Privada
post.findMany()


@app.route('/users/<id>/post/<id>', 'PUT')  # Rota Privada
post.update()
