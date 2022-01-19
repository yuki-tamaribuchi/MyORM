from .templates import INSERT_TEMPLATE as template


def generate_insert_sql(model_instance):
	table_name = model_instance.__class__.__name__.lower()
	fields_list = model_instance.__dict__["fields_list"]

	insert_colums_arr = []
	insert_values_arr = []
	
	for field_name in fields_list:
		field_instace = getattr(model_instance, field_name)
		if field_instace.value is not None:
			insert_colums_arr.append(field_name)
			insert_values_arr.append(str(field_instace.value))
	
	insert_columns_sql = ", ".join(insert_colums_arr)
	insert_values_sql = ", ".join(insert_values_arr)

	sql = template.format(
		table=table_name,
		columns=insert_columns_sql,
		values=insert_values_sql
	)
	return sql