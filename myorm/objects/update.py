from .base import ObjectsBase

from myorm.exceptions.objects.base import UpdateDataNotSpecifiedException


class ObjectsUpdate(ObjectsBase):
	def update(self, **kwargs):
		from myorm.fields.fields.datetime import DatetimeField
		from datetime import datetime

		if kwargs:

			update_data= kwargs

			update_sets_arr= []

			for k, v in update_data.items():
				update_sets_arr.append(
					"{} = \"{}\"".format(k, v)
				)

			for k, v in self.model_instance.fields_dict.items():
				if isinstance(v, DatetimeField) and v.auto_update:
					update_sets_arr.append(
						"{} = \"{}\"".format(k, datetime.now())
					)


			self.sql_dict["update_sets"] = update_sets_arr
			self.sql_dict["sql_mode"] = "update"

			return self

		else:
			raise UpdateDataNotSpecifiedException
