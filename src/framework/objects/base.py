class ObjectsBase(object):
	def __init__(self, model_instance):
		self.model_instance = model_instance

		self.sql_dict = {
			'sql_mode': None,
			'select_mode': None,
			'table': model_instance.__class__,
			'options': None,
			'columns': [],
			'insert_columns': None,
			'insert_values': None,
			'join': [],
			'where': None,
			'group_by': None,
			'having': None,
			'order_by': None,
			'limit': None,
			'update_sets': None
		}