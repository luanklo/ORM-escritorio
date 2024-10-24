from infra.Configs.connection import BDConnectionHandler
from infra.Models.Audiencia import Audiencia

class AudienciaController:
    def select(self, id=None, hora=None, dia=None, tipo=None, status=None, link=None, senha=None, processo_id=None):
        with BDConnectionHandler() as db:
            query = db.session.query(Audiencia)
            
            if id:          query = query.filter(Audiencia.id == id)
            if hora:        query = query.filter(Audiencia.hora == hora)
            if dia:         query = query.filter(Audiencia.dia >= dia)
            if tipo:        query = query.filter(Audiencia.tipo == tipo)
            if status:      query = query.filter(Audiencia.status == status)
            if link:        query = query.filter(Audiencia.link == link)
            if senha:       query = query.filter(Audiencia.senha == senha)
            if processo_id: query = query.filter(Audiencia.processo_id == processo_id)

            query.order_by(Audiencia.dia, Audiencia.hora)
            
            return query.all()
    
    def insert(self, hora, dia, tipo, status="DESIGNADA", link=None, senha=None, processo_id=None):
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

            return db.session.query(Audiencia)\
                .filter(Audiencia.hora == hora)\
                .filter(Audiencia.dia == dia)\
                .filter(Audiencia.processo_id == processo_id).one()
    
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
