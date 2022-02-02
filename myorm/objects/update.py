from .base import ObjectsBase

from myorm.exceptions.objects.base import UpdateDataNotSpecifiedException


class ObjectsUpdate(ObjectsBase):
	def update(self, **kwargs):
		if kwargs:

			update_data= kwargs

			update_sets_arr= []

			for k, v in update_data.items():
				update_sets_arr.append(
					"{} = \"{}\"".format(k, v)
				)

			self.sql_dict["update_sets"] = update_sets_arr
			self.sql_dict["sql_mode"] = "update"

			return self

		else:
			raise UpdateDataNotSpecifiedException
