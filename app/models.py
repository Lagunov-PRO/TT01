from marshmallow import ValidationError

from . import db, mm


class Project(db.Model):  # renamed from Tasks to Projects
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    servers = db.relationship('Server', primaryjoin="and_(Project.id==Server.project_id)")  # uselist=False

    #  Проверяем, что имя содержит только буквы
    @db.validates('name')
    def validate_name(self, key, value):
        if not value.isalpha():
            raise ValidationError('В названии проекта должны быть только буквы.')
        return value

    def __init__(self, name):
        self.name = name

    def as_dict(self):
        return {'id': self.id, 'name': self.name}


class Server(db.Model):
    __tablename__ = 'server'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False, unique=True)  # FIXME: required=True not working

    #  Проверяем, что добавляемый project_id встречается меньше двух раз

    @db.validates('project_id')
    def check_project_has_3_servers(self, key, project_id):
        projects_id_list = Server.query.filter_by(project_id=project_id).all()
        if len(projects_id_list) == 3:
            raise ValidationError('В одном проекте не больше трёх серверов.')
        return project_id

    #  Проверяем, что имя содержит только буквы
    @db.validates('name')
    def validate_name(self, key, value):
        if not value.isalpha():
            raise ValidationError('В названии сервера должны быть только буквы.')
        return value


    def __init__(self, name, project_id):
        self.name = name
        self.project_id = project_id

    def as_dict(self):
        return {'id': self.id, 'name': self.name}


#  Custom validators
def check_server_without_project(data):
    if not data:
        raise ValidationError('Нельзя добавлять сервера без проектов.')


class ProjectSchema(mm.ModelSchema):
    class Meta:
        fields = ('id', 'name')


class ServerSchema(mm.ModelSchema):
    class Meta:
        fields = ('id', 'name', 'project_id')


#  TODO: перенести верификацию в marshmallow
