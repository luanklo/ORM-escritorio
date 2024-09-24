from sqlalchemy import Column, String, Integer, ForeignKey, Time, Date, relationship
from infra.Configs.base import base

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

    partes = relationship("Parte", secondary="audiencia_parte", back_populates="audiencias")

    def __repr__(self):
        return f"Audiencia [id={self.id}, hora={self.hora}, dia={self.dia},\
         tipo={self.tipo}, status={self.status}, link={self.link}, senha={self.senha}, processo_id={self.processo_id}]"