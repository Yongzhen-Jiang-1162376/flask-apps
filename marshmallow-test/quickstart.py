import datetime as dt
from marshmallow import Schema, fields, post_load, validate, validates, ValidationError, INCLUDE
from pprint import pprint
import uuid


class User:
    def __init__(self, name, email, created_at = dt.datetime.now()):
        self.name = name
        self.email = email
        self.created_at = created_at
    
    def __repr__(self):
        # return '<User(name={self.name!r})'.format()
        return f'<User(name={repr(self.name)})'


class UserSchema(Schema):
    name = fields.String()
    email = fields.Email()
    created_at = fields.DateTime()

    @post_load
    def make_user(self, data, **kwargs):
        a = data
        b = kwargs
        return User(**data)


user = User(name='Monty', email='monty@python.org')
schema = UserSchema()
result = schema.dump(user)
pprint(result)

print()

json_result = schema.dumps(user)
pprint(json_result)

print()

filter_schema = UserSchema(only=('name', 'email'))
filter_result = filter_schema.dump(user)
pprint(filter_result)

print()

exclude_schema = UserSchema(exclude=('email',))
exclude_result = exclude_schema.dump(user)
pprint(exclude_result)

print()

user_data = {
    # 'created_at': '2014-08-11T05:26:03.869245',
    'email': 'ken@yahoo.com',
    'name': 'Ken'
}
schema = UserSchema()
result = schema.load(user_data)
pprint(result)

print()

user1 = User(name='Mick', email='mick@stones.com')
user2 = User(name='Keith', email='keith@stones.com')
users = [user1, user2]
# schema = UserSchema(many=True)
schema = UserSchema()
result = schema.dump(users, many=True)
pprint(result)

print()

try:
    result = UserSchema().load({'name': 'John', 'email': 'foo'})
except ValidationError as err:
    print(err.messages)
    print(err.valid_data)

print()

class BandMemberSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email()


user_data = [
    {'email': 'mick@stones.com', 'name': 'Mick'},
    {"email": "invalid", "name": "Invalid"},  # invalid email
    {"email": "keith@stones.com", "name": "Keith"},
    {"email": "charlie@stones.com"},  # missing "name"
]

try:
    BandMemberSchema().load(user_data, many=True)
except ValidationError as err:
    pprint(err.messages)
    pprint(err.valid_data)

print()


class UserSchema(Schema):
    name = fields.String(validate=validate.Length(min=1))
    permission = fields.String(validate=validate.OneOf(['read', 'write', 'admin']))
    age = fields.Integer(validate=validate.Range(min=18, max=40))

in_data = {'name': '', 'permission': 'invalid', 'age': 71}

try:
    UserSchema().load(in_data)
except ValidationError as err:
    pprint(err.messages)

print()

def validate_quantity(n):
    if n < 0:
        raise ValidationError('Quantity must be greater than 0.')
    if n > 30:
        raise ValidationError('Quantity must not be greater than 30.')


class ItemSchema(Schema):
    quantity = fields.Integer(validate=validate_quantity)

in_data = {'quantity': 31}
try:
    result = ItemSchema().load(in_data)
except ValidationError as err:
    print(err.messages)


class ItemSchema(Schema):
    quantity = fields.Integer()

    @validates('quantity')
    def validate_quantity(self, value):
        if value < 0:
            raise ValidationError('Quantity must be greater than 0.')
        if value > 30:
            raise ValidationError('Quantity must not be greater than 30.')

print()

class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True, error_messages={'required': 'Age is required.'})
    city = fields.String(
        required=True,
        error_messages={'required': {'message': 'City required', 'code': 400}}
    )
    email = fields.Email()

try:
    result = UserSchema().load({'email': 'foo@bar.com'})
except ValidationError as err:
    pprint(err.messages)


print()

class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)

result = UserSchema().load({'age': 42}, partial=('name',))
print(result)


print()

class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)

result = UserSchema().load({'age': 42}, partial=True)
pprint(result)


print()

class UserSchema(Schema):
    id = fields.UUID(load_default=uuid.uuid4)
    birthdate = fields.DateTime(dump_default=dt.datetime(2017, 9, 29))

user1 = UserSchema().load({})
pprint(user1)

pprint(UserSchema().dump({}))

print()

class UserSchema(Schema):
    class Meta:
        unknown = INCLUDE

