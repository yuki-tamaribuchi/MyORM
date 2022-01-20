class ObjectsBase(object):
	def __init__(self, model_instance):
		self.model_instance = model_instance

		self.sql_dict = {
			'sql_mode': None,
			'table': model_instance.__class__.__name__.lower(),
			'options': None,
			'insert_columns': None,
			'insert_values': None,
			'join': None,
			'where': None,
			'group_by': None,
			'having': None,
			'order_by': None,
			'limit': None,
			'update_sets': None
		}