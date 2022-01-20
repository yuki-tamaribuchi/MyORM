from .base import ObjectsBase

from framework.exceptions.objects.base import ColumnsNotSpecifiedException

class ColumnsObject(ObjectsBase):
	def columns(self, *args):
		if args:
			self.sql_dict["columns"] = args
			return self
		else:
			raise ColumnsNotSpecifiedException