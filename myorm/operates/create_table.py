from myorm.sqls.create_table import generate_create_table_sql
from myorm.connection.execute import execute

from models import models


def create_all_table():
	for model in models:
		sql = generate_create_table_sql(model)
		execute(sql)
	return True
		