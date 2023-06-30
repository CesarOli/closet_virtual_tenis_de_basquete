import mysql.connector
import requests
from time import sleep

config = { 
    'host': 'localhost',
    'user': 'root',
    'password': 'SENHA_DESEJADA',
    'database': 'closet_virtual'
}
conectar = None

def conectarBancoDados():
    global conectar
    conectar = mysql.connector.connect(**config)
    if conectar.is_connected():
        sleep(2)
        print('Aguarde...Estabelecendo conexão ao bando de dados.')
        sleep(1.5)
        print('...')
        sleep(1)
        print('Conexão ao banco de dados realizada com sucesso.')
    else:
        sleep(2)
        print('Falha na conexão.')

conectarBancoDados()

'''def menuPrincipal():
    print('Bem-vindo ao Closet Virtual!')
    print('Selecione uma opção:')
    print('1. Conectar ao Banco de Dados')
    print('2. Visualizar Closet Virtual')
    print('3. Adicionar Novo Tênis')
    print("0. Sair")



# Verificando conexão


cursor = conexao.cursor()
sql = """CREATE TABLE Tenis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    `Nome do Tenis` VARCHAR(100),
    Marca VARCHAR(50),
    Numeracao DECIMAL(3, 2),
    Cor VARCHAR(50),
    `Ano do Lancamento` YEAR,
    Valor DECIMAL(10, 2),
    Quantidade_Estoque INT
)"""

cursor.execute(sql)

def adicionarColunaLinha():
    sql = "ALTER TABLE Tenis ADD COLUMN Linha VARCHAR(50)"
    cursor.execute(sql)
    print('Coluna "Linha" adiciona com sucesso!')

def adicionarNovoTenis():
    nome = input('Nome do Tênis: ')
    marca = input('Marca do Tênis: ')
    numeracao = (float(input('Numeração: ')))
    cor = input('Cor: ')
    ano = ('Ano de Lançamento: ')
    valor = float(input('Valor do Tênis: '))
    quantidade = ('Quantidade deste modelo em estoque: ')
    #colocar opções de menu: Kobe, Air Jordan, e demais linhas
    linha = input('Linha do Tênis: ')
    
    cursor = conexao.cursor()
    sql = "INSERT INTO Tenis (`Nome do Tenis`, Marca, Numeracao, Cor, `Ano do Lancamento`, Valor, Quantidade_Estoque, Linha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"


sql = 'DESCRIBE Tenis'
cursor.execute(sql)
resultados = cursor.fetchall()
colunas = [coluna[0] for coluna in resultados]

cursor.execute("SELECT * FROM Tenis")
result = cursor.fetchall()

if 'Linha' not in colunas:
    adicionarColunaLinha()

sql = 'SELECT  * FROM Tenis'
cursor.execute(sql)
result = cursor.fetchall()

print('Abrindo seu Closet Virtual...', '\n')
sleep(2.5)
print("=" * 90)
print("{:<5} {:<20} {:<15} {:<10} {:<10} {:<10} {:<10}".format("ID", "Nome do Tênis", "Marca", "Linha", "Numeração", "Cor", "Ano", "Valor"))
print("=" * 90)

for row in result:
    sleep(1.5)
    print("{:<5} {:<20} {:<15} {:<10} {:<10} {:<10} R${:<10.2f}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

sleep(1.5)

menuPrincipal()
conexao.commit()
conexao.close()'''
sleep(2)
print('\n', 'Fim do Programa!!')

