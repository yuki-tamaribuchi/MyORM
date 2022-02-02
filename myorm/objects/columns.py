from .base import ObjectsBase


from myorm.exceptions.objects.base import ColumnsNotSpecifiedException, ColumnNotFoundException

class ColumnsObject(ObjectsBase):
	def columns(self, *args):
		if args:
			columns_arr = self.__create_columns(args)
			self.__set_columns(columns_arr)
			return self
		else:
			raise ColumnsNotSpecifiedException

	def __create_columns(self, columns):
		columns_arr = []
		model_fields_dict = self.sql_dict["table"]().fields_dict
		for column in columns:
			columns_name, columns_instance = self.__get_columns_instance(column, model_fields_dict)
			columns_arr.append((columns_name, columns_instance))
		return columns_arr

				

	def __get_columns_instance(self, column, model_fields_dict):
		from myorm.fields.fields.foreign import ForeignField

		for field_name, field_instance in model_fields_dict.items():
			if isinstance(field_instance, ForeignField):
				field_name = field_name + "_id"

			if column == field_name:
				return (field_name, field_instance)

		else:
			raise ColumnNotFoundException

	
	def __set_columns(self, columns_arr):
		for i, table in enumerate(self.sql_dict["columns"]):
			if table["table"] == self.sql_dict["table"]:
				self.sql_dict["columns"][i]["columns"] = columns_arr
		return True
				