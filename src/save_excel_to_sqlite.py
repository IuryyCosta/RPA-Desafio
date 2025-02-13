import pandas as pd
import os
from sqlalchemy import create_engine


def save_to_execel_from_sqlite(db_name='data/books.db',file_name ='reports/books_rel.xlsx' ):

    os.makedirs('reports', exist_ok=True) #garantindo a existência da pasta reports
    engine = create_engine(f'sqlite:///{db_name}')

    query = "SELECT title, price, availability from books" #query para selecionar os dados da tabela books

    df = pd.read_sql_query(query, engine) #lendo os dados da tabela books e salvando em um dataframe
    df.to_excel(file_name, index=False)  
    print(f"Relatório gerado: {file_name}")