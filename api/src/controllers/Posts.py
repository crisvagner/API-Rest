from flask import request, jsonify
from server import app, db

from src.schemas import PostSchema
from src.models import Posts

post_schema = PostSchema()
posts_schema = PostSchema(many=True)


@app.route('/posts', methods=['POST'])
def create_post():
    try:
        title = request.json['title']
        content = request.json['content']
        user_id = request.json['user_id']

        new_post = Posts(title=title, content=content, user_id=user_id)

        db.session.add(new_post)
        db.session.commit()

        return jsonify({'message': 'Post criado com sucesso'}), 200

    except Exception as error:
        return jsonify({'message': error}), 500


@app.route('/users/<int:user_id>/posts/<int:post_id>', methods=['GET'])
def get_post(user_id, post_id):
    try:
        post = Posts.query.filter_by(
            user_id=user_id, id=post_id).first_or_404()
        post_dict = posts_schema.dump(post)

        return jsonify({'Post': post_dict}), 200

    except:
        return jsonify({'message': 'Post Not Found'}), 404


@app.route('/users/<int:user_id>/posts', methods=['GET'])
def get_all_posts(user_id):
    try:
        posts = Posts.query.filter_by(user_id=user_id).all()
        posts_dict = posts_schema.dump(posts)

        return jsonify({'Posts': posts_dict}), 200

    except:
        return jsonify({'message': 'Not Found'}), 404


@app.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    try:
        post = Posts.query.get(id)
        title = request.json['title']
        content = request.json['content']

        post.title = title
        post.content = content
        db.session.commit()

        return jsonify({'message': 'Post atualizado com sucesso'}), 200

    except Exception as error:
        return jsonify({'message': error}), 500


@app.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    try:
        post = Posts.query.get(id)
        db.session.delete(post)
        db.session.commit()

        return jsonify({'message': 'Post deletado com sucesso'}), 200

    except Exception as error:
        return jsonify({'message': error}), 500
