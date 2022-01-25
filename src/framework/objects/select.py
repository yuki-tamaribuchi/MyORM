from .base import ObjectsBase


class ObjectsSelect(ObjectsBase):
	def get(self, **kwargs):
		self.sql_dict["sql_mode"] = "select"
		self.sql_dict["select_mode"] = "get"
		self.sql_dict["where"] = kwargs

		columns = list(self.model_instance.fields_dict.items())
		self.sql_dict["columns"].append({
			"table": self.model_instance.__class__,
			"columns": columns
		})
		return self


	def all(self):
		pass