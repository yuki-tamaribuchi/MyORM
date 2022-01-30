from ..base import FieldBase

from myorm.exceptions.fields.base import RelatedModelValidationException

from myorm.models.on_delete import OnDeleteBase


class ForeignField(FieldBase):

	data_type = int

	def __init__(
		self,
		relation_model,
		on_delete: OnDeleteBase,
		null: bool,
		unique: bool=False,
		*args,
		**kwargs
		) -> None:

		from myorm.models.base import ModelBase


		super().__init__(null, unique, *args, **kwargs)
		if issubclass(relation_model, ModelBase):
			self.relation_model = relation_model
		else:
			raise RelatedModelValidationException
		
		self.on_delete = on_delete


	def field_sql(self):
		super_sql = super().field_sql()

		sql = "INT " + super_sql
		return sql