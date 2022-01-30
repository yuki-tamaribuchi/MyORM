from .create import ObjectsCreate
from .update import ObjectsUpdate
from .delete import ObjectsDelete
from .select import ObjectsSelect
from .filter import ObjectsFilter
from .order_by import ObjectsOrderBy
from .reverse import ObjectsReverse
from .limit import ObjectsLimit
from .columns import ColumnsObject
from .select_related import SelectRelated
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
	ColumnsObject,
	SelectRelated,
	ObjectsRun
	):
	pass