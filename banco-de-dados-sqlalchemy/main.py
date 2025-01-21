from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

#as tabelas
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True,autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self,nome, email,senha,ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo

class Livro(Base):
    __tablename__ = "livros"
    id = Column("id", Integer, primary_key=True,autoincrement=True)
    titulo = Column("titulo", String)
    qtde_paginas = Column("qtde_paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id"))

    def __init__(self, titulo,qtde_paginas,dono):
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.dono = dono


Base.metadata.create_all(bind=db)

#CRUD - Create, Read, Update, Delete

#C - Create
usuario = Usuario(nome="Tiago", email="tiago@gmail.com",senha="123123")
usuario1 = Usuario(nome="Diogo", email="diogo@gmail.com",senha="123123")
usuario2 = Usuario(nome="Aline", email="aline@gmail.com",senha="123123")
session.add(usuario)
session.add(usuario1)
session.add(usuario2)
session.commit()

# R - Read
#lista_usuarios = session.query(Usuario).all()
usuario_tiago = session.query(Usuario).filter_by(email="tiago@gmail.com").first()
usuario_diogo = session.query(Usuario).filter_by(email="diogo@gmail.com").first()
usuario_aline = session.query(Usuario).filter_by(email="aline@gmail.com").first()
#print(usuario_aline)
print(usuario_aline.nome)
print(usuario_aline.email)

livro = Livro(titulo="Filho do Vento",qtde_paginas=1000,dono=usuario_tiago.id)
session.add(livro)
session.commit()

#U - Update
usuario_tiago.nome = "Bernardes"
session.add(usuario_tiago)
session.commit()

#D - Delete
session.delete(usuario_aline)
session.commit()