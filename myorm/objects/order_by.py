from .base import ObjectsBase

from myorm.exceptions.objects.base import OrderByKeyNotSpecifiedException

class ObjectsOrderBy(ObjectsBase):
	def order_by(self, *args):

		if args:
			self.sql_dict["order_by"] = list(args)
			return self

		else:
			raise OrderByKeyNotSpecifiedException
