from sqlalchemy import Column, String, Integer, Float, ForeignKey
from infra.Configs.base import base

class AudienciaParte(base):
    __tablename__ = "audiencia_parte"
    # advogado_id, parte_id

    advogado_id = Column(Integer, ForeignKey("advogado.id"), nullable=False)
    parte_id = Column(Integer, ForeignKey("parte.id"), nullable=False)

    __table_args__ = (
        UniqueConstraint('advogado_id', 'parte_id'),
    )