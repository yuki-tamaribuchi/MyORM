from framework.models.model import Model
from framework.fields import IntegerField, StringField, ForeignField
from framework.models import CASCADE

from .users import Users

class Entry(Model):

	id = IntegerField(null=False, unique=True, primary_key=True)
	title = StringField(max_length=30, null=False, unique=False, brank=False)
	writer = ForeignField(Users, on_delete=CASCADE,null=False)