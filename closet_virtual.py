import mysql.connector
from time import sleep

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'CesarOli',
    password = '6joiasthanos',
    database = 'closet_virtual'
)
# Verificando conexão
if conexao.is_connected():
    sleep(2.5)
    print('Aguardando conexão ao banco de dados...')
    sleep(1.1)
    print('Conexão estabelecida com sucesso!!')



