from .templates import JOIN_TEMPLATE

from myorm.fields.fields.foreign import ForeignField

def generate_join_sql(join_arr):
	right_table_name_arr = []
	condition_arr = []

	for join in join_arr:

		for k, v in join["left_table"]().fields_dict.items():
			if isinstance(v, ForeignField) and v.relation_model == join["right_table"]:
				left_table_column = k + "_id"

		left_table_name = join["left_table"].__name__.lower()
		right_table_name = join["right_table"].__name__.lower()

		right_table_name_arr.append(right_table_name)
		condition_arr.append("{}.{} = {}.id".format(left_table_name, left_table_column, right_table_name))

	
	join_sql = ""

	for i in range(len(right_table_name_arr)):
		join_sql += JOIN_TEMPLATE.format(
			table=right_table_name_arr[i],
			condition=condition_arr[i]
		)
	return join_sql