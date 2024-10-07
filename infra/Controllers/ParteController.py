from infra.Configs.connection import BDConnectionHandler
from infra.Models.Parte import Parte

class ParteController:
    def select(self, id=None, tipo=None, polo=None, processo_id=None, pessoa_id=None):
        with BDConnectionHandler() as db:
            query = db.session.query(Parte)
            
            if id:          query = query.filter(Parte.id == id)
            if tipo:        query = query.filter(Parte.tipo == tipo)
            if polo:        query = query.filter(Parte.polo == polo)
            if processo_id: query = query.filter(Parte.processo_id == processo_id)
            if pessoa_id:   query = query.filter(Parte.pessoa_id == pessoa_id)
            
            return query.all()
    
    def insert(self, tipo, polo, processo_id, pessoa_id):
        with BDConnectionHandler() as db:
            nova_parte = Parte(
                tipo=tipo,
                polo=polo,
                processo_id=processo_id,
                pessoa_id=pessoa_id
            )
            db.session.add(nova_parte)
            db.session.commit()

            return db.session.query(Parte).filter(Parte.processo_id == processo_id).filter(Parte.pessoa_id == pessoa_id).first()
    
    def delete(self, parte: Parte):
        with BDConnectionHandler() as db:
            db.session.delete(parte)
            db.session.commit()
    
    def update(self, parte: Parte, tipo=None, polo=None):
        with BDConnectionHandler() as db:
            updates = {}
            if tipo: updates["tipo"] = tipo
            if polo: updates["polo"] = polo

            db.session.query(Parte).filter(Parte.id == parte.id).update(updates)
            db.session.commit()
