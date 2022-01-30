from myorm.exceptions.fields.base import NotNullValidationException, DataTypeValidationException



class FieldBase(object):

	data_type = None

	def __init__(
		self,
		null: bool,
		unique: bool,
		*args,
		**kwargs
		) -> None:
		self.null = null
		self.unique = unique
		self.value = None


	def __repr__(self) -> str:
		return str(self.value)


	def validate(self, value) ->bool:
		if (not self.null) and (value is None):
			raise NotNullValidationException

		if value is not None:
			if not (type(value) == self.data_type):
				raise DataTypeValidationException

		#uniqueは後ほど実装
		
		return True


	def set_value(self, value, is_result_data) ->bool:
		if is_result_data:
			self.value = value
			return True


		if self.validate(value):
			self.value = value
			return True
	

	def field_sql(self):
		sql_template = "{null_option}{unique_option}"

		if not self.null:
			null_option = "NOT NULL "
		else:
			null_option = ""

		if self.unique:
			unique_option = "UNIQUE"
		else:
			unique_option = ""
		
		sql = sql_template.format(
			null_option=null_option,
			unique_option=unique_option
		)
		return sql