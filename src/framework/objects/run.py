from .base import ObjectsBase
from framework.connection.execute import execute
from framework.connection.fetch import fetch

from framework.sqls.select import generate_select_sql
from framework.sqls.insert import generate_insert_sql
from framework.sqls.delete import generate_delete_sql
from framework.sqls.update import generate_update_sql

from framework.exceptions.objects.base import ResultNotOneException


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
			print('error')


		if self.sql_dict["sql_mode"] == "select":
			if self.sql_dict["select_mode"] == "get":
				result = fetch(sql)
				result_len = len(result)
				if result_len>1:
					raise ResultNotOneException
				elif result_len == 1:
					return result

				else:
					return None

			elif self.sql_dict["select_mode"] in ["filter", "all"]:
				result = fetch(sql)
				return result
		else:
			result = execute(sql)
		return result