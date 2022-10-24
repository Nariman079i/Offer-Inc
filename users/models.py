from django.db.models import *
from django.contrib.auth.models import *
from .admin import *





class Expirience(Model):

    position = CharField(max_length=60, null=True)
    specialization_id = ForeignKey('Specialization', on_delete=CASCADE, null=True)
    start_work = DateField(null=True)
    end_work = DateField(null=True)
    about_company = TextField(null=True)


class UserData(AbstractUser):
    username = CharField(max_length=255,null=False, default='',unique=True)
    email = EmailField(max_length=255, null=False, default='', unique=True)
    password = CharField(max_length=255, null=False, default='')
    img = ImageField(upload_to='img/', null=True)
    first_name = CharField(max_length=60, null=True),
    last_name = CharField(max_length=60, null=True),
    gender = CharField(max_length=20, choices=(('m', 'Mужской'), ('w', 'Женский')), null=True)
    call_number = CharField(max_length=12 , null=True)
    mail = EmailField(max_length=255, null=True)
    inn = CharField(max_length=12, null=True)
    person_site = CharField(max_length=255, null=True)
    about_me = TextField(max_length=500, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Company(Model):
    title = CharField(max_length=255, null=True)
    date_created = DateField(null=True)
    locate_id = ForeignKey('Locate', on_delete=CASCADE, null=True)
    call_number = CharField(max_length=12, null=True)
    email = EmailField(max_length=40, null=True)
    link = SlugField(max_length=255, null=True)
    short_description = TextField(null=True)
    about_company = TextField(null=True)

    def __str__(self):
        return self.title


class Skill(Model):
    title = CharField(max_length=255, null=True)
    get_date = DateField(null=True)
    description = TextField(null=True)

    def __str__(self):
        return self.title


class Specialization(Model):
    title = CharField(max_length=255, null=True)

    def __str__(self):
        return self.title


class Industry(Model):
    title = CharField(max_length=255, null=True)

    def __str__(self):
        return self.title


class Region(Model):
    title = CharField(max_length=255, null=True)

    def __str__(self):
        return self.title


class Locate(Model):
    region = ForeignKey(Region, on_delete=CASCADE, null=True)
    locality = CharField(max_length=255, null=True)
    population = IntegerField(null=True)

    def __str__(self):
        return self.locality


model_tables = [User, Expirience, UserData, Company, Skill, Specialization, Industry, Region, Locate]
admin.site.register(model_tables)
