from ..base import FieldBase

from framework.exceptions.fields.base import BrankValidationException, MaxLengthValidationException


class StringField(FieldBase):

	data_type = str

	def __init__(
		self,
		max_length: int,
		null: bool,
		unique: bool,
		brank: bool,
		*args,
		**kwargs
		) -> None:

		super().__init__(null, unique, *args, **kwargs)
		self.max_length = max_length
		self.brank = brank

	def validate(self, value) -> bool:
		if super().validate(value):
			if (not self.brank) and value == "":
				raise BrankValidationException
			
			if len(value)>self.max_length:
				raise MaxLengthValidationException
				
		return True