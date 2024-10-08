from sqlalchemy import Column, String, Integer, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from infra.Configs.base import base

class LuanParte(base):
    __tablename__ = "luanparte"
    #parte_id, processo_id, numero

    parte_id = Column(Integer, ForeignKey("parte.id"))
    processo_id = Column(Integer, ForeignKey("processo.id"))
    numero = Column(String)

    __table_args__ = (
        PrimaryKeyConstraint('parte_id', 'processo_id'),  # Combinação como chave primária
    )

    def __repr__(self):
        return f"Advogado [parte_id={self.parte_id}, processo_id={self.processo_id}, numero={self.numero}]"