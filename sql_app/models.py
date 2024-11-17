from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,JSON,Date,CHAR
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sql_app.database import engine,Base

from typing import List


class PC(Base):
    __tablename__="computadoras"
    id=Column(Integer,autoincrement=True,primary_key=True)
    marca=Column(String,nullable=False)
    descripcion=Column(String,nullable=False)
    memoria_ram=Column(String,nullable=False)
    almacenamiento=Column(String,nullable=False)
    sistema_operativo=Column(String,nullable=False)


class Celular(Base):
    __tablename__ = 'celulares'
    id = Column(Integer, primary_key=True, autoincrement=True)
    marca = Column(String, nullable=False)
    procesador = Column(String, nullable=False)
    ram = Column(String, nullable=False)
    almacenamiento = Column(String, nullable=False)
    sistema_operativo = Column(String, nullable=False)
   





class Tablets(Base):
    __tablename__ = 'tablets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    marca = Column(String, nullable=False)
    procesador = Column(String, nullable=False)
    ram = Column(String, nullable=False)
    almacenamiento = Column(String, nullable=False)
    sistema_operativo = Column(String, nullable=False)



   

   
       

Base.metadata.create_all(bind=engine)
