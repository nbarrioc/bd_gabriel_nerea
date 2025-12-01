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

    print("Bienvenido/a al sistema de acceso a la base de datos\nLas secciones son las siguientes:\n")
    print("1. Información general\n2. Información sobre fármacos\n3. Información sobre enfermedades\n4. Información sobre efectos fenotípicos\n5. Información sobre dianas (targets)\n6. Borrados\n7. Inserciones\n8. Modificaciones\n")
    section = input("Introduzca el número de sección al que desea acceder ")

    match section:
        case 1:
            # 1. General information

            print("1. Información general\nSecciones:\n\n")
            
            print("1a. Número total\n1b. Primeras diez instancias\n")

            section1 = input("Introduzca el número de sección al que desea acceder ")

            match section1:
                case "1a":
                    # 1a. Total number

                    print("1a. Número total\nSecciones:\n\n")
            
                    print("i. Número total de fármacos\nii. Número total de enfermedades\niii. Número total de efectos fenotípicos\niv. Número total de dianas (targets)\n")

                    section1a = input("Introduzca el número de sección al que desea acceder ")

                    match section1a:
                        case "i":
                            # 1ai. Total number of drugs
                            queries.query_1ai(conn)

                        case "ii":
                            # 1aii. Total number of diseases
                            queries.query_1aii(conn)

                        case "iii":
                            # 1aiii. Total number of phenotype effects
                            queries.query_1aiii(conn)

                        case "iv":
                            # 1aiv. Total number of targets
                            queries.query_1aiv(conn)

                        case _:
                            print("La sección introducida no es válida")

                case "1b":
                    # 1b. First ten instances

                    print("1b. Primeras diez instancias\nSecciones:\n\n")
            
                    print("i. Primeros diez fármacos\nii. Primeras diez enfermedades\niii. Primeros diez efectos fenotípicos\niv. Primeras diez dianas (targets)\n")

                    section1b = input("Introduzca el número de sección al que desea acceder ")

                    match section1b:
                        case "i":
                            # 1bi. First ten drugs
                            queries.query_1bi(conn)

                        case "ii":
                            # 1bii. First ten diseases
                            queries.query_1bii(conn)

                        case "iii":
                            # 1biii. First ten phenotype effects
                            queries.query_1biii(conn)

                        case "iv":
                            # 1biv. First ten targets
                            queries.query_1biv(conn)

                        case _:
                            print("La sección introducida no es válida")

        case 2:
            # 2. Information about drugs

            print("2. Información sobre fármacos\nSecciones:\n\n")
            
            print("2a. Información sobre un fármaco\n2b. Sinónimos de un fármaco\n2c. Códigos ATC asociados a un fármaco\n")

            section2 = input("Introduzca el número de sección al que desea acceder ")

            match section2:
                case "2a":
                    # 2a. Information on a drug, given its ChEMBL ID
                    queries.query_2a(conn)

                case "2b":
                    # 2b. Synonymous names of a drug, given its name
                    queries.query_2b(conn)

                case "2c":
                    # 2c. ATC codes associated to a drug, given its ChEMBL ID
                    queries.query_2c(conn)

                case _:
                    print("La sección introducida no es válida")

        case 3:
            # 3. Information about diseases

            print("3. Información sobre enfermedades\nSecciones:\n\n")
            
            print("3a. Fármacos para tratar una enfermedad\n3b. Fármaco y enfermedad con mayor puntaje de asociación inferido\n")

            section3 = input("Introduzca el número de sección al que desea acceder ")

            match section3:
                case "3a":
                    # 3a. Drugs used to treat a disease, given its name
                    queries.query_3a(conn)

                case "3b":
                    # 3b. Show the names of the drug and disease whose inferred association score is the highest
                    queries.query_3b(conn)

                case _:
                    print("La sección introducida no es válida")

        case 4:
            # 4. Information about phenotype effects

            print("4. Información sobre efectos secundarios\nSecciones:\n\n")
            
            print("4a. Efectos fenotípicos de un fármaco\n4b. Efectos secundarios de un fármaco\n")

            section4 = input("Introduzca el número de sección al que desea acceder ")

            match section4:
                case "4a":
                    # 4a. Phenotype effects indicated to a drug, given its ChEMBL ID
                    queries.query_4a(conn)

                case "4b":
                    # 4b. Side effects of a given drug, given its ChEMBL ID
                    queries.query_4b(conn)

                case _:
                    print("La sección introducida no es válida")

        case 5:
            # 5. Information about targets

            print("5. Información sobre dianas (targets)\nSecciones:\n\n")
            
            print("5a. Dianas de un tipo\n5b. Organismo con el mayor número de dianas\n")

            section5 = input("Introduzca el número de sección al que desea acceder ")

            match section4:
                case "5a":
                    # 5a. Targets of a certain type given
                    list_targets = queries.query_5a(conn)

                    print("Lista de las 20 primeras dianas ordenadas alfabéticamente:")

                    for target in list_targets:
                        print(target[0])

                case "5b":
                    # 5b. Organism with the most number of targets
                    org_more_targets = queries.query_5b(conn)

                    print("Organismo con mayor número de dianas distintas: ", org_more_targets[0])

                case _:
                    print("La sección introducida no es válida")

        case 6:
            # 6. Deletes

            print("6. Borrados\n")

            queries.query_6(conn)

        case 7:
            # 7. Insertions

            print("7. Inserciones\n")

            queries.query_7(conn)

        case 8:
            # 8. Modifications

            print("8. Modificaciones\n")

            queries.query_8(conn)

        case _:
            print("La sección introducida no es válida")


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

