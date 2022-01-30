from attr import field
from .base import ObjectsBase

from myorm.fields.fields.foreign import ForeignField
from myorm.exceptions.objects.base import FilterConditionNotSpecifiedException, FilterColumnNotFoundException


class ObjectsFilter(ObjectsBase):
	def filter(self, *args, **kwargs):
		all_filter_condition_arr = []

		if kwargs:
			filter_contidion = kwargs
			filter_contidion_dict = {}
			
			
			for filter_field_name, filter_field_value in filter_contidion.items():
				self.__check_field_exists(filter_field_name)
				field_instance = self.model_instance.fields_dict[filter_field_name]
				if isinstance(field_instance, ForeignField):
					filter_field_name = filter_field_name + "_id"

				filter_contidion_dict[filter_field_name] = {
					"table_name": self.model_instance.__class__.__name__.lower(),
					"field_instance": field_instance,
					"field_value": filter_field_value
				}
				
			all_filter_condition_arr.append(filter_contidion_dict)


		else:
			raise FilterConditionNotSpecifiedException

		
		self.sql_dict["where"] = all_filter_condition_arr


		if self.sql_dict["sql_mode"] is None:
			self.sql_dict["sql_mode"] = "select"
			self.sql_dict["select_mode"] = "filter"
			self.sql_dict["table"] = self.model_instance.__class__

			self.sql_dict["columns"].append({
				"table": self.model_instance.__class__,
				"columns": list(self.model_instance.fields_dict.items())
			})

		return self


	def __check_field_exists(self, filter_field_name):
		if filter_field_name in self.model_instance.fields_dict.keys():
			return True

		raise FilterColumnNotFoundException