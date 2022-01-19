from .base import ObjectsBase



class ObjectsUpdate(ObjectsBase):
	def update(self, **kwargs):
		update_data = kwargs
		self.model_instance.update_values(update_data)
		self.model_instance.save()
		return self.model_instance