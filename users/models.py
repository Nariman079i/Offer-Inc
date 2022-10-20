
from django.db.models import *
from django.contrib.auth.models import *
from  .admin import *
class User(AbstractUser):
    call_number = CharField(max_length=255)
    password = CharField(max_length=255)

admin.site.register(User)