from sqlalchemy import Column, String, Integer, Float, ForeignKey
from infra.Configs.base import base

class Motivo(base):
    __tablename__ = "motivo"
    # id, nome

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)

    def __repr__(self):
        return f"Processo [id={self.id}, nome={self.nome}]"