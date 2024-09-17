from infra.Configs.connection import BDConnectionHandler
from infra.Models.Pessoa import Pessoa

class PessoaController:
    def select(self, nome=None, cpf_cnpj=None, numero=None):
        with BDConnectionHandler() as db:
            query = db.session.query(Pessoa)
            
            if nome:     query = query.filter(Pessoa.nome==nome)
            if cpf_cnpj: query = query.filter(Pessoa.cpf_cnpj==cpf_cnpj)
            if numero:   query = query.filter(Pessoa.numero==numero)
            
            # query.all()
            return query

    def insert(self, nome, cpf_cnpj=None, numero=None):
        with BDConnectionHandler() as db:
            data_insert = Pessoa(nome=nome, cpf_cnpj=cpf_cnpj, numero=numero)
            db.session.add(data_insert)
            db.session.commit()
    
    def delete(self, nome=None, cpf_cnpj=None, numero=None):
        with BDConnectionHandler() as db:
            query = db.session.query(Pessoa)

            if nome: query.filter(Pessoa.nome==nome)
            if cpf_cnpj: query.filter(Pessoa.cpf_cnpj==cpf_cnpj)
            if numero: query.filter(Pessoa.numero==numero)

            query.delete()
            db.session.commit()
    
    def update(filtro_nome=None, filtro_cpf_cnpj=None, filtro_numero=None, **updates):
        with BDConnectionHandler() as db:
            query = db.query(Pessoa)
            
            if filtro_nome:     query = query.filter(Pessoa.nome==filtro_nome)
            if filtro_cpf_cnpj: query = query.filter(Pessoa.cpf_cnpj==filtro_cpf_cnpj)
            if filtro_numero:   query = query.filter(Pessoa.numero==filtro_numero)
            
            query.update(updates)
            db.commit()