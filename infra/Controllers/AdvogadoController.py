from infra.Configs.connection import BDConnectionHandler
from infra.Models.Advogado import Advogado

class AdvogadoController:
    def select(self, id=None, nome=None, aob=None):
        with BDConnectionHandler() as db:
            query = db.session.query(Advogado)
            
            if id:   query = query.filter(Pessoa.id==id)
            if nome: query = query.filter(Pessoa.nome==nome)
            if aob:  query = query.filter(Pessoa.aob==aob)
            
            return query
    
    def insert(self, nome, aob):
        with BDConnectionHandler() as db:
            data_insert = Pessoa(nome=nome, aob=aob)
            db.session.add(data_insert)
            db.session.commit()
    
    def delete(self, id=None, nome=None, aob=None):
        with BDConnectionHandler() as db:
            query = db.session.query(Pessoa)

            if id:   query = query.filter(Pessoa.id==id)
            if nome: query = query.filter(Pessoa.nome==nome)
            if aob:  query = query.filter(Pessoa.aob==aob)

            query.delete()
            db.session.commit()
    
    def update(filtro_id=None, filtro_nome=None, filtro_aob=None, **updates):
        with BDConnectionHandler() as db:
            query = db.query(Pessoa)
            
            if filtro_id:   query = query.filter(Pessoa.id==filtro_id)
            if filtro_nome: query = query.filter(Pessoa.nome==filtro_nome)
            if filtro_aob:  query = query.filter(Pessoa.cpf_cnpj==filtro_aob)
            
            query.update(updates)
            db.commit()