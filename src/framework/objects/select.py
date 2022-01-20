from .base import ObjectsBase


class ObjectsSelect(ObjectsBase):
	def get(self, **kwargs):
		self.sql_dict["sql_mode"] = "select"
		self.sql_dict["where"] = kwargs

		return self


	def all(self):
		pass