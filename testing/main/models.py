from django.db import models


class Table(models.Model):
    title = models.CharField('Название', max_length=150)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title


class Form(models.Model):
    nikname = models.CharField('nikname', max_length=150)
    razdel = models.CharField('Раздел', max_length=150)
    USER_NAME = models.CharField('ФИО', max_length=150)
    Birthday = models.DateField('День рождения', max_length=10)
    Froms = models.CharField('Гражданство', max_length=60)
    Pasport = models.CharField('Серия и номер паспорта', max_length=20)
    INFO = models.TextField('Сведения о недвижемости', max_length=120)
    Data_pasport = models.DateField('Дата выдачи', max_length=10)
    Number = models.CharField('Номер телефона', max_length=10)
    email = models.CharField('email', max_length=100)
    status = models.CharField('Статус', max_length=1)

    def get_absolute_url(self):
        return f'/form/{self.id}'
    def __str__(self):
        return self.nikname

class Form2(models.Model):
    nikname = models.CharField('nikname', max_length=150)
    razdel = models.CharField('Раздел', max_length=150)
    USER_NAME = models.CharField('ФИО', max_length=150)
    Birthday = models.DateField('День рождения', max_length=10)
    Froms = models.CharField('Гражданство', max_length=60)
    Pasport = models.CharField('Серия и номер паспорта', max_length=20)
    INFO = models.TextField('Сведения о недвижемости', max_length=120)
    Data_pasport = models.DateField('Дата выдачи', max_length=10)
    Number = models.CharField('Номер телефона', max_length=10)
    email = models.CharField('email', max_length=100)
    status = models.CharField('Статус', max_length=1)

    def __str__(self):
        return self.nikname
class Form3(models.Model):
    nikname = models.CharField('nikname', max_length=150)
    razdel = models.CharField('Раздел', max_length=150)
    USER_NAME = models.CharField('ФИО', max_length=150)
    Birthday = models.DateField('День рождения', max_length=10)
    Froms = models.CharField('Гражданство', max_length=60)
    Pasport = models.CharField('Серия и номер паспорта', max_length=20)
    INFO = models.CharField('Сведения о недвижемость', max_length=40)
    Data_pasport = models.DateField('Дата выдачи', max_length=10)
    Number = models.CharField('Номер телефона', max_length=10)
    email = models.CharField('email', max_length=100)
    status = models.CharField('Статус', max_length=1)

    def __str__(self):
        return self.nikname

class Form4(models.Model):
    nikname = models.CharField('nikname', max_length=150)
    razdel = models.CharField('Раздел', max_length=150)
    USER_NAME = models.CharField('ФИО', max_length=150)
    Birthday = models.DateField('День рождения', max_length=10)
    Froms = models.CharField('Гражданство', max_length=60)
    Pasport = models.CharField('Серия и номер паспорта', max_length=20)
    INFO = models.CharField('Недвижемость', max_length=40)
    Data_pasport = models.DateField('Дата выдачи', max_length=10)
    Number = models.CharField('Номер телефона', max_length=10)
    email = models.CharField('email', max_length=100)
    status = models.CharField('Статус', max_length=1)

    def __str__(self):
        return self.nikname
class Form5(models.Model):
    nikname = models.CharField('nikname', max_length=150)
    razdel = models.CharField('Раздел', max_length=150)
    USER_NAME = models.CharField('ФИО', max_length=150)
    Birthday = models.DateField('День рождения', max_length=10)
    Froms = models.CharField('Гражданство', max_length=60)
    Number = models.CharField('Номер телефона', max_length=10)
    email = models.CharField('email', max_length=100)
    status = models.CharField('Статус', max_length=1)

    def __str__(self):
        return self.nikname
class Form6(models.Model):
    nikname = models.CharField('nikname', max_length=150)
    razdel = models.CharField('Раздел', max_length=150)
    USER_NAME = models.CharField('ФИО', max_length=150)
    Birthday = models.DateField('День рождения', max_length=10)
    Number = models.CharField('Номер телефона', max_length=10)
    email = models.CharField('email', max_length=100)
    status = models.CharField('Статус', max_length=1)

    def __str__(self):
        return self.nikname