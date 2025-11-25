# %%
# Connection stablishment
import mysql.connector
import config_data

def get_connection():
    conn = mysql.connector.connect(**config_data.config)
    conn.autocommit = True
    return conn

# %%
