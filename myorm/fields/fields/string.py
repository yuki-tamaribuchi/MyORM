from ..base import FieldBase

from myorm.exceptions.fields.base import BrankValidationException, MaxLengthValidationException


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

	
	def field_sql(self):
		super_sql = super().field_sql()

		sql_template = "{max_length}"

		sql = sql_template.format(
			max_length = "VARCHAR(" + str(self.max_length) +") "
		) + super_sql
		return sql