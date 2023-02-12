from flask import request, jsonify
from ..models.models import Users, Posts
from server.instance import server
from db.services import db

app = server.app


@app.route('/posts', methods=['POST'])
def create_post():
    title = request.json['title']
    content = request.json['content']
    user_id = request.json['user_id']
    new_post = Posts(title=title, content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'message': 'Post criado com sucesso'})


@app.route('/users/<int:user_id>/posts/<int:post_id>', methods=['GET'])
def get_post(user_id, post_id):
    try:
        post = Posts.query.filter_by(
            user_id=user_id, id=post_id).first_or_404()
        if post:
            post_dict = {
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'user_id': post.user_id
            }
            return jsonify({'Post': post_dict})
    except:
        return jsonify({'message': 'Post Not Found'})


@app.route('/users/<int:user_id>/posts', methods=['GET'])
def get_all_posts(user_id):
    try:
        posts = Posts.query.filter_by(user_id=user_id).all()
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
            return jsonify({'Posts': posts_list})
    except:
        return jsonify({'message': 'Not Found'})


@app.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    post = Posts.query.get(id)
    title = request.json['title']
    content = request.json['content']
    post.title = title
    post.content = content
    db.session.commit()
    return jsonify({'message': 'Post atualizado com sucesso'})


@app.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Posts.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post deletado com sucesso'})
