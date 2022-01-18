from .create import ObjectsCreate
from .update import ObjectsUpdate
from .delete import ObjectsDelete
from .select import ObjectsSelect
from .filter import ObjectsFilter



class Objects(
	ObjectsCreate,
	ObjectsUpdate,
	ObjectsDelete,
	ObjectsSelect,
	ObjectsFilter
	):
	pass