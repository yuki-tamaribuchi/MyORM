from .templates import WHERE_TEMPLATE


def generate_where_sql(all_filter_conditon_arr):

	filter_arr = []

	for filter_condition in all_filter_conditon_arr:
		for k, v in filter_condition.items():
			filter_arr.append("{} = \"{}\"".format(k, v["field_value"]))
	

	filter_sql = " AND ".join(filter_arr)
	
	sql = WHERE_TEMPLATE.format(
		where_clause=filter_sql
	)
	return sql