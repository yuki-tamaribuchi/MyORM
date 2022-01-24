from framework.fields.fields.foreign import ForeignField


def generate_columns(objects_instance):

	columns_arr = []

	#if objects_instance.sql_dict["columns"]["custom"]:
	#	table_name = objects_instance.model_instance.__class__.__name__.lower()
	#	for column in objects_instance.sql_dict["columns"]["custom"]:
	#		columns_instance = getattr(objects_instance.model_instance, column)
	#		if isinstance(columns_instance, ForeignField):
	#			column = column + "_id"
	#		columns_arr.append("{}.{}".format(table_name, column))

	#else:
	#	column_tables = objects_instance.sql_dict["columns"]
	#	column_tables.pop("custom")
	#	
	#	for table_name, columns in column_tables.items():
	#		for column in columns:
	#			columns_instance = getattr(objects_instance.model_instance, column)
	#			if isinstance(columns_instance, ForeignField):
	#				column = column + "_id"
	#			columns_arr.append("{}.{}".format(table_name, column))

	columns_arr.append("*")

	columns_sql = ", ".join(columns_arr)
	return columns_sql	