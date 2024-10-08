from sqlalchemy import Column, String, Integer, ForeignKey
from infra.Configs.base import base

class Pessoa(base):
    __tablename__ = "pessoa"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf_cnpj = Column(String, nullable=True, unique=True)
    numero = Column(String, nullable=True, unique=True)

    def __repr__(self):
        return f"Pessoa [id={self.id}, nome={self.nome}, cpf_cnpj={self.cpf_cnpj}, numero={self.numero}]"