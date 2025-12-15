# %% 
# Authors: Nerea Barrio, Gabriel Coll
# Script  to access the database to fetch or modify information

# Establish the connection
import mysql.connector
from mysql.connector import errorcode
from connection import get_connection
# Import the file containing the different posible queries to carry out
import queries

# %%
# Handle possible errors related to the connection to the database (shown towards the end of the script)
try: 
    conn = get_connection()
    print('Conexión satisfactoria')

    # Starting menu and queries
    while True:

        print("\nBienvenido/a al sistema de acceso a la base de datos\nLas secciones son las siguientes:\n")
        print("1. Información general\n2. Información sobre fármacos\n3. Información sobre enfermedades\n4. Información sobre efectos fenotípicos\n5. Información sobre dianas (targets)\n6. Borrados\n7. Inserciones\n8. Modificaciones\n9. Salir\n")
        section = input("Introduzca el número de sección al que desea acceder\n")

        match section:
            case "1":
                # 1. General information

                print("1. Información general\nSecciones:\n\n")
                
                print("1a. Número total\n1b. Primeras diez instancias\n1c. Volver al menú principal\n1d. Salir\n")

                section1 = input("Introduzca el número de sección al que desea acceder\n").lower()

                match section1:
                    case "1a":
                        # 1a. Total number

                        print("1a. Número total\nSecciones:\n\n")
                
                        print("i. Número total de fármacos\nii. Número total de enfermedades\niii. Número total de efectos fenotípicos\niv. Número total de dianas (targets)\nv. Volver al menú principal\nvi. Salir\n")

                        section1a = input("Introduzca el número de sección al que desea acceder\n").lower()

                        match section1a:
                            case "i":
                                # 1ai. Total number of drugs
                                total_drugs = queries.query_1ai(conn)
                                print(total_drugs)

                                print("\n¿Desea volver al menú principal?\n")
                                answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                                match answer:
                                    case "s":
                                        continue   # keep program open
                                    case _:
                                        print("Saliendo del programa...")   # close the program
                                        break

                            case "ii":
                                # 1aii. Total number of diseases
                                total_diseases = queries.query_1aii(conn)
                                print(total_diseases)

                                print("\n¿Desea volver al menú principal?\n")
                                answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                                match answer:
                                    case "s":
                                        continue   # keep program open
                                    case _:
                                        print("Saliendo del programa...")   # close the program
                                        break

                            case "iii":
                                # 1aiii. Total number of phenotype effects
                                total_phenotype_effects = queries.query_1aiii(conn)
                                print(total_phenotype_effects)

                                print("\n¿Desea volver al menú principal?\n")
                                answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                                match answer:
                                    case "s":
                                        continue   # keep program open
                                    case _:
                                        print("Saliendo del programa...")   # close the program
                                        break

                            case "iv":
                                # 1aiv. Total number of targets
                                total_targets = queries.query_1aiv(conn)
                                print(total_targets)

                                print("\n¿Desea volver al menú principal?\n")
                                answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                                match answer:
                                    case "s":
                                        continue   # keep program open
                                    case _:
                                        print("Saliendo del programa...")   # close the program
                                        break

                            case "v":
                                print()   # keep program open
                                continue

                            case "vi":
                                print("\nSaliendo del programa...\n")   # close the program
                                break

                            case _:
                                print("La sección introducida no es válida")   # input section identifier does not match any

                                print("\n¿Desea volver al menú principal?\n")
                                answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                                match answer:
                                    case "s":
                                        continue   # keep program open
                                    case _:
                                        print("Saliendo del programa...")   # close the program
                                        break

                    case "1b":
                        # 1b. First ten instances

                        print("1b. Primeras diez instancias\nSecciones:\n\n")
                
                        print("i. Primeros diez fármacos\nii. Primeras diez enfermedades\niii. Primeros diez efectos fenotípicos\niv. Primeras diez dianas (targets)\nv. Volver al menú principal\nvi. Salir")

                        section1b = input("Introduzca el número de sección al que desea acceder\n").lower()

                        match section1b:
                            case "i":
                                # 1bi. First ten drugs
                                ten_drugs = queries.query_1bi(conn)
                                ten_drugs

                                print("\n¿Desea volver al menú principal?\n")
                                answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                                match answer:
                                    case "s":
                                        continue   # keep program open
                                    case _:
                                        print("Saliendo del programa...")   # close the program
                                        break

                            case "ii":
                                # 1bii. First ten diseases
                                ten_diseases = queries.query_1bii(conn)
                                ten_diseases

                                print("\n¿Desea volver al menú principal?\n")
                                answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                                match answer:
                                    case "s":
                                        continue   # keep program open
                                    case _:
                                        print("Saliendo del programa...")   # close the program
                                        break

                            case "iii":
                                # 1biii. First ten phenotype effects
                                ten_phenotype_effects = queries.query_1biii(conn)
                                ten_phenotype_effects

                                print("\n¿Desea volver al menú principal?\n")
                                answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                                match answer:
                                    case "s":
                                        continue   # keep program open
                                    case _:
                                        print("Saliendo del programa...")   # close the program
                                        break

                            case "iv":
                                # 1biv. First ten targets
                                ten_targets = queries.query_1biv(conn)
                                ten_targets

                                print("\n¿Desea volver al menú principal?\n")
                                answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                                match answer:
                                    case "s":
                                        continue   # keep program open
                                    case _:
                                        print("Saliendo del programa...")   # close the program
                                        break

                            case "v":
                                print()   # keep program open
                                continue

                            case "vi":
                                print("\nSaliendo del programa...\n")   # close the program
                                break

                            case _:
                                print("La sección introducida no es válida")   # input section identifier does not match any

                                print("\n¿Desea volver al menú principal?\n")
                                answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                                match answer:
                                    case "s":
                                        continue   # keep program open
                                    case _:
                                        print("Saliendo del programa...")   # close the program
                                        break
                    
                    case "1c":
                        print()   # keep program open
                        continue

                    case "1d":
                        print("\nSaliendo del programa...\n")   # close the program
                        break
                    
                    case _:
                        print("La sección introducida no es válida")   # input section identifier does not match any

                        print("\n¿Desea volver al menú principal?\n")
                        answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                        match answer:
                            case "s":
                                continue   # keep program open
                            case _:
                                print("Saliendo del programa...")   # close the program
                                break


            case "2":
                # 2. Information about drugs

                print("2. Información sobre fármacos\nSecciones:\n\n")
                
                print("2a. Información sobre un fármaco\n2b. Sinónimos de un fármaco\n2c. Códigos ATC asociados a un fármaco\n2d. Volver al menú principal\n2e. Salir\n")

                section2 = input("Introduzca el número de sección al que desea acceder\n").lower()

                match section2:
                    case "2a":
                        # 2a. Information on a drug, given its ChEMBL ID
                        drug_info = queries.query_2a(conn)
                        drug_info

                        print("\n¿Desea volver al menú principal?\n")
                        answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                        match answer:
                            case "s":
                                continue   # keep program open
                            case _:
                                print("Saliendo del programa...")   # close the program
                                break

                    case "2b":
                        # 2b. Synonymous names of a drug, given its name
                        drug_synonym = queries.query_2b(conn)
                        drug_synonym

                        print("\n¿Desea volver al menú principal?\n")
                        answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                        match answer:
                            case "s":
                                continue   # keep program open
                            case _:
                                print("Saliendo del programa...")   # close the program
                                break

                    case "2c":
                        # 2c. ATC codes associated to a drug, given its ChEMBL ID
                        drug_ATC = queries.query_2c(conn)
                        drug_ATC

                        print("\n¿Desea volver al menú principal?\n")
                        answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                        match answer:
                            case "s":
                                continue   # keep program open
                            case _:
                                print("Saliendo del programa...")   # close the program
                                break
                    
                    case "2d":
                        print()   # keep program open
                        continue

                    case "2e":
                        print("\nSaliendo del programa...\n")   # close the program
                        break

                    case _:
                        print("La sección introducida no es válida")   # input section identifier does not match any

            case "3":
                # 3. Information about diseases

                print("3. Información sobre enfermedades\nSecciones:\n\n")
                
                print("3a. Fármacos para tratar una enfermedad\n3b. Fármaco y enfermedad con mayor puntaje de asociación inferido\n3c. Volver al menú principal\n3d. Salir\n")

                section3 = input("Introduzca el número de sección al que desea acceder\n").lower()

                match section3:
                    case "3a":
                        # 3a. Drugs used to treat a disease, given its name
                        drug_disease = queries.query_3a(conn)
                        drug_disease

                        print("\n¿Desea volver al menú principal?\n")
                        answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                        match answer:
                            case "s":
                                continue   # keep program open
                            case _:
                                print("Saliendo del programa...")   # close the program
                                break

                    case "3b":
                        # 3b. Show the names of the drug and disease whose inferred association score is the highest
                        drug_disease_higher_score = queries.query_3b(conn)
                        drug_disease_higher_score

                        print("\n¿Desea volver al menú principal?\n")
                        answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                        match answer:
                            case "s":
                                continue   # keep program open
                            case _:
                                print("Saliendo del programa...")   # close the program
                                break

                    case "3c":
                        print()   # keep program open
                        continue

                    case "3d":
                        print("\nSaliendo del programa...\n")   # close the program
                        break
                    
                    case _:
                        print("La sección introducida no es válida")   # input section identifier does not match any

            case "4":
                # 4. Information about phenotype effects

                print("4. Información sobre efectos secundarios\nSecciones:\n\n")
                
                print("4a. Efectos fenotípicos de un fármaco\n4b. Efectos secundarios de un fármaco\n4c. Volver al menú principal\n4d. Salir\n")

                section4 = input("Introduzca el número de sección al que desea acceder\n").lower()

                match section4:
                    case "4a":
                        # 4a. Phenotype effects indicated to a drug, given its ChEMBL ID
                        drug_phenotype_effect = queries.query_4a(conn)
                        drug_phenotype_effect

                        print("\n¿Desea volver al menú principal?\n")
                        answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                        match answer:
                            case "s":
                                continue   # keep program open
                            case _:
                                print("Saliendo del programa...")   # close the program
                                break

                    case "4b":
                        # 4b. Side effects of a given drug, given its ChEMBL ID
                        drug_side_effects = queries.query_4b(conn)
                        drug_side_effects

                        print("\n¿Desea volver al menú principal?\n")
                        answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                        match answer:
                            case "s":
                                continue   # keep program open
                            case _:
                                print("Saliendo del programa...")   # close the program
                                break

                    case "4c":
                        print()   # keep program open
                        continue

                    case "4d":
                        print("\nSaliendo del programa...\n")   # close the program
                        break

                    case _:
                        print("La sección introducida no es válida")   # input section identifier does not match any

            case "5":
                # 5. Information about targets

                print("5. Información sobre dianas (targets)\nSecciones:\n\n")
                
                print("5a. Dianas de un tipo\n5b. Organismo con el mayor número de dianas\n5c. Volver al menú principal\n5d. Salir\n")

                section5 = input("Introduzca el número de sección al que desea acceder\n").lower()

                match section5:
                    case "5a":
                        # 5a. Targets of a certain type given
                        list_targets = queries.query_5a(conn)
                        list_targets

                        print("\n¿Desea volver al menú principal?\n")
                        answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                        match answer:
                            case "s":
                                continue   # keep program open
                            case _:
                                print("Saliendo del programa...")   # close the program
                                break

                    case "5b":
                        # 5b. Organism with the most number of targets
                        org_more_targets = queries.query_5b(conn)
                        org_more_targets

                        print("\n¿Desea volver al menú principal?\n")
                        answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                        match answer:
                            case "s":
                                continue   # keep program open
                            case _:
                                print("Saliendo del programa...")   # close the program
                                break
                        
                    case "5c":
                        print()   # keep program open
                        continue

                    case "5d":
                        print("\nSaliendo del programa...\n")   # close the program
                        break
                    
                    case _:
                        print("La sección introducida no es válida")    # input section identifier does not match any

            case "6":
                # 6. Deletes

                print("6. Borrados\n")

                queries.query_6(conn)

                print("\n¿Desea volver al menú principal?\n")
                answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                match answer:
                    case "s":
                        continue   # keep program open
                    case _:
                        print("Saliendo del programa...")   # close the program
                        break

            case "7":
                # 7. Insertions

                print("7. Inserciones\n")

                queries.query_7(conn)

                print("\n¿Desea volver al menú principal?\n")
                answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                match answer:
                    case "s":
                        continue   # keep program open
                    case _:
                        print("Saliendo del programa...")   # close the program
                        break

            case "8":
                # 8. Modifications

                print("8. Modificaciones\n")

                queries.query_8(conn)

                print("\n¿Desea volver al menú principal?\n")
                answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                match answer:
                    case "s":
                        continue   # keep program open
                    case _:
                        print("Saliendo del programa...")   # close the program
                        break
            
            case "9":
                print("\n¿Está seguro de que desea salir del programa?\n")
                answer = input("Escribir 's' si se desea, o cualquier otro carácter si no").lower()

                match answer:
                    case "s":
                        print("Saliendo del programa...")   # close the program
                        break 

                    case _:
                        continue   # keep program open

            case _:
                print("La sección introducida no es válida")   # input section identifier does not match any


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Usuario y/o contraseña incorrectos')   # when the user and/or password provided do not match the ones on the database
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('Nombre de la base de datos incorrecto.')   # when the given database name is not correct
    else:
        print(err)
else: 
    conn.close()
    print('\nSe ha cerrado la conexión correctamente')   # message that lets the user know that the program was correctly closed and stopped executing



# %%
