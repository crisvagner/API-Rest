from flask import request, jsonify
from ..models.models import Users, Posts
from server.instance import server
from db.services import db
import json

app = server.app


@app.route('/users', methods=['POST'])
def create_user():
    email = request.json['email']
    password = request.json['password']
    new_user = Users(email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Usuário criado com sucesso'})


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = Users.query.get(id)
    if user:
        user_dict = {
            'id': user.id,
            'email': user.email
        }
        return jsonify({'User': user_dict})
    return jsonify({'message': 'User Not Found'})


@app.route('/users', methods=['GET'])
def get_all_users():
    users = Users.query.all()
    if users:
        # users_list = [user.to_json() for user in users]
        users_list = []
        for user in users:
            user_dict = {
                'id': user.id,
                'email': user.email
            }
            users_list.append(user_dict)
        return jsonify({'Users': users_list})
    return jsonify({'message': 'Not Found'})


@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = Users.query.get(id)
    email = request.json['email']
    password = request.json['password']
    user.email = email
    user.password = password
    db.session.commit()
    return jsonify({'message': 'Usuário atualizado com sucesso'})


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = Users.query.get(id)
    posts = Posts.query.filter_by(user_id=user.id).all()
    for post in posts:
        db.session.delete(post)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'Usuário deletado com sucesso'})
