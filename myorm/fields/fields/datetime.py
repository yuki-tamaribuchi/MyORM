from datetime import datetime

from ..base import FieldBase

class DatetimeField(FieldBase):

	data_type = datetime

	def __init__(
		self,
		null:bool,
		auto_add:bool,
		*args,
		**kwargs
	):

		super().__init__(null, unique=False, *args, **kwargs)
		self.auto_add = auto_add

	def field_sql(self):
		super_sql = super().field_sql()
		
		sql = "DATETIME " + super_sql
		return sql