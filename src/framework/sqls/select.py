from .columns import generate_columns
from .where import generate_where_sql
from .join import generate_join_sql
from .templates import SELECT_TEMPLATE



def generate_select_sql(objects_instance):


	if objects_instance.sql_dict["options"]:
		options = ""
	else:
		options = ""

	if objects_instance.sql_dict["columns"]:
		columns = generate_columns(objects_instance)
	else:
		print('columns err')

	
	if objects_instance.sql_dict["join"]:
		join = generate_join_sql(objects_instance.sql_dict["join"])
	else:
		join = ""

	if objects_instance.sql_dict["where"]:
		where = generate_where_sql(objects_instance.sql_dict["where"])
	else:
		where = ""

	if objects_instance.sql_dict["order_by"]:
		order_by = ""
	else:
		order_by = ""

	if objects_instance.sql_dict["having"]:
		having = ""
	else:
		having = ""

	if objects_instance.sql_dict["limit"]:
		limit = ""
	else:
		limit = ""

	select_sql = SELECT_TEMPLATE.format(
		options=options,
		columns=columns,
		table=objects_instance.sql_dict["table"].__name__.lower(),
		join=join,
		where=where,
		order_by=order_by,
		having=having,
		limit=limit
	)
	return select_sql