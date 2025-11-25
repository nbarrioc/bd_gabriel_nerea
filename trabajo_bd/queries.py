# Script to define the different queries that will be used

# Selection queries

query_5a = """
           SELECT target_name_pref
           FROM target
           WHERE target_type = "%s"
           ORDER BY target_name_pref ASC
           LIMIT 20;
           """

query_5b = """
           SELECT taxonomy_name
           FROM organism, 
                (SELECT organism_id, COUNT(DISTINCT target_id) ntarget
	            FROM target
	            GROUP BY organism_id
	            ORDER BY ntarget DESC
	            LIMIT 1) ntar
           WHERE taxonomy_id=organism_id;
           """

# Modification queries

query_6a = """
           SELECT inferred_score, drug_name, disease_name
           FROM drug_disease, drug, disease_has_code, disease
           WHERE inferred_score IS NOT NULL AND
           drug_disease.drug_id=drug.drug_id AND
           drug_disease.code_id=disease_has_code.code_id AND
           disease_has_code.disease_id=disease.disease_id
           ORDER BY inferred_score, drug_name, disease_name ASC
           LIMIT 10;
           """

query_6b = """
           DELETE FROM drug_disease
           WHERE inferred_score=%s AND
           drug_id =
                (SELECT drug_id
                FROM drug
                WHERE drug_name="%s") AND
           code_id =
            	(SELECT code_id
	            FROM disease_has_code, disease
	            WHERE disease_name="%s" AND
		            disease_has_code.disease_id=disease.disease_id);"""

query_7 = """
          INSERT INTO drug_has_code
          VALUES (
	          (SELECT drug_id
	          FROM drug
	          WHERE drug_name = "%s"),
	          %s,
	          "%s");
          """