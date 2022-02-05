import mysql.connector
from mysql.connector import errorcode

from .connect import DBConnection

def execute(sql, is_insert)->bool:
	db = DBConnection()

	with db.connect() as cnx:
		with cnx.cursor() as cursor:
			try:
				cursor.execute(sql)
				cnx.commit()

				if is_insert:
					return cursor.lastrowid
				else:
					return True
			
			except	mysql.connector.Error as err:
				if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
					pass
				else:
					raise err