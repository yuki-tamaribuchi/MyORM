from .templates import UPDATE_TEMPLATE


def generate_update_sql(sql_dict):
	
	if sql_dict["update_sets"]:
		sets = ""
	else:
		pass
		#raise err

	if sql_dict["where"]:
		where = ""
	else:
		where = ""

	if sql_dict["order_by"]:
		order_by = ""
	else:
		order_by = ""

	if sql_dict["limit"]:
		limit = ""
	else:
		limit = ""

	
	update_sql = UPDATE_TEMPLATE.format(
		table=sql_dict["table"],
		sets=sets,
		where=where,
		order_by=order_by,
		limit=limit
	)
	return update_sql