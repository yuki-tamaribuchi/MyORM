from datetime import datetime

from ..base import FieldBase

class DatetimeField(FieldBase):

	data_type = datetime

	def __init__(
		self,
		null:bool,
		auto_now:bool,
		auto_update:bool,
		*args,
		**kwargs
	):

		super().__init__(null, unique=False, *args, **kwargs)
		self.auto_now = auto_now
		self.auto_update = auto_update

	def field_sql(self):
		super_sql = super().field_sql()
		
		sql = "DATETIME " + super_sql
		return sql