from ..base import FieldBase


class FloadField(FieldBase):

	data_type = float

	def __init__(
		self,
		null: bool,
		unique: bool,
		*args,
		**kwargs
		) -> None:
		super().__init__(null, unique, *args, **kwargs)