import sqlite3
conexao = sqlite3.connect('ativ_m2s1.sqlite3')
cursor = conexao.cursor()

sql = '''
CREATE TABLE cliente (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT(100),
    cpf TEXT(11),
    data_cadastro TEXT(10),
    endereco TEXT(100)
)
'''

cursor.execute(sql)
conexao.commit() 
conexao.close()