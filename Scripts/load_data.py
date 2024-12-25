import os
import psycopg2
import dotenv as load_env
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine 
##
#load environmental variables from .env

load_dotenv()
#fetch database connector parameter from enviromental variables
DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")
DB_NAME=os.getenv("DB_NAME")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def load_data_using_sql_alchemy(query):
    try:
        engine = create_engine(DATABASE_URL)
        df=pd.read_sql_query(query, engine)
        if df is not None:
            df.head()
        else:
            print("Noo")
        #df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        print(f"Database Connection Failed: {str(e)}")
query="SELECT * FROM xdr_data;"
load_data_using_sql_alchemy(query)
