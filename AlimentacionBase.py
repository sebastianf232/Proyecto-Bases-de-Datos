from sqlalchemy import create_engine
import pandas as pd
import glob
from pathlib import Path

list_df = []
for file in glob.glob("/Users/sebastianfranco/Documents/Universidad/Cuarto Semestre/Bases de Datos/Proyecto1/Copia de Datos/**/*.csv", recursive=True):
    list_df.append(file)
engine = create_engine('postgresql://postgres:admin@localhost:5432/proyecto1')
for i in list_df:
    df = pd.read_csv(i)
    df.to_sql(Path(i).resolve().stem, engine)
    print("listo")


