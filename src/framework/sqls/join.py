from .templates import JOIN_TEMPLATE

def generate_join_sql(join_arr):
	right_table_arr = []
	condition_arr = []

	for join in join_arr:
		right_table_arr.append(join["right_table"])
		condition_arr.append(
			"{left_table}.{column} = {right_table}.id".format(
				left_table=join["left_table"],
				column=join["column"],
				right_table=join["right_table"]
			)
		)
	
	join_sql = ""

	for i in range(len(right_table_arr)):
		join_sql += JOIN_TEMPLATE.format(
			table=right_table_arr[i],
			condition=condition_arr[i]
		)

	return join_sql