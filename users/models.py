from django.db.models import *
from django.contrib.auth.models import *
from .admin import *


class Experience(Model):
    position = CharField(verbose_name="Должность", max_length=60, null=True)
    specialization = ForeignKey('Specialization', on_delete=CASCADE, null=True, verbose_name='Специализация', )
    start_work = DateField(verbose_name='Дата начала работы', null=True)
    end_work = DateField(verbose_name='Дата окончания работы', null=True)
    about_company = TextField(verbose_name='О компании', null=True)

    class Meta:
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"


admin.site.register(Experience)


class UserData(AbstractUser):
    username = CharField(verbose_name='Имя пользователя', max_length=255, null=False, default='', unique=True)
    email = EmailField(verbose_name='Адрес электронной почты', max_length=255, null=False, default='', unique=True)
    password = CharField(verbose_name='Пароль', max_length=255, null=False, default='')
    img = ImageField(verbose_name='Фото профиля', upload_to='img/', null=True)
    first_name = CharField(verbose_name='Имя', max_length=60, null=True),
    last_name = CharField(verbose_name='Фамилия', max_length=60, null=True),
    gender = CharField(verbose_name='Пол', max_length=20, choices=(('m', 'Mужской'), ('w', 'Женский')), null=True)
    call_number = CharField(verbose_name="Номер телефона", max_length=12, null=True)
    inn = CharField(verbose_name='ИНН', max_length=12, null=True)
    person_site = CharField(verbose_name='Сайт', max_length=255, null=True)
    about_me = TextField(verbose_name='Обо мне', max_length=500, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователи"


admin.site.register(UserData)


class Company(Model):
    title = CharField(verbose_name='Наименование', max_length=255, null=True)
    date_created = DateField(verbose_name='Дата основания', null=True)
    locate = ForeignKey('Locate', on_delete=CASCADE, null=True, verbose_name='Локация')
    call_number = CharField(verbose_name='Номер телефона', max_length=12, null=True)
    email = EmailField(verbose_name='Адрес электронной почты', max_length=40, null=True)
    link = SlugField(verbose_name='Сайт компании', max_length=255, null=True)
    short_description = TextField(verbose_name='Краткое описание', null=True)
    about_company = TextField(verbose_name='Основная информация о компании', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Компании"
        verbose_name_plural = "Компании"


admin.site.register(Company)


class Skill(Model):
    title = CharField(verbose_name='Название', max_length=255, null=True)
    get_date = DateField(verbose_name='Дата получения', null=True, help_text="Формат даты: ДД.ММ.ГГГГ")
    description = TextField(verbose_name='Описание', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"


admin.site.register(Skill)


class Specialization(Model):
    title = CharField(verbose_name='Название', max_length=255, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"


admin.site.register(Specialization)


class Industry(Model):
    title = CharField(verbose_name='Название', max_length=255, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Индустрия"
        verbose_name_plural = "Индустрии"


admin.site.register(Industry)


class Region(Model):
    title = CharField(verbose_name='Название региона', max_length=255, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


admin.site.register(Region)


class Locate(Model):
    region = ForeignKey(Region, on_delete=CASCADE, null=True, verbose_name='Регион')
    locality = CharField(verbose_name='Населенный пункт', max_length=255, null=True)
    population = IntegerField(verbose_name='Численность населения', null=True)

    def __str__(self):
        return self.locality

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


admin.site.register(Locate)


class UserLink(Model):
    user = OneToOneField(UserData, on_delete=CASCADE, verbose_name="Пользователь")
    link_vk = CharField(max_length=255, null=True, verbose_name="Ссылка на VK")
    link_tm = CharField(max_length=255, null=True, verbose_name="Ссылка на Telegram")
    link_in = CharField(max_length=255, null=True, verbose_name="Ссылка на Linkedin")

    class Meta:
        verbose_name = "Социальные сети пользователя"
        verbose_name_plural = "Социальные сети пользователей"


admin.site.register(UserLink)


class CompanyLink(Model):
    company = OneToOneField(Company, on_delete=CASCADE, verbose_name="Компания")
    link_vk = CharField(max_length=255, null=True, verbose_name="Ссылка на VK")
    link_tm = CharField(max_length=255, null=True, verbose_name="Ссылка на Telegram")
    link_in = CharField(max_length=255, null=True, verbose_name="Ссылка на Linkedin")

    class Meta:
        verbose_name = "Социальные сети компании"
        verbose_name_plural = "Социальные сети компаний"


admin.site.register(CompanyLink)


class UserSkill(Model):
    user = ForeignKey(UserData, on_delete=CASCADE)
    skill = ForeignKey(Skill, on_delete=CASCADE)

    def __str__(self):
        return self.user
    class Meta:
        verbose_name = "Достижение пользователя"
        verbose_name_plural = "Достижения пользователей"


admin.site.register(UserSkill)


class CoFounder(Model):
    company = OneToOneField(Company, on_delete=CASCADE, verbose_name="Компания")
    user = ForeignKey(UserData, on_delete=CASCADE, verbose_name="Соучредитель")

    class Meta:
        verbose_name = "Соучредитель"
        verbose_name_plural = "Соучредители"


admin.site.register(CoFounder)


class CoCompany(Model):
    company = OneToOneField(Company, on_delete=CASCADE, related_name="MainCompany", verbose_name="Компания")
    co_company = ForeignKey(Company, on_delete=CASCADE, related_name="SubCompany", verbose_name="Партнер")

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"


admin.site.register(CoCompany)


class UserExperience(Model):
    user = ForeignKey(UserData, on_delete=CASCADE, verbose_name="Пользователь")
    experience = ForeignKey(Experience, on_delete=CASCADE, verbose_name="Опыт работы")

    class Meta:
        verbose_name = "Опыт работы пользователя"
        verbose_name_plural = "Опыт работы пользователей"


admin.site.register(UserExperience)


class UserLocation(Model):
    user = OneToOneField(UserData, on_delete=CASCADE, verbose_name="Пользователь")
    locate = OneToOneField(Locate, on_delete=CASCADE, verbose_name="Населенный пункт")

    class Meta:
        verbose_name = "Локация пользователя"
        verbose_name_plural = "Локации пользователей"


admin.site.register(UserLocation)

