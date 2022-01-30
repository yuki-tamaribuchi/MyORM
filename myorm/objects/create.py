from .base import ObjectsBase

from myorm.fields.fields.foreign import ForeignField
from myorm.exceptions.objects.base import CreateDataNotFoundException, FieldNotInThisClassException


class ObjectsCreate(ObjectsBase):
	def create(self, **kwargs):		
		if not kwargs:
			raise CreateDataNotFoundException

		insert_columns_arr = []
		insert_values_arr = []


		self.sql_dict["sql_mode"] = "insert"
		model_fields_dict = self.model_instance.fields_dict
		insert_data =kwargs
		for k, v in insert_data.items():
			if k not in model_fields_dict:
				raise FieldNotInThisClassException
			

			if model_fields_dict[k].validate(v):
				insert_values_arr.append("\"" + str(v) + "\"")

				if isinstance(model_fields_dict[k], ForeignField):
					insert_columns_arr.append(k + "_id")
				else:
					insert_columns_arr.append(k)


		
		self.sql_dict["insert_columns"] = insert_columns_arr
		self.sql_dict["insert_values"] = insert_values_arr




		return self