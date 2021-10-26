from models import Efetivo, Pacotes, db_session

def insere_pacote():
    pacote = Pacotes(nome='ROTINA')
    pacote.save()

def consulta_pacote():
    pacote = Pacotes.query.all()
    print(pacote)
    # pessoa = Pacotes.query.filter_by(nome='rotina pe-1').first()
    # print(pessoa)
def altera_pacote():
    pacote = Pacotes.query.filter_by(nome='rotina pe-1').first()
    pacote.nome = 'Plano de Pintura'
    pacote.save()

def exclui_pacote():
    pacote = Pacotes.query.filter_by(nome='Plano de Pintura').first()
    pacote.delete()

if __name__ == '__main__':
    #insere_pacote()
    #altera_pacote()
    #exclui_pacote()
    consulta_pacote()

