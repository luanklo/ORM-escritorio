from infra.Configs.connection import BDConnectionHandler
from infra.Models.Motivo import Motivo

class MotivoController:
    def select(self, id=None, nome=None):
        with BDConnectionHandler() as db:
            query = db.session.query(Motivo)
            
            if id:       query = query.filter(Pessoa.id==id)
            if nome:     query = query.filter(Pessoa.nome==nome)
            
            return query.all()

    def insert(self, nome):
        with BDConnectionHandler() as db:
            data_insert = Motivo(nome=nome)
            db.session.add(data_insert)
            db.session.commit()

    def delete(self, motivo: Motivo):
        with BDConnectionHandler() as db:
            if len(motivo) != 1: print("tamanho errado"); return
            
            db.session.delete(motivo[0])
            db.session.commit()

    def update(self, motivo: Motivo, nome):
        with BDConnectionHandler() as db:
            updates = {}
            if nome: updates["nome"] = nome

            db.session.query(Motivo).filter(Motivo.id == motivo[0].id).update(updates)
            db.session.commit()