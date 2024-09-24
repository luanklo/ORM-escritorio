from sqlalchemy import Column, String, Integer, ForeignKey, Time, Date, relationship
from infra.Configs.base import base

class Parte(base):
    __tablename__ = "parte"
    # id, tipo, polo, processo_id, pessoa_id

    id = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)
    polo = Column(String, nullable=False)
    processo_id = Column(Integer, ForeignKey("processo.id"), nullable=False)
    pessoa_id = Column(Integer, ForeignKey("pessoa.id"), nullable=False)

    audiencias = relationship("Audiencia", secondary="processo_motivo", back_populates="partes")
    advogados = relationship("Advogado", secondary="advogado_parte", back_populates="partes")

