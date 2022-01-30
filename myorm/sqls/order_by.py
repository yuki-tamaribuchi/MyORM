from .templates import ORDER_BY_TEMPLATE


def generate_orderby_sql(sql_dict):

	order_by_arr = []

	order_by_columns = sql_dict["order_by"]

	if sql_dict["sort"]:
		sort = sql_dict["sort"]
	else:
		sort = "asc"


	for column in order_by_columns:
		order_by_arr.append("{} {}".format(column, sort))

	order_by_clause_sql = ", ".join(order_by_arr)
	order_by_sql = ORDER_BY_TEMPLATE.format(
		order_by_clause=order_by_clause_sql
	)

	return order_by_sql