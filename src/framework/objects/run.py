from .base import ObjectsBase

from framework.connection.execute import execute
from framework.connection.fetch import fetch

from framework.sqls.select import generate_select_sql
from framework.sqls.insert import generate_insert_sql

from framework.exceptions.objects.base import ResultNotOneException


class ObjectsRun(ObjectsBase):
	def run(self):

		if self.sql_dict["sql_mode"]  == "select":
			sql = generate_select_sql(self)
		elif self.sql_dict["sql_mode"] == "insert":
			sql = generate_insert_sql(self.sql_dict)
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
			elif self.sql_dict["select_mode"] == "filter":
				result = fetch(sql)
				return result
		else:
			result = execute(sql)
		return result




	def __set_value_to_object(self, result):
		model_instances = []

		fields_dict_keys = self.model_instance.fields_dict.keys()

		for r in result:
			values_dict = {}
			for i, k in enumerate(fields_dict_keys):
				values_dict[k] =r[i]
			
			self.model_instance.set_values(values_dict, True)
			model_instances.append(self.model_instance)
		
		return model_instances