# Importações
import mysql.connector as mysql
try:
    from tqdm import tqdm
except:
    print('instale a biblioteca tqdm pelo comando !pip install tqdm e importe novamente!')

"""
    Objetivo:
        O objetivo desse código é servir como módulo importável com as funções que auxiliaram o código principal.
    Para utiliza-lo, basta importar esse arquivo .py, como se importam as bibliotecas utilizadas no código. Scripts
    .py servem como módulos importaveis em um código, para tal, apenas, para facilitar a sua utilização, certifique-se
    que o o código script esteja NA MESMA PASTA DO ARQUIVO QUE O IMPORTARÁ!

    Operações CRUD:
        As operações CRUD representam um conjunto básico de operações que podem ser realizadas em qualquer
    sistema de gerenciamento de banco de dados relacional. CRUD é um acrônimo para Create (Criar), Read (Ler),
    Update (Atualizar) e Delete (Excluir). Essas operações correspondem às ações básicas que você pode realizar
    em relação aos dados em um banco de dados.
"""

# Definição do Ambiente:
print('Se estiver vazio será definido automaticamente como localhost')
host = input("Insira o host: ")
if host == "":
    host="localhost"
username = input("Insira o User: ")
password = input('Insirao password: ')

# Criando o conector:
db = mysql.connect(
    host=host,
    user=username,
    passwd=password
)

interact = db.cursor()

# Funções:
def create_table(name, qtd_columns):
    '''
        Função que construoi uma tabela,
    no Mysql.
    '''
    try:
        qtd_columns = int(qtd_columns)
    except:
        print('Tipo errada para qtd_columns')
        return None
    
    #print('''
    #           Favor inserir o tipo de dado completo, já
    #       com informando se a coluna é chame primária e
    #       processos similares.
    #''')
    #informacoes = [(input('Insira o nome da coluna:'), input('Insira o tipo de dado: ')) for colum in range(0,qtd_columns)]
    informacoes = []
    for colum in range(0,qtd_columns):
        if colum == 0:
            coluna = input('Favor inserir a Chave Primária:')
            tipo_dado = input('Insira o tipo de dado: ')
            informacoes.append((coluna,tipo_dado))
            
        coluna = input('Insira o nome da coluna:')
        tipo_dado = input('Insira o tipo de dado: ')
        informacoes.append((coluna,tipo_dado))
    print(informacoes)
    
    interact.execute("""
    CREATE TABLE if not exists Tipos_Aerossol (
    Data VARCHAR(7) NOT NULL PRIMARY KEY,
    Poeira FLOAT,
    Poluição_continental_Fumaça FLOAT,
    Poeira_Poluída FLOAT,
    Fumaça_Elevada FLOAT,
    Poeira_Marinha FLOAT
    );
    """)
# Funções para o DML - Data Manipulation Language:
'''
Data Manipulation Language (DML):
    O DML (Data Manipulation Language) é uma parte da linguagem SQL que se concentra
    nas operações de manipulação de dados em um banco de dados. Essas operações envolvem
    a inserção, atualização, recuperação e exclusão de dados em tabelas.
'''

# Função de Inserção de Dados:
def insert_info(dataframe,table):
    '''
        Função que adiciona um dataframe ao
    banco de dados MySQL.
    '''
    
    # Supondo que type_aerosol.columns contenha os nomes das colunas
    columns = dataframe.columns

    # Criando a string de marcadores de posição %s para VALUES
    placeholders_str = ', '.join(['%s'] * len(columns))
    
    # Criando a string completa para a consulta INSERT
    insert_query = f"INSERT INTO BD_aerossol.{table} VALUES ({placeholders_str})"
    
    for i in tqdm(range(0,len(dataframe)-1)):
        try:
            interact.execute(insert_query, tuple(dataframe.iloc[i]))
            db.commit()
        except:
            print(f'problemas na linha {i}')

    if i >= len(dataframe) and i > 0:
        print("Valores Inseridos!")
        
# Função de dropagem de Tabela ou Schema:
def drop(elemento, classe="TABLE"):
    """
    Função que dropa uma tabela ou schema
    """
    try:
        # Utiliza a classe fornecida para determinar se é uma tabela ou schema
        interact.execute(f"DROP {classe} {elemento}")
        print(f'{elemento} Dropado')
    except Exception as e:
        print(f'ERRO! {e}')