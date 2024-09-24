from sqlalchemy import Column, String, Integer, Float, ForeignKey
from infra.Configs.base import base

class AdvogadoParte(base):
    __tablename__ = "advogado_parte"
    # advogado_id, parte_id

    advogado_id = Column(Integer, ForeignKey("advogado.id"), nullable=False, primary_key=True)
    parte_id = Column(Integer, ForeignKey("parte.id"), nullable=False, primary_key=True)