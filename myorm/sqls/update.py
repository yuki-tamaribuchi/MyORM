from .templates import UPDATE_TEMPLATE


from .where import generate_where_sql
from myorm.exceptions.objects.base import UpdateSetsNotFoundException
def generate_update_sql(sql_dict):
	
	if sql_dict["update_sets"]:
		sets = ", ".join(sql_dict["update_sets"])
	else:
		raise UpdateSetsNotFoundException

	if sql_dict["where"]:
		where = generate_where_sql(sql_dict["where"])
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
		table=sql_dict["table"].__name__.lower(),
		sets=sets,
		where=where,
		order_by=order_by,
		limit=limit
	)
	return update_sql