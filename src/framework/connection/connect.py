import mysql.connector
from mysql.connector import errorcode

from framework.exceptions.connection.base import DatabaseCreatedException

from settings.databases import DATABASES_LIST


def connect():
	user = DATABASES_LIST["default"]["USER"]
	password = DATABASES_LIST["default"]["PASSWORD"]
	host = DATABASES_LIST["default"]["HOST"]
	database = DATABASES_LIST["default"]["NAME"]

	try:
		cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
		return cnx
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_BAD_DB_ERROR:
			with mysql.connector.connect(user=user, password=password, host=host) as cnx:
				cursor = cnx.cursor()
				sql = "CREATE DATABASE {}".format(database)
				cursor.execute(sql)
				raise DatabaseCreatedException(database)
		else:
			raise err