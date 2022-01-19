from .base import ObjectsBase


class ObjectsCreate(ObjectsBase):
	def create(self, **kwargs):
		input_data = kwargs
		model_class_instance =self.model_class()
		model_class_instance.set_values(input_data=input_data)
		model_class_instance.save()
		return model_class_instance