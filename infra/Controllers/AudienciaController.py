from infra.Configs.connection import BDConnectionHandler
from infra.Models.Audiencia import Audiencia

class AudienciaController:
    def select(self, id=None, processo_id=None, dia=None):
        with BDConnectionHandler() as db:
            query = db.session.query(Audiencia)
            
            if id:          query = query.filter(Audiencia.id == id)
            if hora:        query = query.filter(Audiencia.hora == hora)
            if dia:         query = query.filter(Audiencia.dia == dia)
            if tipo:        query = query.filter(Audiencia.tipo == tipo)
            if status:      query = query.filter(Audiencia.status == status)
            if link:        query = query.filter(Audiencia.link == link)
            if senha:       query = query.filter(Audiencia.senha == senha)
            if processo_id: query = query.filter(Audiencia.processo_id == processo_id)
            
            return query.all()
    
    def insert(self, hora, dia, tipo, status="designada", link=None, senha=None, processo_id=None):
        with BDConnectionHandler() as db:
            nova_audiencia = Audiencia(
                hora=hora,
                dia=dia,
                tipo=tipo,
                status=status,
                link=link,
                senha=senha,
                processo_id=processo_id
            )
            db.session.add(nova_audiencia)
            db.session.commit()
    
    def delete(self, audiencia: Audiencia):
        with BDConnectionHandler() as db:
            db.session.delete(audiencia)
            db.session.commit()
    
    def update(self, audiencia: Audiencia, hora=None, dia=None, tipo=None, status=None, link=None, senha=None):
        with BDConnectionHandler() as db:
            updates = {}
            if hora: updates["hora"] = hora
            if dia: updates["dia"] = dia
            if tipo: updates["tipo"] = tipo
            if status: updates["status"] = status
            if link: updates["link"] = link
            if senha: updates["senha"] = senha

            db.session.query(Audiencia).filter(Audiencia.id == audiencia.id).update(updates)
            db.session.commit()
