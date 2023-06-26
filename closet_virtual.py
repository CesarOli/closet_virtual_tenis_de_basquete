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

cursor = conexao.cursor()
sql = """
CREATE TABLE Tenis (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    Nome do Tenis VARCHAR(100),
    Marca VARCHAR(50),
    Numeracao DECIMAL(3, 2),
    Cor VARCHAR(50),
    Ano_Lancamento(YEAR),
    Valor DECIMAL(10, 2)
    Quantidade_Estoque INT
)
"""
cursor.execute(sql)
conexao.commit()
conexao.close()

