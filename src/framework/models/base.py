from copy import copy

from framework.objects import Objects
from framework.fields import IntegerField
from framework.fields.base import FieldBase

from framework.exceptions.models.fields import FieldNotInThisClassException



class ModelBase(object):

	def __init__(self, **kwargs):
		ModelBase.objects = Objects(self.__class__)
		
		if kwargs:
			
			self.input_data = kwargs
			self.is_saved = False

			self.__set_fields_to_attr()
			self.__create_fields_list()
			self.set_values(self.input_data)
			
		else:
			self.is_saved = None


	def __set_fields_to_attr(self) ->dict:
		for k, v in self.__class__.__dict__.items():
			if issubclass(v.__class__, FieldBase):
				setattr(self, k, copy(v))
		return True


	def __create_fields_list(self):
		self.fields_list = []
		for k, v in self.__class__.__dict__.items():
			if issubclass(v.__class__, FieldBase):
				self.fields_list.append(k)
		return True


	def __check_fields_in_this_class(self, input_data:dict) ->bool:
		for k in input_data.keys():
			if k in self.fields_list:
				pass
			else:
				raise FieldNotInThisClassException(k)
		return True


	def set_values(self, input_data:dict):
		if self.__check_fields_in_this_class():
			for field in self.fields_list:
				field_instalce = getattr(self, field)
				if field in input_data: field_instalce.set_value(value=self.input_data[field])
				else: field_instalce.set_value(value=None)
			return True
		return False


	def save(self):
		self.is_saved = True
		return True