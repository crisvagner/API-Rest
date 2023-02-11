from flask import request, redirect, render_template, jsonify
from models.models import User, Post
from db.services import db
from server import server

app = server.app


@app.before_first_request
def create_tables():
    db.create_all()

# @app.route('/')
# def index():
#     users = User.query.all()
#     return render_template('index.html', users=users)


@app.route('/users', methods=['POST'])
def create_user():
    email = request.form['email']
    password = request.form['password']
    new_user = User(email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    # return redirect('/')
    jsonify({'message': 'usuário criado com sucesso'})


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    posts = Post.query.filter_by(user_id=user.id).all()
    for post in posts:
        db.session.delete(post)
    db.session.delete(user)
    db.session.commit()
    # return redirect('/')
    return jsonify({'message': 'usuário deletado com sucesso'})


@app.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    # return redirect('/')
    return jsonify({'message': 'post deletado com sucesso'})


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user:
        user_dict = {
            'id': user.id,
            'email': user.email
        }
        return jsonify({'user': user_dict})
    return jsonify({'message': 'erro ou n existe este usuario'})


@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    if users:
        users_list = []
        for user in users:
            user_dict = {
                'id': user.id,
                'email': user.email
            }
            users_list.append(user_dict)
        return jsonify({'users': users_list})
    return jsonify({'message': 'erro ou n existe usuarios'})


@app.route('/posts', methods=['GET'])
def get_all_posts():
    posts = Post.query.all()
    if posts:
        posts_list = []
        for post in posts:
            post_dict = {
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'user_id': post.user_id
            }
            posts_list.append(post_dict)
        return jsonify({'posts': posts_list})
    return jsonify({'message': 'erro ou n existe posts'})


# //////////////////////////////////////////////////////////////////////


# def create_user(email, password):
#     user = User(email=email, password=password)
#     db.session.add(user)
#     db.session.commit()
#     return user


# def get_user_by_id(user_id):
#     user = User.query.get(user_id)
#     return user


# def get_all_users():
#     users = User.query.all()
#     return users


# def create_post(title, content, user_id):
#     post = Post(title=title, content=content, user_id=user_id)
#     db.session.add(post)
#     db.session.commit()
#     return post


# def get_post(post_id):
#     post = Post.query.get(post_id)
#     return post


# def get_all_posts():
#     posts = Post.query.all()
#     return posts

# if __name__ == '__main__':
#     db.init_app(app)
#     ma.init_app(app)
#     server.run()
