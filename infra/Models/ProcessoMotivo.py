from sqlalchemy import Column, String, Integer, Float, ForeignKey
from infra.Configs.base import base

class ProcessoMotivo(base):
    __tablename__ = "processo_motivo"
    # processo_id, motivo_id

    processo_id = Column(Integer, ForeignKey("processo.id"), nullable=False, primary_key=True)
    motivo_id = Column(Integer, ForeignKey("motivo.id"), nullable=False, primary_key=True)