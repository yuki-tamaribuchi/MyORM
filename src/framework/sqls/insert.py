from .templates import INSERT_TEMPLATE


def generate_insert_sql(sql_dict):
	
	columns = ", ".join(sql_dict["insert_columns"])
	values = ", ".join(sql_dict["insert_values"])


	insert_sql = INSERT_TEMPLATE.format(
		table=sql_dict["table"],
		columns=columns,
		values=values
	)

	return insert_sql