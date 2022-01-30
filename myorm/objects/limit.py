from .base import ObjectsBase

from myorm.exceptions.objects.base import LimitNumberMustBePositiveException


class ObjectsLimit(ObjectsBase):
	def limit(self, n:int):
		if n>0:
			self.sql_dict["limit"] = n
			return self

		else:
			raise LimitNumberMustBePositiveException
