from server import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'password')


class PostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'content', 'author')
