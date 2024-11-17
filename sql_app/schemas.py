from pydantic import BaseModel
from typing import Optional
class SchemaPC(BaseModel):
    
    marca: str
    descripcion: str
    memoria_ram: str
    almacenamiento: str
    sistema_operativo: str


class SchemaCelular(BaseModel):
    
    marca: str
    procesador: str
    ram: str
    almacenamiento: str
    sistema_operativo: str

 
class SchemaTablet(BaseModel):
    
    marca: str
    procesador: str
    ram: str
    almacenamiento: str
    sistema_operativo: str

  

