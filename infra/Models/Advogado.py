from sqlalchemy import Column, String, Integer, ForeignKey
from infra.Configs.base import base

class Advogado(base):
    __tablename__ = "advogado"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    aob = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"Pessoa [id={self.id}, nome={self.nome}, aob={self.aob}]"