from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema
import os

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pass1234@db/animals'
db = SQLAlchemy(app)

@app.route('/hello', methods=['GET'])
def hello():
    print('hello, hello, hello')
    dogs = Dog.query.all()
    # schema = DogSchema()
    # result = schema.dump(dog)

    print('running...')
    for dog in dogs:
        print('dog {0}:', dog)


    return jsonify({'woof': 'boo'})

@app.route('/nested')
def nested():
    return jsonify({"a": 3,
                    "b": True,
                    "c": None,
                    "d": "hello json",
                    "e": 3.14,
                    "f": [1, 2, 3],
                    "g": {"x":1, "y":2, "z":3}
                   })

@app.route('/echo', methods=['POST'])
def echo():
    # import IPython
    # from IPython import embed
    # embed() # this call anywhere in your program will start IPython
    # import pdb; pdb.set_trace()
    # IPython.start_ipython()
    return jsonify(request.json)

class Dog(db.Model):
    __tablename__ = "dogs"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    age = db.Column('age', db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

class DogSchema(Schema):
    class Meta:
        fields = ('id', 'name', 'age')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ['PORT']))
