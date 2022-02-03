from django.db import models


# Create your models here.
class Bolted_By(models.Model):
    name=models.CharField(max_length=50,verbose_name='Имя пробившего маршрут',default='Неизвестно')
    def __str__(self):
        return self.name
class Grade(models.Model):
    grade=models.CharField(max_length=10, verbose_name='Выберите сложность маршрута',default='Проект')
    def __str__(self):
        return self.grade
class Location(models.Model):
    location=models.CharField(max_length=50,verbose_name='Название локации',default='Неизвестно')
    additional_info=models.CharField(max_length=1000,help_text='Введите информацию по поводу парковки, источников воды итд',verbose_name='Доп информация',default='Все очевидно :)')
    def __str__(self):
        return self.location
class Comf(models.Model):
    comfort=models.IntegerField(verbose_name='Уровень комфорта от 1 до 10',default=5)
    def __str__(self):
        return str(self.comfort)


class Sector(models.Model):
    location = models.ForeignKey('Location',max_length=50,verbose_name='Локация',on_delete=models.CASCADE)
    sector=models.CharField(verbose_name='Название сектора',max_length=30,default='Еще не придумали')
    def __str__(self):
        return self.sector
class Route(models.Model):
    name=models.CharField(max_length=50,verbose_name="Название маршрута",default='Еще не придумали')
    bolter =models.ManyToManyField('Bolted_by',verbose_name='Имя пробившего',default='Неизвестно')
    grade=models.ForeignKey('Grade',verbose_name='Сложность',on_delete=models.SET_DEFAULT,default='Еще не известно')
    location = models.ForeignKey('Location',verbose_name='Локация',default='Неизвестно',on_delete=models.CASCADE)
    comfort=models.ForeignKey('Comf',verbose_name='Насколько комфортная трасса от 1 до 10',on_delete=models.SET_DEFAULT,default=5)
    rope_len=models.IntegerField(verbose_name='Необходимая длина веревки',default=60)
    quickdraws=models.IntegerField(verbose_name='Количество оттяжек',default=16)
    coords=models.URLField(max_length=1000,verbose_name='Ссылка на локацию трассы',help_text='Принимаются метки с гугл карт',null=True)
    extra_info=models.CharField(max_length=300,verbose_name='Доп информация о трассе',null=True)
    sector=models.ForeignKey('Sector',verbose_name='Выберите сектор',max_length=30, on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.name

class Boulder(models.Model):
    name=models.CharField(max_length=50,verbose_name="Название камня",default='Еще не придумали')
    bolter =models.ManyToManyField('Bolted_by',verbose_name='Нашел',default='Неизвестно')
    grade = models.ForeignKey('Grade', verbose_name='Сложность', on_delete=models.SET_DEFAULT,default=33)
    comfort=models.ForeignKey('Comf',verbose_name='Насколько комфортная трасса от 1 до 10',on_delete=models.SET_DEFAULT,default=5)
    height=models.IntegerField(default=0,verbose_name='Высота')
    extra_info=models.CharField(max_length=300,verbose_name='Доп информация о трассе',null=True)
    photo=models.ImageField(upload_to='boulder_photos/',null=True,verbose_name="Фото")
    coords=models.URLField(max_length=1000,verbose_name='Ссылка на локацию трассы',help_text='Принимаются метки с гугл карт',null=True)
    amount_of_crashpads=models.IntegerField(default=0,null=True,verbose_name='Кол-во крешпедов')
    location = models.ForeignKey('Location',verbose_name='Локация',default='Неизвестно',on_delete=models.CASCADE)
    sector=models.ForeignKey('Sector',verbose_name='Выберите сектор',max_length=30, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name



