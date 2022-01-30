from .base import ObjectsBase

from myorm.exceptions.objects.base import SelectRelatedTableNotFoundException


class SelectRelated(ObjectsBase):
	
	def select_related(self, *args):

		related_data = args

		for data in related_data:
			if "__" in data:
				pass
			else:
				left_table = self.sql_dict["table"]
				right_table = self.__get_table(data)

				self.sql_dict["join"].append(
					{
						"left_table": left_table,
						"right_table": right_table,
					}
				)

				right_table_columns = list(right_table().fields_dict.items())

				self.sql_dict["columns"].append({
					'table': right_table,
					'columns': right_table_columns
				})

		return self


	def __get_table(self, table_name):
		if table_name in self.model_instance.fields_dict:
			field = self.model_instance.fields_dict[table_name]
			table = field.relation_model
			return table
		else:
			raise SelectRelatedTableNotFoundException