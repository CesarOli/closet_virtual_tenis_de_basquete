import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = ' 6joiasthanos',
    database = 'closet_virtual'
)
# Verificando conexão
if conexao.is_connected():
    print('Conexão estabelecida com sucesso!!')
