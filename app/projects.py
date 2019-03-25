from flask import Blueprint, jsonify, request, abort
from app import db
from .models import Project, ProjectSchema, Server, ServerSchema

tasks = Blueprint('projects', __name__)


@tasks.route('/api/projects', methods=['GET'])
def get_projects():
    # FIXME: исправить
    projects = Project.query.all()
    data = ProjectSchema(many=True).dump(projects).data
    return jsonify(data)


@tasks.route('/api/projects', methods=['POST'])
def add_project():
    if not request.is_json or 'name' not in request.json:
        abort(400)

    project = Project(request.json['name'])
    db.session.add(project)
    db.session.commit()

    return '', 200


@tasks.route('/api/servers', methods=['POST'])
def add_server():
    if not request.is_json or 'name' not in request.json:
        abort(400)

    server = Server(request.json['name'])
    db.session.add(server)
    db.session.commit()

    return '', 200


@tasks.route('/api/servers', methods=['GET'])
def get_servers():
    # FIXME: исправить
    server = Project.query.all()
    data = ProjectSchema(many=True).dump(server).data
    return jsonify(data)


@tasks.route('/api/servers/<int:id>', methods=['DELETE'])
def delete_server(id):

    server = Server.query.filter(Server.id == id).first()
    if not server:
        return '', 404  # tuple - 1-ый элемент - ответ, 2 - код статуса

    db.session.delete(server)
    db.session.commit()

    return '', 200

