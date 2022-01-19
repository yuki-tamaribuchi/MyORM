from .base import ObjectsBase



class ObjectsDelete(ObjectsBase):
	def delete(self):
		self.model_instance.delete()