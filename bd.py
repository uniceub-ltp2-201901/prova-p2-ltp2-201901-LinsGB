def cadastrar(cursor,username,senha,numero):
    cursor.execute(f'INSERT INTO cadastros.usuarios (numurl, login, senha, contador) VALUES ("{numero}","{username}","{senha}",0)')

def url_emuso(cursor):
    cursor.execute(f'SELECT numurl FROM cadastros.usuarios')
    numurl_usadas = cursor.fetchall()
    return numurl_usadas
