from infra.Configs.connection import BDConnectionHandler
from infra.Models.Pessoa import Pessoa

class PessoaController:
    def select(self, id=None, nome=None, cpf_cnpj=None, numero=None):
        with BDConnectionHandler() as db:
            query = db.session.query(Pessoa)
            
            if id:       query = query.filter(Pessoa.id==id)
            if nome:     query = query.filter(Pessoa.nome==nome)
            if cpf_cnpj: query = query.filter(Pessoa.cpf_cnpj==cpf_cnpj)
            if numero:   query = query.filter(Pessoa.numero==numero)
            
            return query.all()

    def insert(self, nome, cpf_cnpj=None, numero=None):
        with BDConnectionHandler() as db:
            data_insert = Pessoa(nome=nome, cpf_cnpj=cpf_cnpj, numero=numero)
            db.session.add(data_insert)
            db.session.commit()
    
    def delete(self, pessoa: Pessoa):
        with BDConnectionHandler() as db:
            if len(pessoa) != 1: print("tamanho errado"); return
            
            db.session.delete(pessoa[0])
            db.session.commit()
    
    def update(self, pessoa: Pessoa, nome=None, cpf_cnpj=None, numero=None):
        with BDConnectionHandler() as db:
            updates = {}
            if nome: updates["nome"] = nome
            if cpf_cnpj: updates["cpf_cnpj"] = cpf_cnpj
            if numero: updates["numero"] = numero

            db.session.query(Pessoa).filter(Pessoa.id == pessoa[0].id).update(updates)
            db.session.commit()