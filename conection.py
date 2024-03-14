import mysql.connector
from time import time
import numpy as np

def insert_data(dataframe, tabela, temporizador=True):
    '''
        Função construida para inserir
    dados numa tabela qualquer.
    '''

    # Ajustando valores nan para serem inseridos na tabela:
    dataframe.replace({'nan': None, np.nan: None}, inplace=True)

    # Extraindo as colunas como string:
    colunas = ', '.join([f'`{col}`' for col in dataframe.columns])

    inicio = time()

    # Preparando os valores para inserção
    values = [tuple(row) for row in dataframe.to_numpy()]

    # Construindo a instrução SQL com %s para cada valor
    insert = f"INSERT INTO {tabela} ({colunas}) VALUES ({', '.join(['%s'] * len(dataframe.columns))})"

    # Executando a inserção em lote
    cursor.executemany(insert, values)
    mydb.commit()

    final = time()

    print(f'Dados inseridos com sucesso na tabela {var}')
    print('Tempo de processamento:', int(final - inicio), 'segundos')

    if temporizador == "False":
        # Ajustando valores nan para serem inseridos na tabela:
        dataframe.replace({'nan': None, np.nan: None}, inplace=True)
    
        # Extraindo as colunas como string:
        colunas = ', '.join([f'`{col}`' for col in dataframe.columns])
    
        inicio = time()
    
        # Preparando os valores para inserção
        values = [tuple(row) for row in dataframe.to_numpy()]
    
        # Construindo a instrução SQL com %s para cada valor
        insert = f"INSERT INTO {tabela} ({colunas}) VALUES ({', '.join(['%s'] * len(dataframe.columns))})"
    
        # Executando a inserção em lote
        cursor.executemany(insert, values)
        mydb.commit()
    
        

def connection(host, user, password):
    '''
        Função que faz a conexão dos
    com o SGBD em questão.
    '''

    # Conectando-se ao SGBD:
    mydb = mysql.connector.connect(
      host=host,
      user=user,
      password=password
    )
    
    if mydb.is_connected() == True:
        print('Conectado ao SGBD')

    # Instanciando o cursor para transferência de informação:
    return mydb.cursor()