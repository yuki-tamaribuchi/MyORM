from .templates import CREATE_TABLE_TEMPLATE as template

from framework.fields.base import FieldBase

def generate_create_table_sql(model_class):
	from framework.fields.fields.foreign import ForeignField

	table_name = model_class.__name__.lower()

	fields_sql_arr = []
	
	for k, v in model_class.__dict__.items():
		if issubclass(v.__class__, FieldBase):
			if issubclass(v.__class__, ForeignField):
				field_sql_template = "{field_name} {field_sql}, FOREIGN KEY({field_name}) REFERENCES {foreign_table_name}(id) ON DELETE {on_delete}"

				field_name = k + "_id"
				foreign_table_name = v.relation_model.__name__.lower()
				on_delete = v.on_delete.__name__

				field_sql = field_sql_template.format(
					field_name=field_name,
					field_sql=v.field_sql(),
					foreign_table_name=foreign_table_name,
					on_delete=on_delete
				)

			else:
				field_sql_template = "{field_name} {field_sql}"
				field_name = k

				field_sql = field_sql_template.format(
					field_name=field_name,
					field_sql=v.field_sql()
				)
			
			fields_sql_arr.append(field_sql)
			

	fields_sql = ", ".join(fields_sql_arr)

	sql = template.format(
		table=table_name,
		fields=fields_sql
	)
	return sql