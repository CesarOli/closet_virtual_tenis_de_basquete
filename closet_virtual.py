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
'''
cursor = conexao.cursor()
sql = """
CREATE TABLE Tenis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    `Nome do Tenis` VARCHAR(100),
    Marca VARCHAR(50),
    Numeracao DECIMAL(3, 2),
    Cor VARCHAR(50),
    `Ano do Lancamento` YEAR,
    Valor DECIMAL(10, 2),
    Quantidade_Estoque INT
)
"""

cursor.execute(sql)'''

cursor = conexao.cursor()
sql = 'DESCRIBE Tenis'
cursor.execute(sql)
resultados = cursor.fetchall()

cursor.execute("SELECT * FROM Tenis")
result = cursor.fetchall()

print('Abrindo seu Closet Virtual...', '\n')
sleep(2.5)
print("=" * 90)
print("{:<5} {:<20} {:<15} {:<10} {:<10} {:<10} {:<10}".format("ID", "Nome do Tênis", "Marca", "Numeração", "Cor", "Ano", "Valor"))
print("=" * 90)

for row in result:
    sleep(1.5)
    print("{:<5} {:<20} {:<15} {:<10} {:<10} {:<10} R${:<10.2f}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

sleep(1.5)
print('\n', 'Fim do Programa!!')
conexao.commit()
conexao.close()


