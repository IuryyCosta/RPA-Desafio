import pandas as pd
import os
from sqlalchemy import create_engine

def save_to_sqlite(data, db_name='data/books.db'):

    os.makedirs('data', exist_ok= True) #garante a criação da pasta data se ela não existir

    db_path = os.path.abspath(db_name)

    engine = create_engine(f'sqlite:///{db_path}') #Configuração da conexão com SQLite 
    df = pd.DataFrame(data) #Transforma a lista em um DataFrame
    df.to_sql('books', engine, if_exists='replace', index=False) #Salva
