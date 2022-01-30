from myorm.models.model import Model
from myorm.fields import IntegerField, StringField, ForeignField
from myorm.models import CASCADE

from .users import Users

class Entry(Model):

	id = IntegerField(null=False, unique=True, primary_key=True)
	title = StringField(max_length=30, null=False, unique=False, brank=False)
	writer = ForeignField(Users, on_delete=CASCADE,null=False)