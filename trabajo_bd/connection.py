# %%
# Connection stablishment
import mysql.connector
import config_data

def get_connection():
    return mysql.connection.connect(**config_data.config)
