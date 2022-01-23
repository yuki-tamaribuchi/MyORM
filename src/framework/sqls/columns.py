def generate_columns(columns_dict):

	columns_arr = []

	for k, v in columns_dict.items():
		for column_name in v:
			columns_arr.append("{}.{}".format(k, column_name))
	
	columns_sql = ", ".join(columns_arr)
	return columns_sql