from MVC import pygres_connection


def insere_pessoa(dados_pessoa):

    pygres_connection.cursor.execute("INSERT INTO pessoas (nome, endereco, cpf, estado, turma, periodo, modulos)"
                                      "VALUES (%s, %s,%s,%s,%s,%s,%s)",
                                            (
                                            dados_pessoa['pessoa'],
                                            dados_pessoa['endereço'],
                                           dados_pessoa['cpf'],
                                            dados_pessoa['estado'],
                                          dados_pessoa['turma'],
                                            dados_pessoa['periodo'],
                                           dados_pessoa['modulo']
                                            )
                                     )
def retorna_pessoa():

    return pygres_connection.cursor.execute("SELECT * FROM pessoas")

    pygres_connection.db.insert("pessoa", nome=dados_pessoa['pessoa'],
                                endereco=dados_pessoa['endereço'],
                                cpf=dados_pessoa['cpf'],
                                estado=dados_pessoa['estado'],
                                turma=dados_pessoa['turma'],
                                periodo=dados_pessoa['periodo'],
                                modulo=dados_pessoa['modulo'])
