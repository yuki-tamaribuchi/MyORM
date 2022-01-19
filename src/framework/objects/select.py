from .base import ObjectsBase


class ObjectsSelect(ObjectsBase):
	def get(self, **kwargs):
		where_caluse = kwargs
		self.model_instance.get(where_caluse)
		return self.model_instance


	def all(self):
		pass