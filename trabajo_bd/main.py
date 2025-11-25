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

    # Cursor
    cursor = conn.cursor()

    # Start the menu for the user to interact with the database

    # 5. Target information
    target_type = input("Introduce un tipo de diana y a continuación se mostrarán los nombres de las primeras 20 dianas de ese tipo ordenadas alfabéticamente. Tipo de diana: ")

    cursor.execute(query_5a,(target_type))

    data = cursor.fetchall()
    for row in data:
        print("Primeras 20 dianas del tipo ", target_type, ":\n", row[1])
    
        



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

