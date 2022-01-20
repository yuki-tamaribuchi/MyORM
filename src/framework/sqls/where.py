from .templates import WHERE_TEMPLATE


def generate_where_sql(where_clause):

	where_arr = []

	for k, v in where_clause.items():

		where_arr.append("{} = \"{}\"".format(k, str(v)))
	
	

	where_clause_sql = " AND ".join(where_arr)

	sql = WHERE_TEMPLATE.format(
		where_clause=where_clause_sql
	)

	return sql
	