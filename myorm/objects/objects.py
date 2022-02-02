from .create import ObjectsCreate
from .update import ObjectsUpdate
from .delete import ObjectsDelete
from .select import ObjectsSelect
from .filter import ObjectsFilter
from .order_by import ObjectsOrderBy
from .reverse import ObjectsReverse
from .limit import ObjectsLimit
from .columns import ObjectsColumns
from .select_related import ObjectsSelectRelated
from .run import ObjectsRun



class Objects(
	ObjectsCreate,
	ObjectsUpdate,
	ObjectsDelete,
	ObjectsSelect,
	ObjectsFilter,
	ObjectsOrderBy,
	ObjectsReverse,
	ObjectsLimit,
	ObjectsColumns,
	ObjectsSelectRelated,
	ObjectsRun
	):
	pass