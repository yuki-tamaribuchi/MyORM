from framework.models import Model
from framework.fields import StringField, IntegerField

class Users(Model):

	username = StringField(max_length=30, null=False, unique=True, brank=False)
	lucky_number = IntegerField(null=True, unique=False)