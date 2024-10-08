from sqlalchemy import Column, String, Integer, ForeignKey, Time, Date
from infra.Configs.base import base
from sqlalchemy.orm import relationship

from infra.Configs.connection import BDConnectionHandler
from infra.Models.AudienciaParte import AudienciaParte
from infra.Models.LuanParte import LuanParte

class Audiencia(base):
    __tablename__ = "audiencia"
    #id, hora, dia, tipo, status, link, senha, processo_id

    id =          Column(Integer, primary_key=True)
    hora =        Column(Time, nullable=False)
    dia =         Column(Date, nullable=False)
    tipo =        Column(String, nullable=False)
    status =      Column(String, nullable=False)
    link =        Column(String, nullable=True)
    senha =       Column(String, nullable=True)
    processo_id = Column(Integer, ForeignKey("processo.id"), nullable=False)

    #artes = relationship("Parte", secondary="audiencia_parte", back_populates="audiencias")

    def addParte(self):
        with BDConnectionHandler() as db:
            ids = db.session.query(LuanParte).filter(LuanParte.processo_id == self.processo_id).all()

            for id in ids:
                nova_audienciaparte = AudienciaParte(audiencia_id=self.id, parte_id = id.parte_id, etapa = "FAZER")
                db.session.add(nova_audienciaparte)
                db.session.commit()

    def __repr__(self):
        return f"Audiencia [id={self.id}, hora={self.hora}, dia={self.dia},\
         tipo={self.tipo}, status={self.status}, link={self.link}, senha={self.senha}, processo_id={self.processo_id}]"