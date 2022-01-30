from .connect import DBConnection

def fetch(sql) ->list:
	db = DBConnection()
	results = []

	with db.connect() as cnx:
		with cnx.cursor() as cursor:
			cursor.execute(sql)
			for result in cursor:
				results.append(result)
	return results