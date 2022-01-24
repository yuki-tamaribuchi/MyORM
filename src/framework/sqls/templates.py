CREATE_TABLE_TEMPLATE = "CREATE TABLE {table} ( {fields} )"

SELECT_TEMPLATE = "SELECT {options} {columns} FROM {table} {join} {where} {order_by} {having} {limit}"
INSERT_TEMPLATE = "INSERT INTO {table} ({columns}) VALUES ({values})"
UPDATE_TEMPLATE = "UPDATE {table} SET {sets} {where} {order_by} {limit}"
DELETE_TEMPLATE = "DELETE FROM {table} {where} {order_by} {limit}"

WHERE_TEMPLATE = "WHERE  {where_clause}"
JOIN_TEMPLATE = "LEFT JOIN {table} ON {condition} "