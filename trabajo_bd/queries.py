# %%
# Authors: Nerea Barrio, Gabriel Coll
# Script to define the different queries that will be used

import mysql.connector


# %%

# 1. General information

# 1a. Total number

# 1ai. Total number of drugs
def query_1ai(conn):

    # Cursor
    cursor = conn.cursor() 

    # Execute query
    query = """
            SELECT COUNT(DISTINCT drug_id) NumDrugs FROM drug;
            """
    
    print("Mostrando todos los fármacos:")

    cursor.execute(query)

    # Manage results
    data = cursor.fetchall()

    # Close cursor
    cursor.close()

    print()

    return data[0][0]

# 1aii. Total number of diseases
def query_1aii(conn):

    # Cursor
    cursor = conn.cursor()

    # Execute query
    query = """
            SELECT COUNT(DISTINCT disease_id) NumDiseases FROM disease;
            """
    
    print("Mostrando todas las enfermedades:")

    cursor.execute(query)

    # Handle results
    data = cursor.fetchall()

    # Close cursor
    cursor.close()

    print()

    return data[0][0]

# 1aiii. Total number of phenotype effects
def query_1aiii(conn):

    # Cursor
    cursor = conn.cursor()

    # Execute query
    query = """
            SELECT COUNT(DISTINCT phenotype_id) NumPhenoEff FROM phenotype_effect;
            """
    
    print("Mostrando todos los efectos fenotípicos:")

    cursor.execute(query)

    # Handle results
    data = cursor.fetchall()

    # Close the cursor
    cursor.close()

    print()

    return data[0][0]

# 1aiv. Total number of targets
def query_1aiv(conn):

    # Cursor
    cursor = conn.cursor()

    # Execute the query
    query = """
            SELECT COUNT(DISTINCT target_id) NumTargets FROM target;
            """
    
    print("Mostrando todas las dianas (targets):")

    cursor.execute(query)

    # Get the results
    data = cursor.fetchall()

    # Close the cursor
    cursor.close()

    print()

    return data[0][0]


# 1b. First ten instances

# 1bi. First ten drugs
def query_1bi(conn):

    # Cursor
    cursor = conn.cursor()

    # Execute query
    query = """
            SELECT drug_id, drug_name, molecular_type, chemical_structure, inchi_key
            FROM drug WHERE drug_id IS NOT NULL AND drug_name IS NOT NULL
            AND molecular_type IS NOT NULL
            AND chemical_structure IS NOT NULL AND inchi_key IS NOT NULL
            LIMIT 10;
            """
    
    print("Mostrando los primeros diez fármacos:")
    print("\n(ID, nombre, tipo molecular, estructura química, InChI key)")

    cursor.execute(query)

    # Get the results
    data = cursor.fetchall()

    # Close the cursor
    cursor.close()

    print()

    # Return the results in an elegant format
    for item in data:
        result = f"{item[0]}    {item[1]}    {item[2]}    {item[3]}    {item[4]}"
        print(result)
    
    
    

# 1bii. First ten diseases
def query_1bii(conn):

    # Cursor
    cursor = conn.cursor()

    # Execute the query
    query = """
            SELECT * FROM disease WHERE disease_id IS NOT NULL
            AND disease_name IS NOT NULL
            LIMIT 10;
            """
    
    print("Mostrando las primeras diez enfermedades:")
    print("\n(ID, nombre)")

    cursor.execute(query)

    # Get the results
    data = cursor.fetchall()

    # Close the cursor
    cursor.close()

    print()

    # Return the result in a prettier format
    for item in data:
        result = f"{item[0]}    {item[1]}"
        print(result)

    

# 1biii. First ten phenotype effects
def query_1biii(conn):

    # Cursor
    cursor = conn.cursor()

    # Execute the query
    query = """
            SELECT * FROM phenotype_effect
            WHERE phenotype_id IS NOT NULL
            AND phenotype_name IS NOT NULL
            LIMIT 10;
            """
    
    print("Mostrando los primeros diez efectos fenotípicos:")
    print("\n(ID, nombre)")

    cursor.execute(query)

    # Get the results
    data = cursor.fetchall()

    # Close the cursor
    cursor.close()

    # Print the results in a friendly format
    print()

    for item in data:
        result = f"{item[0]}    {item[1]}"
        print(result)


# 1biv. First ten targets
def query_1biv(conn):

    # Cursor
    cursor = conn.cursor()

    # Execute the query
    query = """
            SELECT t.target_id, t.target_name_pref, t.target_type, o.taxonomy_name
            FROM target t, organism o
            WHERE t.organism_id=o.taxonomy_id
            AND t.target_id IS NOT NULL
            AND t.target_name_pref IS NOT NULL
            AND t.target_type IS NOT NULL
            AND o.taxonomy_name IS NOT NULL
            LIMIT 10;
            """
    
    print("Mostrando las primeras diez dianas (targets):")
    print("\n(ID, nombre, tipo, organismo)")

    cursor.execute(query)

    # Get the results
    data = cursor.fetchall()

    # Close the cursor
    cursor.close()

    print()

    # Print the results
    for item in data:
        result = f"{item[0]}    {item[1]}    {item[2]}    {item[3]}"
        print(result)



# 2. Information about drugs

# 2a. Information on a drug, given its ChEMBL ID
def query_2a(conn):

    # Cursor
    cursor = conn.cursor()

    # Execute the query
    query = """
            SELECT drug_name, molecular_type, chemical_structure, inchi_key
            FROM drug WHERE drug_id=%s;
            """
    
    print("Introduzca el ID ChEMBL de un fármaco y a continuación se mostrará su nombre, tipo, estructura e InChi-key.")
    drug_id = input("ChEMBL ID: ")

    cursor.execute(query,(drug_id,))

    # Get the results
    data = cursor.fetchall()

    # Close the cursor
    cursor.close()

    # Print the results
    print()

    if not data:
        print("El ID introducido fue mal escrito o no se encuentra en la base de datos")

    for item in data:
        print(f"Nombre: {item[0]}")
        print(f"Tipo: {item[1]}")
        print(f"Estructura: {item[2]}")
        print(f"InChi-Key: {item[3]}")
        


# 2b. Synonymous names of a drug, given its name
def query_2b(conn):

    # Cursor
    cursor = conn.cursor()

    # Execute the query
    query = """
            SELECT s.synonymous_name FROM synonymous s, drug d
            WHERE d.drug_id=s.drug_id AND d.drug_id=(SELECT drug_id
            FROM drug WHERE drug_name=%s);
            """
    
    print("Introduzca el nombre de un fármaco y a continuación se mostrarán sus sinónimos.")
    drug_name = input("Nombre del fármaco: ")

    cursor.execute(query,(drug_name,))

    # Get the results
    data = cursor.fetchall()

    # Close the cursor
    cursor.close()

    # Print the results
    print()

    if not data:
        print("El nombre introducido fue mal escrito, no se encuentra en la base de datos o no cuenta con sinónimos")

    for item in data: 
        print(item[0])


    

# 2c. ATC codes associated to a drug, given its ChEMBL ID
def query_2c(conn):

    # Cursor
    cursor = conn.cursor()

    # Execute the query
    query = """
            SELECT atc_code_id FROM atc_code
            WHERE drug_id=%s;
            """
    
    print("Introduzca el ID ChEMBL de un fármaco y a continuación se mostrarán los códigos ATC asociados a él.")
    drug_id = input("ChEMBL ID: ")

    cursor.execute(query,(drug_id,))

    # Get the results
    data = cursor.fetchall()

    # Close the cursor
    cursor.close()

    # Print the results
    print()

    if not data:
        print("El ID introducido fue mal escrito o no se encuentra en la base de datos")

    for item in data: 
        print(item[0])

    


# 3. Information about diseases

# 3a. Drugs used to treat a disease, given its name
def query_3a(conn):

    # Cursor
    cursor = conn.cursor()

    # Execute the query
    query = """
            SELECT d.drug_id, d.drug_name
            FROM drug d, disease_code dc, drug_disease dd
            WHERE dc.name=%s
            AND dc.code_id=dd.code_id AND d.drug_id=dd.drug_id;
            """
    
    print("Introduzca el nombre de una enfermedad y a continuación se mostrarán los identificadores y nombres de los fármacos usados para tratarla.")
    disease_name = input("Nombre de la enfermedad: ")

    cursor.execute(query,(disease_name,))

    # Get the results
    data = cursor.fetchall()

    # Close the cursor
    cursor.close()

    # Print the results
    print()

    if not data:
        print("El nombre introducido fue mal escrito o la base de datos no cuenta con fármacos para tratar la enfermedad")

    for item in data:
        result = f"{item[0]}    {item[1]}"
        print(result)

# 3b. Show the names of the drug and disease whose inferred association score is the highest
def query_3b(conn):

    # Cursor
    cursor = conn.cursor()

    # Execute the query
    query = """
            SELECT dc.name, d.drug_name, dd.inferred_score
            FROM drug d, disease_code dc, drug_disease dd
            WHERE dc.code_id=dd.code_id AND d.drug_id=dd.drug_id
            ORDER BY dd.inferred_score DESC
            LIMIT 1;
            """
    
    print("Mostrando el fármaco y la enfermedad que comparten el mayor puntaje de asociación:")

    cursor.execute(query)

    # Get the results
    data = cursor.fetchall()

    # Close the cursor
    cursor.close()

    # Print the results
    print()

    for item in data:
        print(f"Enfermedad: {item[0]}")
        print(f"Fármaco: {item[1]}")
        print(f"Score: {item[2]}")



# 4. Information about phenotype effects

# 4a. Phenotype effects indicated to a drug, given its ChEMBL ID
def query_4a(conn):

    # Cursor
    cursor = conn.cursor()

    # Execute the query
    query = """
            SELECT p.phenotype_id, p.phenotype_name
            FROM drug d, phenotype_effect p, drug_phenotype_effect dp
            WHERE d.drug_id=%s
            AND dp.phenotype_id=p.phenotype_id
            AND d.drug_id=dp.drug_id;
            """
    
    print("Introduzca el ID ChEMBL de un fármaco y a continuación se mostrarán los identificadores y nombres de los efectos fenotípicos asociados a él.")
    drug_id = input("ChEMBL ID: ")

    cursor.execute(query,(drug_id,))

    # Get the results
    data = cursor.fetchall()

    # Close the cursor
    cursor.close()

    # Print the results
    print()

    if not data:
        print("El ID introducido fue mal escrito, no se encuentra en la base de datos o no tiene efectos fenotípicos tipificados")

    for item in data:
        result = f"{item[0]}    {item[1]}"
        print(result)


# 4b. Side effects of a given drug, given its ChEMBL ID
def query_4b(conn):

    # Cursor
    cursor = conn.cursor()

    # Execute the query
    query = """
            SELECT p.phenotype_id, p.phenotype_name, dp.score
            FROM drug d, phenotype_effect p, drug_phenotype_effect dp
            WHERE d.drug_id=%s
            AND dp.phenotype_id=p.phenotype_id AND d.drug_id=dp.drug_id
            AND dp.phenotype_type="SIDE EFFECT"
            ORDER BY dp.score DESC;
            """
    
    print("Introduzca el ID ChEMBL de un fármaco y a continuación se mostrarán los identificadores y nombres de los efectos secundarios asociados a él, ordenados de mayor a menos puntaje.")
    drug_id = input("ChEMBL ID: ")

    cursor.execute(query,(drug_id,))

    # Get the results
    data = cursor.fetchall()

    # Close the cursor
    cursor.close()

    # Print the results
    print()

    if not data:
        print("El ID introducido fue mal escrito, no se encuentra en la base de datos o no tiene efectos secundarios tipificados")

    for item in data:
        result = f"{item[0]}    {item[1]}    {item[2]}"
        print(result)



# 5. Information about targets

# 5a. Targets of a certain target type given
def query_5a(conn):

    # Cursor
    cursor = conn.cursor()

    # Execute the query
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

    # Get the results
    data = cursor.fetchall()

    # Close the cursor
    cursor.close()

    # Print the results
    print()

    if not data:
        print("El tipo introducido fue mal escrito o no se encuentra en la base de datos")
    else:
        print("Lista de las 20 primeras dianas ordenadas alfabéticamente:")

    for item in data:
        print(item[0])



# 5b. Organism with the most number of targets
def query_5b(conn):

    # Cursor
    cursor = conn.cursor()

    # Execute the query
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

    # Get the results
    data = cursor.fetchone()

    # Close the cursor
    cursor.close()

    # Print the results
    print()

    print("Organismo con mayor número de dianas distintas: ", data[0])




# Modification queries

# 6. Deletes
def query_6(conn):

    # Cursor
    cursor = conn.cursor()

    # Execute the first query
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

    # Get the results
    interactions = cursor.fetchall()

    # Execute the second query
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

    # Print the list with a prettier format, easier to select
    for row in interactions:
        print("[",j,"]. ", row)
        j = j+1
    
    # Store the values of the chosen item in the list
    option_number = int(input("Por favor, introduzca el número de la fila que desea eliminar: "))

    inferred_score_selected = interactions[option_number-1][0]
    drug_name_selected = interactions[option_number-1][1]
    disease_name_selected = interactions[option_number-1][2]

    # Make sure the user knows he is about to delete certain values of the database
    print("¿Desea eliminar la siguiente asociación de fármaco y enfermedad?")
    print(f"Fármaco: {drug_name_selected}\nEnfermedad: {disease_name_selected}\nScore: {inferred_score_selected}")

    answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()
    
    match answer:
        case "s":
            cursor.execute(query2,(inferred_score_selected-0.005,inferred_score_selected+0.005,drug_name_selected,disease_name_selected,))
            print('Número de filas eliminadas: %s' % (cursor.rowcount))

        case _:
            print("No se modificó ningún valor")

    # Close the cursor
    cursor.close()



# 7. Insertions
def query_7(conn):

    # Cursor
    cursor = conn.cursor()

    # Execute the query
    query = """
            INSERT INTO drug_has_code
            VALUES (
	            (SELECT drug_id
	            FROM drug
	            WHERE drug_name = %s),
	            %s,
	            %s);
          """
    
    # Store the values given by the user in separate variables
    print("Va a proceder a crear una nueva entrada en la base de datos con la información de codificación de un fármaco ya existente.")
    print("Debe introducir los siguientes valores separados por comas en el siguiente orden: nombre del fármaco, nuevo identificador del fármaco y nombre del vocabulario")
    request = input("Por favor, introduzca los valores: ")
    list_drug_code_values = [item.strip() for item in request.split(',')]


    drug_name = list_drug_code_values[0]
    drug_code = list_drug_code_values[1]
    vocabulary = list_drug_code_values[2]

    # Make sure the drug name provided already exists in the database
    cursor.execute("SELECT * FROM drug WHERE drug_name=%s;",(drug_name,))

    data=cursor.fetchall()

    if not data:
        print("El nombre de fármaco introducido no existe en la base de datos")
    else:
        # Make sure the user knows he is about to insert new information in the database
        print("¿Desea introducir la siguiente entrada en la base de datos?")
        print(f"{drug_name}    {drug_code}    {vocabulary}")

        answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()
        
        match answer:
            case "s":
                cursor.execute(query,(drug_name,drug_code,vocabulary,))
                print('Número de filas insertadas: %s' % (cursor.rowcount))

            case _:
                print("No se modificó ningún valor")

    # Close the cursor
    cursor.close()


# 8. Modifications
def query_8(conn):

    # Cursor
    cursor = conn.cursor()

    # Define the queries
    query_selection = """
           SELECT * FROM drug_phenotype_effect
           WHERE score<%s
           AND phenotype_type="SIDE EFFECT";
           """

    query_modification = """
            UPDATE drug_phenotype_effect SET score=0
            WHERE score<%s
            AND phenotype_type="SIDE EFFECT";
            """ 

    # Execute the first query
    print("Introduzca un número de puntaje (score) y a continuación se mostrarán las asociaciones entre fármacos y efectos secundarios cuyo puntaje sea inferior al dado.")
    score = input("Score: ")

    cursor.execute(query_selection,(score,))

    # Get the result
    data = cursor.fetchall()

    print("\nAsociaciones con puntaje inferior:\n")
    print("\n(ID_fenotipo, ID_fármaco, ID_fuente, SCORE, efecto fenotípico)\n")

    # Return the results in an elegant format
    for item in data:
        result = f"{item[0]}    {item[1]}    {item[2]}    {item[3]}    {item[4]}"
        print(result)

    # Make sure the user knows they are about to change certain database values
    answer = input("¿Desea reemplazar estas puntuaciones por 0? Escribir 's' si se desea, o cualquier otro carácter si no").lower()
    
    # Execute the second query if the user is sure
    match answer:
        case "s":
            cursor.execute("""SET SQL_SAFE_UPDATES = 0;""") # Remove the safe update mode
            cursor.execute(query_modification,(score,)) # Execute the query
            print('Número de puntajes anulados: %s' % (cursor.rowcount))
            cursor.execute("""SET SQL_SAFE_UPDATES = 1;""") # Restore the safe update mode

        case _:
            print("No se modificó ningún valor")

    # Close the cursor
    cursor.close()

#%%
