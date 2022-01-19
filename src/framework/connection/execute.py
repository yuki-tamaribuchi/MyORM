import mysql.connector
from mysql.connector import errorcode

from .connect import DBConnection

def execute(sql)->bool:
	db = DBConnection()

	with db.connect() as cnx:
		with cnx.cursor() as cursor:
			try:
				cursor.execute(sql)
				return True
			
			except	mysql.connector.Error as err:
				if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
					print('Table already exists.')
				else:
					raise err