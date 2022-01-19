from copy import copy

from framework.objects import Objects
from framework.fields import IntegerField
from framework.fields.base import FieldBase

from framework.exceptions.models.fields import FieldNotInThisClassException, PrimaryKeyCannotUpdateException



class ModelBase(object):

	def __init__(self, **kwargs):
		ModelBase.objects = Objects(self)

		self.is_saved = None

		self.__set_fields_to_attr()
		self.__create_fields_list()
		
		if kwargs:
			
			self.input_data = kwargs
			self.set_values(self.input_data)
			self.is_saved = False


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
		if self.__check_fields_in_this_class(input_data=input_data):
			for field in self.fields_list:
				field_instalce = getattr(self, field)
				if field in input_data: field_instalce.set_value(value=input_data[field])
				else: field_instalce.set_value(value=None)

			self.is_saved = False

			return True

		return False


	def update_values(self, update_data:dict):
		#ネストが深すぎるため後でどうにかする
		if self.__check_fields_in_this_class(input_data=update_data):
			for field in self.fields_list:
				field_instance = getattr(self, field)

				#フィールドがある場合
				if field in update_data:

					#Primary Keyかを調べ、Primary Keyの場合変更させない
					if hasattr(field_instance, "primary_key"):
						if field_instance.primary_key:
							raise PrimaryKeyCannotUpdateException


					#フィールドのデータがある場合は値を変更
					if update_data[field] is not None:
						field_instance.set_value(value=update_data[field])
					
				#フィールドがない場合はパス
				else:
					field_instance.set_value(value=field_instance.value)

			self.is_saved = False
			return True
		return False



	def save(self):
		self.is_saved = True
		print("Output from save(). :", self.__dict__)
		return True


	def delete(self):
		print("Deleted.")
		return True

	
	def get(self, where_caluse):
		# where_calueからWHEREを生成してSELECT文を発行
		# resultが1つなら値をセットして返す
		# resultが2つ以上ならエラー
		print("get called.: ", where_caluse)