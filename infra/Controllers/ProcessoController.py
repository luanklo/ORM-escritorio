from infra.Configs.connection import BDConnectionHandler
from infra.Models.Processo import Processo

class ProcessoController:
    def select(self, id=None, numero=None, valor=None, vara=None, classe=None, link=None, profissao=None):
        with BDConnectionHandler() as db:
            query = db.session.query(Processo)
            
            if id:        query = query.filter(Processo.id==id)
            if numero:    query = query.filter(Processo.numero==numero)
            if valor:     query = query.filter(Processo.valor==valor)
            if vara:      query = query.filter(Processo.vara==vara)
            if classe:    query = query.filter(Processo.classe==classe)
            if link:      query = query.filter(Processo.link==link)
            if profissao: query = query.filter(Processo.profissao==profissao)
            
            return query.all()

    def insert(self, numero, valor, vara, classe, link, profissao=None):
        with BDConnectionHandler() as db:
            data_insert = Processo(numero=numero, valor=valor, vara=vara, classe=classe, link=link, profissao=profissao)
            db.session.add(data_insert)
            db.session.commit()
    
    def delete(self, processo: Processo):
        with BDConnectionHandler() as db:
            if len(processo) != 1: print("tamanho errado"); return
            
            db.session.delete(processo[0])
            db.session.commit()

    def update(self, processo: Processo, numero=None, valor=None, vara=None, classe=None, link=None, profissao=None):
        with BDConnectionHandler() as db:
            updates = {}
            if numero: updates["numero"] = numero
            if valor: updates["valor"] = valor
            if vara: updates["vara"] = vara
            if classe: updates["classe"] = classe
            if link: updates["link"] = link
            if profissao: updates["profissao"] = profissao

            db.session.query(Processo).filter(Processo.id == processo[0].id).update(updates)
            db.session.commit()