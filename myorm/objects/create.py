from datetime import datetime

from .base import ObjectsBase


from myorm.exceptions.objects.base import CreateDataNotFoundException, FieldNotInThisClassException


class ObjectsCreate(ObjectsBase):
	def create(self, **kwargs):
		from myorm.fields.fields.foreign import ForeignField
		from myorm.fields.fields.datetime import DatetimeField

		insert_columns_arr = []
		insert_values_arr = []

		insert_data = kwargs
		model_fields_dict = self.model_instance.fields_dict


		for field_name in insert_data.keys():
			if field_name not in model_fields_dict.keys():
				raise FieldNotInThisClassException

		
		for field_name, field_instance in model_fields_dict.items():
			if isinstance(field_instance, DatetimeField):
				if field_name not in insert_data and not field_instance.null:
					if field_instance.auto_add:
						insert_data["datetime"] = datetime.now()
					else:
						insert_data["datetime"] = None


			if field_name in insert_data:
				if field_instance.validate(insert_data[field_name]):
					insert_values_arr.append(insert_data[field_name])

					if isinstance(field_instance, ForeignField):
						field_name = field_name + "_id"

					insert_columns_arr.append(field_name)
		

		self.sql_dict["sql_mode"] = "insert"
		self.sql_dict["insert_columns"] = insert_columns_arr
		self.sql_dict["insert_values"] = insert_values_arr

		return self