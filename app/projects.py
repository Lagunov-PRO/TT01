from flask import Blueprint, jsonify, request, abort
from app import db
from .models import Project, ProjectSchema, Server, ServerSchema

db.create_all()
db.session.commit()

projects = Blueprint('projects', __name__)


@projects.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    data = ProjectSchema(many=True).dump(projects).data
    return jsonify(data)


@projects.route('/projects', methods=['POST'])
def add_project():
    if not request.is_json or 'name' not in request.json:
        abort(400)

    project = Project(request.json['name'])
    db.session.add(project)
    db.session.commit()

    return '', 200


@projects.route('/servers', methods=['POST'])
def add_server():
    if not request.is_json or 'name' not in request.json:
        abort(400)

    name = request.json['name']
    project = request.json['project_id']
    new_server = Server(name, project)
    db.session.add(new_server)
    db.session.commit()

    return '', 200


@projects.route('/servers', methods=['GET'])
def get_servers():
    server = Server.query.all()
    data = ServerSchema(many=True).dump(server).data
    return jsonify(data)


@projects.route('/servers/<int:id>', methods=['PUT'])
def update_servers(id):
    server = Server.query.get(id)
    name = request.json['name']
    project_id = request.json['project_id']

    server.name = name
    server.project_id = project_id

    db.session.commit()

    return '', 200


@projects.route('/servers/<int:id>/delete', methods=['DELETE'])
def delete_server(id):

    server = Server.query.filter(Server.id == id).first()
    if not server:
        return '', 404  # tuple - 1-ый элемент - ответ, 2 - код статуса

    db.session.delete(server)
    db.session.commit()

    return '', 200

