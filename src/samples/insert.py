from models import Users, Entry

import random

def insert_users(n):
	for i in range(n):
		Users().objects.create(username="sample{}".format(i), lucky_number=random.randint(1,20)).run()

def insert_entry(n):
	for i in range(n):
		Entry().objects.create(title="sample{}".format(i), writer=i+1).run()