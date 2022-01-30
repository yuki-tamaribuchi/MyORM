import mysql.connector
from mysql.connector import errorcode

from myorm.exceptions.connection.base import DatabaseCreatedException

from settings.databases import DATABASES_LIST


class DBConnection:

	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, "_instance"):
			cls._instance = super().__new__(cls)
		return cls._instance

	def __init__(self):
		self.user = DATABASES_LIST["default"]["USER"]
		self.password = DATABASES_LIST["default"]["PASSWORD"]
		self.host = DATABASES_LIST["default"]["HOST"]
		self.database = DATABASES_LIST["default"]["NAME"]


	def connect(self):
		try:
			cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)
			return cnx
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_BAD_DB_ERROR:
				with mysql.connector.connect(user=self.user, password=self.password, host=self.host) as cnx:
					cursor = cnx.cursor()
					sql = "CREATE DATABASE {}".format(self.database)
					cursor.execute(sql)
					raise DatabaseCreatedException(self.database)
			else:
				raise err