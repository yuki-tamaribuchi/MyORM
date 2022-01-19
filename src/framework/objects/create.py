from .base import ObjectsBase


class ObjectsCreate(ObjectsBase):
	def create(self, **kwargs):
		input_data = kwargs
		self.model_instance.set_values(input_data=input_data)
		self.model_instance.save()
		return self.model_instance