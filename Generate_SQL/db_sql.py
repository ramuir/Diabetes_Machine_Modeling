#create database and connect df_clean
#create seperate connect file for users to add their password and user name
#SELECT * FROM "InitialData"
#SELECT * FROM "DiabetesData"
import pandas as pd
from connect import password
from sqlalchemy import create_engine
import psycopg2

df_clean = pd.read_csv('../Data_csv/cleaned_data.csv')
initial_dataset = pd.read_csv('../Data_csv/initial_dataset.csv')
engine = create_engine(f'postgresql://postgres:{password}@localhost:5432/Diabetes_Awareness')
df_clean.to_sql("DiabetesData", engine, if_exists="append", index=False)
initial_dataset.to_sql("InitialData", engine)

print("connected to postgres DB")