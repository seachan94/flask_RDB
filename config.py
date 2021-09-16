import os
from dotenv import load_dotenv
load_dotenv()

db = {
'user':os.getenv('db_user'),
'password':os.getenv('db_password'),
'host':os.getenv('db_host'),
'port':os.getenv('db_port'),
'database':os.getenv('database')
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8" 




