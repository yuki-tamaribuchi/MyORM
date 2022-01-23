from .base import ObjectsBase


class ObjectsSelect(ObjectsBase):
	def get(self, **kwargs):
		self.sql_dict["sql_mode"] = "select"
		self.sql_dict["select_mode"] = "get"
		self.sql_dict["where"] = kwargs
		self.sql_dict["columns"][self.model_instance.__class__.__name__.lower()] = list(self.model_instance.fields_dict.keys())
		return self


	def all(self):
		pass