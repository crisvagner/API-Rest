from marshmallow import Schema, fields
from .UserSchema import UserSchema


class PostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    author = fields.Nested(UserSchema, only=('id', 'email'))
