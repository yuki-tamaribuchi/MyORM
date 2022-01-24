from .base import ObjectsBase

from framework.exceptions.objects.base import SelectRelatedTableNotFoundException


class SelectRelated(ObjectsBase):
	
	def select_related(self, *args):

		table_names = args

		for table in table_names:
			if "__" in table:
				pass
			else:
				left_table = self.sql_dict["table"]
				right_table = self.__get_table(table)
				right_table_name = right_table.__name__.lower()
				table = table + "_id"
				self.sql_dict["join"].append(
					{
						'left_table': left_table,
						'right_table': right_table_name,
						'column': table
					}
				)

				right_table_columns = list(right_table().__dict__["fields_dict"].keys())

				self.sql_dict["columns"][right_table_name] = right_table_columns

		return self


	def __get_table(self, table_name):
		if table_name in self.model_instance.fields_dict:
			field = self.model_instance.fields_dict[table_name]
			table = field.relation_model
			return table
		else:
			raise SelectRelatedTableNotFoundException