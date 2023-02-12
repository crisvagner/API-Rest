from ..models.models import Users, Posts
# from marshmallow import Schema, fields
from db.services import ma


# class UserSchema(Schema):
#     id = fields.Int(dump_only=True)
#     email = fields.Str(required=True)
#     password = fields.Str(required=True, load_only=True)


# class PostSchema(Schema):
#     id = fields.Int(dump_only=True)
#     title = fields.Str(required=True)
#     content = fields.Str(required=True)
#     author = fields.Nested(UserSchema, only=('id', 'email'))


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        load_instance = True


class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Posts
        load_instance = True
