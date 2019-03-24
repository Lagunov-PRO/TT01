from sqlalchemy import select, func
from sqlalchemy.orm import relationship, column_property, validates

from . import db, mm


class User(db.Model):  # renamed from Tasks to Projects
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    servers = db.relationship('Server')

    #  Checking that name has only letters
    @validates('name')
    def validate_name(self, value):
        assert value.isalpha()
        return value

    # Подсчёт колличества серверов в проекте
    # servers_count = column_property(select([func.count(Server.id)]).where(Server.project_id == id))

    # def __init__(self, name):
    #     self.name = name
    #
    # def as_dict(self):
    #     return {'id': self.id, 'name': self.name}


class Server(db.Model):
    __tablename__ = 'servers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    #  Checking that name has only letters
    @validates('name')
    def validate_name(self, value):
        assert value.isalpha()
        return value


class TaskSchema(mm.ModelSchema):
    class Meta:
        model = Task
