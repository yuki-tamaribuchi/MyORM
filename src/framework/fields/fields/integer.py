from wsgiref import validate
from ..base import FieldBase

from framework.exceptions.fields.base import PrimaryKeyValidationException, NotNullValidationException

class IntegerField(FieldBase):

	data_type = int

	def __init__(
		self,
		null: bool,
		unique: bool,
		primary_key: bool = False,
		*args,
		**kwargs
		) -> None:

		super().__init__(null, unique, *args, **kwargs)
		self.primary_key = primary_key

	def validate(self, value) -> bool:
		if self.primary_key:
			if value is not None:
				raise PrimaryKeyValidationException
			try:
				super().validate(value)
			except NotNullValidationException:
				pass
		else:
			super().validate(value)
		return True
			



		#if not super().validate(value):
		#	return False

		#if self.primary_key and value is not None:
		#	raise PrimaryKeyValidationException