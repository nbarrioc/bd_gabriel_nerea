# %% 
# Stablish the connection
from connection import get_connection
from mysql.connector import errorcode

try: 
    conn = get_connection()
    print('Conexión satisfactoria')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Usuario y/o contraseña incorrectos')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('Nombre de la base de datos incorrecto.')
    else:
        print(err)


# %%
# Main menu
# %%
# 5. Información de los targets
input("Introduce un tipo de diana y a continuación se mostrarán los nombres de las primeras 20 dianas de ese tipo ordenadas alfabéticamente. Tipo de diana: ")
query_5a = """
           SELECT target_name_pref
           FROM target
           WHERE target_type = %s
           ORDER BY target_name_pref ASC
           LIMIT 20;
           """