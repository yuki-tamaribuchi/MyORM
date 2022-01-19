from .base import ObjectsBase


class ObjectsCreate(ObjectsBase):
	def create(self, **kwargs):
		input_data = kwargs
		self.model_class().set_values(input_data=input_data)