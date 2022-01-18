from framework.exceptions.fields.base import NotNullValidationException, DataTypeValidationException



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


	def set_value(self, value) ->bool:
		if self.validate(value):
			self.value = value
		return True