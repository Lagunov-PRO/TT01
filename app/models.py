from sqlalchemy import select, func
from sqlalchemy.orm import relationship, column_property, validates

from . import db, mm


class Project(db.Model):  # renamed from Tasks to Projects
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    servers = db.relationship('Server')

    #  Проверяем, что имя содержит только буквы
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

    #  Проверяем, что добавляемый project_id встречается меньше двух раз
    @validates('project_id')
    def validate_projects_count(self, key, value):
        projects_count = column_property(select([func.count(value)]))
        assert projects_count <= 2
        return value

    #  Проверяем, что имя содержит только буквы
    @validates('name')
    def validate_name(self, key, value):
        assert value.isalpha()
        return value


class TaskSchema(mm.ModelSchema):
    class Meta:
        model = Task
