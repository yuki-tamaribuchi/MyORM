from .base import ObjectsBase

class ObjectsRevese(ObjectsBase):
	def reverse(self):
		self.sql_dict["sort"] = "desc"
		return self