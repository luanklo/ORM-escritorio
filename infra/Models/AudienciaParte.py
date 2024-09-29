from sqlalchemy import Column, String, Integer, Float, ForeignKey
from infra.Configs.base import base

class AudienciaParte(base):
    __tablename__ = "audiencia_parte"
    # advogado_id, parte_id

    audiencia_id = Column(Integer, ForeignKey("audiencia.id"), nullable=False, primary_key=True)
    parte_id = Column(Integer, ForeignKey("parte.id"), nullable=False, primary_key=True)