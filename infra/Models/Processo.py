from sqlalchemy import Column, String, Integer, Float, ForeignKey
from infra.Configs.base import base
from sqlalchemy.orm import relationship

from infra.Models.ProcessoMotivo import ProcessoMotivo
from infra.Models.Motivo import Motivo
from infra.Configs.connection import BDConnectionHandler


class Processo(base):
    __tablename__ = "processo"
    # id, numero, valor, vara, classe, link, profissao

    id = Column(Integer, primary_key=True)
    numero = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    vara = Column(String, nullable=False)
    classe = Column(String, nullable=False)
    link = Column(String, nullable=False)
    profissao = Column(String, nullable=True)

    motivos = relationship("Motivo", secondary="processo_motivo", back_populates="processos")

    def addMotivo(self, motivo: Motivo):
        with BDConnectionHandler() as db:
            novo_motivo = ProcessoMotivo(processo_id=self.id, motivo_id=motivo.id)
            db.session.add(novo_motivo)
            db.session.commit()

    def __repr__(self):
        return f"Processo [id={self.id}, numero={self.numero}, valor={self.valor}, vara={self.vara}, classe={self.classe}, link={self.link}, profissao={self.profissao}]"