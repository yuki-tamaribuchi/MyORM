from .base import ObjectsBase



class ObjectsDelete(ObjectsBase):
	def delete(self):
		self.sql_dict["sql_mode"] = "delete"
		
		return self