from . import db, mm


class Project(db.Model):  # renamed from Tasks to Projects
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    servers = db.relationship('Server', primaryjoin="and_(Project.id==Server.project_id, ""Server.id)")  # uselist=False

    #  Проверяем, что имя содержит только буквы
    @db.validates('name')
    def validate_name(self, key, value):
        assert value.isalpha()
        return value

    def __init__(self, name):
        self.name = name

    def as_dict(self):
        return {'id': self.id, 'name': self.name}


class Server(db.Model):
    __tablename__ = 'server'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)  # FIXME: required=True not working

    #  Проверяем, что добавляемый project_id встречается меньше двух раз
    @db.validates('project_id')
    def validate_projects_count(self, key, value):
        projects_count = db.column_property(db.select([db.func.count(value)]))
        assert projects_count <= 2
        return value

    #  Проверяем, что имя содержит только буквы
    @db.validates('name')
    def validate_name(self, key, value):
        assert value.isalpha()
        return value

    def __init__(self, name, project_id):
        self.name = name
        self.project_id = project_id

    def as_dict(self):
        return {'id': self.id, 'name': self.name}


class ProjectSchema(mm.ModelSchema):
    class Meta:
        fields = ('id', 'name', 'servers')


class ServerSchema(mm.ModelSchema):
    class Meta:
        fields = ('id', 'name', 'project_id')


#  TODO: перенести верификацию в marshmallow
