from .base import ObjectsBase

from myorm.fields.fields.foreign import ForeignField
from myorm.exceptions.objects.base import GetConditonNotSpecifiedException, GetColumnNotFoundException



class ObjectsSelect(ObjectsBase):
	def get(self, **kwargs):

		if kwargs:

			all_filter_condition_arr = []

			get_conditon = kwargs

			get_condition_dict = {}

			for get_field_name, get_field_value in get_conditon.items():
				self.__check_field_exists(get_field_name)
				field_instance = self.model_instance.fields_dict[get_field_name]

				if isinstance(field_instance, ForeignField):
					get_field_name = get_field_name + "_id"
				
				get_condition_dict[get_field_name] = {
					"table_name": self.model_instance.__class__.__name__.lower(),
					"field_instance": field_instance,
					"field_value": get_field_value
				}


			all_filter_condition_arr.append(get_condition_dict)


			self.sql_dict["where"] = all_filter_condition_arr
			self.sql_dict["sql_mode"] = "select"
			self.sql_dict["select_mode"] = "get"


			columns = list(self.model_instance.fields_dict.items())
			self.sql_dict["columns"].append({
				"table": self.model_instance.__class__,
				"columns": columns
			})

			return self
		
		else:
			raise GetConditonNotSpecifiedException


	def __check_field_exists(self, get_field_name):
		if get_field_name in self.model_instance.fields_dict.keys():
			return True
		raise GetColumnNotFoundException

	def all(self):
		self.sql_dict["sql_mode"] = "select"
		self.sql_dict["select_mode"] = "all"

		columns = list(self.model_instance.fields_dict.items())
		self.sql_dict["columns"].append({
				"table": self.model_instance.__class__,
				"columns": columns
			})

		return self