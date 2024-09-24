from sqlalchemy import Column, String, Integer, Float, ForeignKey
from infra.Configs.base import base
from sqlalchemy.orm import relationship

class Motivo(base):
    __tablename__ = "motivo"
    # id, nome

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)

    processos = relationship("Processo", secondary="processo_motivo", back_populates="motivos")


    def __repr__(self):
        return f"Motivo [id={self.id}, nome={self.nome}]"