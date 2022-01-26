from .base import ObjectsBase

class ObjectsReverse(ObjectsBase):
	def reverse(self):
		self.sql_dict["sort"] = "desc"
		return self