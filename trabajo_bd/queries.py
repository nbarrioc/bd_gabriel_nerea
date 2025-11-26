# %%
# Script to define the different queries that will be used

import mysql.connector


# %%
# Selection queries

# %%
# 5. Information about targets

# 5a. Targets of a certain target type given
def query_5a(conn):
    cursor = conn.cursor()
    query = """
            SELECT target_name_pref
            FROM target
            WHERE target_type = %s
            ORDER BY target_name_pref ASC
            LIMIT 20;
            """
    
    print("Introduzca un tipo de diana y a continuación se mostrarán los nombres de las primeras 20 dianas de ese tipo ordenadas alfabéticamente.")
    target_type = input("Tipo de diana: ")

    cursor.execute(query,(target_type,))

    data = cursor.fetchall()

    cursor.close()

    return data


# %%
# 5b. Organism with the most number of targets
def query_5b(conn):
    cursor = conn.cursor()
    query = """
            SELECT taxonomy_name
            FROM organism, 
                (SELECT organism_id, COUNT(DISTINCT target_id) ntarget
	            FROM target
	            GROUP BY organism_id
	            ORDER BY ntarget DESC
	            LIMIT 1) ntar
            WHERE taxonomy_id=organism_id;
            """
    
    cursor.execute(query)

    data = cursor.fetchone()

    cursor.close()

    return data


# %%
# Modification queries

# 6. Deletes
def query_6(conn):
    cursor = conn.cursor()
    query1 = """
           SELECT inferred_score, drug_name, disease_name
           FROM drug_disease, drug, disease_has_code, disease
           WHERE inferred_score IS NOT NULL AND
           drug_disease.drug_id=drug.drug_id AND
           drug_disease.code_id=disease_has_code.code_id AND
           disease_has_code.disease_id=disease.disease_id
           ORDER BY inferred_score, drug_name, disease_name ASC
           LIMIT 10;
           """
    
    cursor.execute(query1)

    interactions = cursor.fetchall()

    query2 = """
             DELETE FROM drug_disease
             WHERE inferred_score BETWEEN %s AND %s AND
             drug_id =
                  (SELECT drug_id
                  FROM drug
                  WHERE drug_name=%s) AND
             code_id =
            	  (SELECT code_id
	              FROM disease_has_code, disease
	              WHERE disease_name=%s AND
		              disease_has_code.disease_id=disease.disease_id);
             """ 

    print("Lista de las 10 primeras interacciones con menor inferred score")
    
    j = 1

    for row in interactions:
        print("[",j,"]. ", row)
        j = j+1
    
    option_number = int(input("Por favor, introduzca el número de la fila que desea eliminar: "))

    inferred_score_selected = interactions[option_number-1][0]
    drug_name_selected = interactions[option_number-1][1]
    disease_name_selected = interactions[option_number-1][2]

    cursor.execute(query2,(inferred_score_selected-0.005,inferred_score_selected+0.005,drug_name_selected,disease_name_selected,))

    # Aquí habría que poner el conn.commit() si no estuviese el autocommit

    print('Número de filas eliminadas: %s' % (cursor.rowcount))

    cursor.close()


# %%
# 7. Insertions
def query_7(conn):
    cursor = conn.cursor()
    query = """
            INSERT INTO drug_has_code
            VALUES (
	            (SELECT drug_id
	            FROM drug
	            WHERE drug_name = %s),
	            %s,
	            %s);
          """
    
    print("Va a proceder a crear una nueva entrada en la base de datos con la información de codificación de un fármaco ya existente.")
    print("Debe introducir los siguientes valores separados por comas en el siguiente orden: nombre del fármaco, nuevo identificador del fármaco y nombre del vocabulario")
    request = input("Por favor, introduzca los valores: ")
    list_drug_code_values = [item.strip() for item in request.split(',')]


    drug_name = list_drug_code_values[0]
    drug_code = list_drug_code_values[1]
    vocabulary = list_drug_code_values[2]
    
    cursor.execute(query,(drug_name,drug_code,vocabulary,))

    print('Número de filas insertadas: %s' % (cursor.rowcount))

    cursor.close()

