from django.db.models import *
from django.contrib.auth.models import *
from .admin import *


class Expirience(Model):
    position = CharField(verbose_name="Должность", max_length=60, null=True)
    specialization = ForeignKey('Specialization', on_delete=CASCADE, null=True, verbose_name='Специализация', )
    start_work = DateField(verbose_name='Дата начала работы', null=True)
    end_work = DateField(verbose_name='Дата окончания работы',null=True)
    about_company = TextField(verbose_name='О компании',null=True)


class UserData(AbstractUser):
    username = CharField(verbose_name='Имя пользователя', max_length=255, null=False, default='', unique=True)
    email = EmailField(verbose_name='Адрес электронной почты', max_length=255, null=False, default='', unique=True)
    password = CharField(verbose_name='Пароль', max_length=255, null=False, default='')
    img = ImageField(verbose_name='Фото профиля', upload_to='img/', null=True)
    first_name = CharField(verbose_name='Имя',max_length=60, null=True),
    last_name = CharField(verbose_name='Фамилия' , max_length=60, null=True),
    gender = CharField(verbose_name='Пол', max_length=20, choices=(('m', 'Mужской'), ('w', 'Женский')), null=True)
    call_number = CharField(verbose_name="Номер телефона", max_length=12, null=True)
    inn = CharField(verbose_name='ИНН', max_length=12, null=True)
    person_site = CharField(verbose_name='Сайт' ,max_length=255, null=True)
    about_me = TextField(verbose_name='Обо мне', max_length=500, null=True)

    def __str__(self):
        return self.username


class Company(Model):
    title = CharField(verbose_name='Наименование',max_length=255, null=True)
    date_created = DateField(verbose_name='Дата основания' ,null=True)
    locate = ForeignKey('Locate', on_delete=CASCADE, null=True, verbose_name='Локация')
    call_number = CharField(verbose_name='Номер телефона' ,max_length=12, null=True)
    email = EmailField(verbose_name='Адрес электронной почты' ,max_length=40, null=True)
    link = SlugField(verbose_name='Сайт компании', max_length=255, null=True)
    short_description = TextField(verbose_name='Краткое описание' ,null=True)
    about_company = TextField(verbose_name='Основная информация о компании' ,null=True)

    def __str__(self):
        return self.title


class Skill(Model):
    title = CharField(verbose_name='Название', max_length=255, null=True)
    get_date = DateField(verbose_name='Дата получения', null=True)
    description = TextField(verbose_name='Описание', null=True)

    def __str__(self):
        return self.title


class Specialization(Model):
    title = CharField(verbose_name='Название',max_length=255, null=True)

    def __str__(self):
        return self.title


class Industry(Model):
    title = CharField(verbose_name='Название',max_length=255, null=True)

    def __str__(self):
        return self.title


class Region(Model):
    title = CharField(verbose_name='Название региона',max_length=255, null=True)

    def __str__(self):
        return self.title


class Locate(Model):
    region = ForeignKey(Region, on_delete=CASCADE, null=True, verbose_name='Регион')
    locality = CharField(verbose_name='Населенный пункт', max_length=255, null=True)
    population = IntegerField(verbose_name='Численность населения',null=True)

    def __str__(self):
        return self.locality



model_tables = [User, Expirience, UserData, Company, Skill, Specialization, Industry, Region, Locate]


admin.site.register(model_tables)
