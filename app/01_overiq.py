from sqlalchemy import MetaData, Table, String, Column, Integer, ForeignKey, CheckConstraint, create_engine

engine = create_engine('postgresql://localhost/users_db')

metadata = MetaData()

servers = Table('servers', metadata,
                Column('id', Integer(), primary_key=True),
                Column('name', String(20), nullable=False),
                )
projects = Table('projects', metadata,
                 Column('id', Integer(), primary_key=True),
                 Column('name', String(20), nullable=False),
                 CheckConstraint("REGEXP_LIKE('^[a-zA-Z]+$')", name='no_digits'),
                 Column('server', Integer(), ForeignKey('servers.id')),
                 )

metadata.create_all(engine)
