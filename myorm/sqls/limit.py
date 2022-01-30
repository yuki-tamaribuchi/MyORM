from .templates import LIMIT_TEMPLATE

def generate_limit_sql(limit):
	return LIMIT_TEMPLATE.format(
		limit=limit
	)