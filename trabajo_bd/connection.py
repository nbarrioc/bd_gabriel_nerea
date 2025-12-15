# %%
# Authors: Nerea Barrio, Gabriel Coll
# Connection establishment

import mysql.connector
import config_data

def get_connection():
    conn = mysql.connector.connect(
        user=config_data.config["user"],
        password=config_data.config["password"],
        host=config_data.config["host"],
        database=config_data.config["database"],
        use_pure=True
    )
    conn.autocommit = True
    return conn

