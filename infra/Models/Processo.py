from sqlalchemy import Column, String, Integer, Float, ForeignKey
from infra.Configs.base import base

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

    def __repr__(self):
        return f"Processo [id={self.id}, numero={self.numero}, valor={self.valor}, vara={self.vara}, classe={self.classe}, link={self.link}, profissao={self.profissao}]"