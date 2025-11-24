# %%
# Connection stablishment
import mysql.connector
import config_data

def get_connection():
    return mysql.connector.connect(**config_data.config)
