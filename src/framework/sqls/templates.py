SELECT_TEMPLATE = "SELECT {options} {columns} FROM {table} {join} {where} {order_by} {having} {limit}"
INSERT_TEMPLATE = "INSERT INTO {table} ({columns}) VALUES ({values})"
UPDATE_TEMPLATE = "UPDATE {table} SET {sets} {where}"
DELETE_TEMPLATE = "DELETE FROM {table} {where} {order_by} {limit}"