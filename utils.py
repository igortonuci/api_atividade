from models import Pessoas, db_session

#insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Galeane', idade=25)
    print(pessoa)
    db_session.add(pessoa)
    db_session.commit()

#consulta dados na tabela pessoa
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Galeane').first()
    print(pessoa.nome)

#altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.idade = 21
    db_session.add(pessoa)
    db_session.commit()

#exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    db_session.delete(pessoa)
    db_session.commit()




if __name__ == '__main__':
    #insere_pessoas()
    consulta_pessoas()
    #altera_pessoa()
    #exclui_pessoa()