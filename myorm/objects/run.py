from types import NoneType
from .base import ObjectsBase
from myorm.connection.execute import execute
from myorm.connection.fetch import fetch

from myorm.sqls.select import generate_select_sql
from myorm.sqls.insert import generate_insert_sql
from myorm.sqls.delete import generate_delete_sql
from myorm.sqls.update import generate_update_sql

from myorm.exceptions.objects.base import ResultNotOneException, SQLModeNotAcceptableException, SelectModeNotAcceptableException


class ObjectsRun(ObjectsBase):
	def run(self):

		if self.sql_dict["sql_mode"]  == "select":
			sql = generate_select_sql(self)
		elif self.sql_dict["sql_mode"] == "insert":
			sql = generate_insert_sql(self.sql_dict)
		elif self.sql_dict["sql_mode"] == "delete":
			sql = generate_delete_sql(self.sql_dict)
		elif self.sql_dict["sql_mode"] == "update":
			sql = generate_update_sql(self.sql_dict)
		else:
			raise SQLModeNotAcceptableException


		if self.sql_dict["sql_mode"] == "select":
			if self.sql_dict["select_mode"] == "get":
				results = fetch(sql)
				results_len = len(results)
				if results_len>1:
					raise ResultNotOneException
				elif results_len == 1:
					pass
				else:
					results = None

			elif self.sql_dict["select_mode"] in ["filter", "all"]:
				results = fetch(sql)

			else:
				raise SelectModeNotAcceptableException
			
			return self.__create_result_dict(results)


		elif self.sql_dict["sql_mode"] == "insert":
			return execute(sql, True)
			
		else:
			return execute(sql, False)



	def __create_result_dict(self, results):
		
		if self.sql_dict["sql_mode"] == "select":
			return self.__set_result_to_dict(results)



	def __create_table_columns_dict(self):
		table_columns_dict = {}

		for table in self.sql_dict["columns"]:
			table_name = table["table"].__name__
			table_columns_dict[table_name] = {}
			
			for column in table["columns"]:
				table_columns_dict[table_name][column[0]] = None

		return table_columns_dict


	
	def __set_result_to_dict(self, results):
		
		results_dict_arr = []

		if type(results) is NoneType:
			return results_dict_arr

		
		for result in results:
			table_columns_dict = self.__create_table_columns_dict()
			i=0

			for table_name, column_names in table_columns_dict.items():
				for column_name in column_names:
					table_columns_dict[table_name][column_name] = result[i]
					i+=1

			results_dict_arr.append(table_columns_dict)

		return results_dict_arr
