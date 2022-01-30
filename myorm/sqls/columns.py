from myorm.fields.fields.foreign import ForeignField


def generate_columns(objects_instance):

	columns_arr = []

	table_columns = objects_instance.sql_dict["columns"]
	for table in table_columns:
		table_name = table["table"].__name__.lower()
		columns = table["columns"]

		for column_name ,column_instance in columns:
			if isinstance(column_instance, ForeignField):
				column_name = column_name + "_id"
			columns_arr.append("{}.{}".format(table_name, column_name))
		
	columns_sql = ", ".join(columns_arr)
	return columns_sql	