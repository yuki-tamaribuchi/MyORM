from .base import ObjectsBase

from framework.sqls.select import generate_select_sql


class ObjectsRun(ObjectsBase):
	def run(self):

		if self.sql_dict["sql_mode"]  == "select":
			sql = generate_select_sql(self.sql_dict)

		else:
			print('error')


		print(sql)

		if self.sql_dict["sql_mode"] == "select":
			result = None
		else:
			result = None

		return result
			