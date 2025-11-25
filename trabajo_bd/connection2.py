# %%
import mysql.connector
import config_data
def get_connection2():
    conn = mysql.connector.connect(**config_data.config)
    return conn

# %%
