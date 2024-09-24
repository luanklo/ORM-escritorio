from sqlalchemy import Column, String, Integer, ForeignKey, Time, Date, relationship
from infra.Configs.base import base

from infra.Configs.connection import BDConnectionHandler
from infra.Models.AdvogadoParte import AdvogadoParte
from infra.Models.Advogado import Advogado

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

    def addAdvogado(self, advogado: Advogado):
        with BDConnectionHandler() as db:
            novo_advogado = AdvogadoParte(parte_id=self.id, advogado_id=advogado.id)
            db.session.add(novo_advogado)
            db.session.commit()