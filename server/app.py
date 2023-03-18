#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()
    if animal:
        # attributes = ['name', 'species', 'zookeeper']
        # listElems = [f'<li>{animal.attr}</li>' for attr in Animal.keys()]
        response = f'''
            <ul>Name: {animal.name}</ul>
            <ul>Species: {animal.species}</ul>
            <ul>Zookeeper: {animal.zookeeper.name}</ul>
            <ul>Enclosure: {animal.enclosure.environment}</ul>
        '''
        return make_response(response, 200)

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()
    res = ""
    res += f"<ul>Name: {zookeeper.name}</ul>"
    res += f"<ul>Birthday: {zookeeper.birthday}</ul>"
    res += f"<ul>Animals: {zookeeper.animals}</ul>"


    return make_response(res, 200)

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enc = Enclosure.query.filter(Enclosure.id == id).first()
    res = ""
    res += f"<ul>Environment: {enc.environment}</ul>"
    res += f"<ul>Open to Visitors: {enc.open_to_visitors}</ul>"
    res += f"<ul>Animals: {enc.animals}</ul>"

    return make_response(res, 200)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
