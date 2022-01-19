from ..base import FieldBase

from framework.exceptions.fields.base import PrimaryKeyValidationException

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
		if not super().validate(value):
			return False

		if self.primary_key and value is not None:
			raise PrimaryKeyValidationException
		return True