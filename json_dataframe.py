
import json
from sre_parse import State
import pandas as pd

def jsonimport(p):
  with open(p,'r') as f:
    jsonload = json.loads(f.read())

  json_df = pd.json_normalize(jsonload, record_path=['states'], meta=[])
  json_df[['name','abbreviation']]= json_df[['name','abbreviation']].applymap(lambda x: x.lower())
  json_df['country'] = 'US'
#   json_df.rename(columns={'index':'id'})
  return json_df

file_path = '/Users/sauami/Documents/Python/tmp/{}'.format('data.json')

json_dataframe = jsonimport(file_path)
# print(json_dataframe)


from sqlalchemy import create_engine
import psycopg2

engine = create_engine('postgresql://db_user:Tiger123456@localhost:5432/sr1001')


def json_sqlto_db(df, engine, tbl):
    try:
        df.to_sql(tbl, engine, if_exists='append')
        #  replace will trunc table and insert, append add the new record to table
    except:
        print('Error in exporting Json to DB')
    else:
        print('Json load Successfully')


json_sqlto_db(json_dataframe,engine,'my_tbl')
