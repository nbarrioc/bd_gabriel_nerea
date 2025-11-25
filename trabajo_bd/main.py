# %% 
# Stablish the connection
import mysql.connector
from mysql.connector import errorcode
from connection import get_connection
# Import the file containing the different posible queries to carry out
import queries

# %%
# Handle posible errors
try: 
    conn = get_connection()
    print('Conexión satisfactoria')

    # Starting menu and queries

    # 5. Information about targets

    # 5a. Targets of a certain type given
    list_targets = query_5a(conn)

    print("Lista de las 20 primeras dianas ordenadas alfabéticamente:")

    print(list_targets)



except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Usuario y/o contraseña incorrectos')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('Nombre de la base de datos incorrecto.')
    else:
        print(err)
else: 
    conn.close()
    print('Se ha cerrado la conexión correctamente')


# %%
