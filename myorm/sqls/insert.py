from .templates import INSERT_TEMPLATE


def generate_insert_sql(sql_dict):
	
	columns = ", ".join(sql_dict["insert_columns"])
	values_arr = ["\"{}\"".format(v) for v in sql_dict["insert_values"]]
	values = ", ".join(values_arr)


	insert_sql = INSERT_TEMPLATE.format(
		table=sql_dict["table"].__name__.lower(),
		columns=columns,
		values=values
	)

	return insert_sql