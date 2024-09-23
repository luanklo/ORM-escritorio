from sqlalchemy import Column, String, Integer, Float, ForeignKey
from infra.Configs.base import base

class ProcessoMotivo(base):
    __tablename__ = "processo_motivo"
    # processo_id, motivo_id

    processo_id = Column(Integer, ForeignKey("processo.id"), nullable=False)
    motivo_id = Column(Integer, ForeignKey("motivo.id"), nullable=False)

    __table_args__ = (
        UniqueConstraint('user_id', 'study_id'),
    )