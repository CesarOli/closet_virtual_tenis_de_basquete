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
cursor = conectar.cursor()

def verificaExisteTabelaTenis(cursor):
    cursor.execute("SHOW TABLES LIKE 'Tenis'")

    if cursor.fetchone():
        print("A tabela 'Tenis' já existe.")
    else:
        criarTabelaTenis = '''CREATE TABLE Tenis (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        marca VARCHAR(50),
        numeracao VARCHAR(10),
        linha VARCHAR(50)
        )'''
        cursor.execute(criarTabelaTenis)
        print("A tabela 'Tenis' já existe.")

verificaExisteTabelaTenis(cursor)

def menuPrincipal():
    print('Bem-vindo ao Closet Virtual!')
    sleep(1)
    while True:
        print('Selecione uma opção:')
        sleep(0.5)
        print('1. Adicione seu Novo Tênis')
        sleep(0.5)
        print("0. Sair")

        sleep(0.3)
        opcao = input('Digite o número da opção desejada: ')

        if opcao == '1':
            adicionarNovoTenis()
        elif opcao == '0':
            sleep(1)
            print('Parabéns, seu novo Tênis foi adicionado ao seu Closet Virtual!!')
            
            break
        else:
            print('Opção inválida. Por favor, selecione uma opção válida.')

def adicionarNovoTenis():
    print('Adicione seu novo Tênis')

    nome = input('Informe o nome do Tênis: ')
    marca = input('Informe a marca do Tênis: ')
    numeracao = input('Informe a numeração do Tênis: ')
    linha = input('Informe a linha do Tênis: ')

    if conectar is None or not conectar.is_connected():
        print('Não há uma conexão estabelecida com o banco de dados.')
        return

    cursor = conectar.cursor()

    inserirNovoTenis = '''INSERT INTO Tenis (nome, marca, numeracao, linha)
    VALUES (%s, %s, %s, %s)'''

    infoTenis = (nome, marca, numeracao, linha)
    cursor.execute(inserirNovoTenis, infoTenis)
    conectar.commit()

menuPrincipal()
