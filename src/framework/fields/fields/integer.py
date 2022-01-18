from ..base import FieldBase

from framework.exceptions.fields.base import AutoIncrementButNullException

class IntegerField(FieldBase):

	data_type = int

	def __init__(
		self,
		null: bool,
		unique: bool,
		auto_increment: bool=False,
		*args,
		**kwargs
		) -> None:

		super().__init__(null, unique, *args, **kwargs)
		self.auto_increment = auto_increment

	def validate(self, value) -> bool:
		if super().validate(value):
			if self.auto_increment and value is None:
				raise AutoIncrementButNullException
			return True