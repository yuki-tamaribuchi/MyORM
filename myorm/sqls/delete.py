from .templates import DELETE_TEMPLATE
from .where import generate_where_sql


def generate_delete_sql(sql_dict):

	if sql_dict["order_by"]:
		order_by = ""
	else:
		order_by = ""

	if sql_dict["where"]:
		where=generate_where_sql(sql_dict["where"])
	else:
		where = ""

	if sql_dict["limit"]:
		limit = ""
	else:
		limit = ""

	delete_sql = DELETE_TEMPLATE.format(
		table=sql_dict["table"].__name__.lower(),
		where=where,
		order_by=order_by,
		limit=limit
	)

	return delete_sql