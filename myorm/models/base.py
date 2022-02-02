from copy import copy

from myorm.objects import Objects
from myorm.fields import IntegerField
from myorm.fields.base import FieldBase

from myorm.exceptions.models.fields import FieldNotInThisClassException, PrimaryKeyCannotUpdateException


from myorm.sqls.insert import generate_insert_sql



class ModelBase(object):

	def __init__(self, **kwargs):
		ModelBase.objects = Objects(self)
		self.fields_dict = {}

		self.__set_fields_to_attr()
		self.__create_fields_dict()


	def __set_fields_to_attr(self) ->dict:
		for k, v in self.__class__.__dict__.items():
			if issubclass(v.__class__, FieldBase):
				setattr(self, k, copy(v))
		return True


	def __create_fields_dict(self):
		for k, v in self.__class__.__dict__.items():
			if issubclass(v.__class__, FieldBase):
				self.fields_dict[k] = v
		return True


	def create_table(self):
		from myorm.sqls.create_table import generate_create_table_sql

		generate_create_table_sql(self.__class__)