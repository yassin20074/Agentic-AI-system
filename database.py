#Retrieve the required libraries 
import os
from psycopg_pool import ConnectionPool
from langgraph.checkpoint.postgres import PostgresSaver
from dotenv import load_dotenv

load_dotenv()

DB_URI = os.getenv("DATABASE_URL", "database_Url")

#  Establishing a communications hub 
pool = ConnectionPool(conninfo=DB_URI, max_size=20)

def get_checkpointer():
    checkpointer = PostgresSaver(pool)
    # Creating tables 
    checkpointer.setup()
    return checkpointer
