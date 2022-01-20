from .columns import generate_columns
from .where import generate_where_sql
from .templates import SELECT_TEMPLATE



def generate_select_sql(sql_dict):


	if sql_dict["options"]:
		options = ""
	else:
		options = ""

	if sql_dict["columns"]:
		columns = generate_columns(sql_dict["columns"])
	else:
		columns = "*"
	
	if sql_dict["join"]:
		join = ""
	else:
		join = ""

	if sql_dict["where"]:
		where = generate_where_sql(sql_dict["where"])
	else:
		where = ""

	if sql_dict["order_by"]:
		order_by = ""
	else:
		order_by = ""

	if sql_dict["having"]:
		having = ""
	else:
		having = ""

	if sql_dict["limit"]:
		limit = ""
	else:
		limit = ""

	select_sql = SELECT_TEMPLATE.format(
		options=options,
		columns=columns,
		table=sql_dict["table"],
		join=join,
		where=where,
		order_by=order_by,
		having=having,
		limit=limit
	)
	return select_sql