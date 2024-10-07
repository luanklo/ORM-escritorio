from infra.Configs.connection import BDConnectionHandler
from infra.Models.Advogado import Advogado

class AdvogadoController:
    def select(self, id=None, nome=None, aob=None):
        with BDConnectionHandler() as db:
            query = db.session.query(Advogado)
            
            if id:   query = query.filter(Advogado.id==id)
            if nome: query = query.filter(Advogado.nome==nome)
            if aob:  query = query.filter(Advogado.aob==aob)
            
            return query.all()
    
    def insert(self, nome, aob):
        with BDConnectionHandler() as db:
            data_insert = Advogado(nome=nome, aob=aob)
            db.session.add(data_insert)
            db.session.commit()

            return db.session.query(Advogado).filter(Advogado.aob==aob).first()
    
    def delete(self, advogado: Advogado):
        with BDConnectionHandler() as db:
            if len(advogado) != 1: print("tamanho errado"); return

            db.session.delete(advogado[0])
            db.session.commit()
    
    def update(self, advogado: Advogado, nome=None, aob=None):
        with BDConnectionHandler() as db:
            updates = {}
            if nome: updates["nome"] = nome
            if aob: updates["aob"] = aob

            db.session.query(Advogado).filter(Advogado.id == advogado[0].id).update(updates)
            db.session.commit()
